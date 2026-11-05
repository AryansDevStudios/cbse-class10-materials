import os
import json
import re
import hashlib

SOURCE_DIR = r"D:\CBSE Materials"
OUTPUT_PATHS = [
    r"C:\Users\aryan\.gemini\antigravity\scratch\academic-command-center\cbse_materials_index.json",
    r"D:\CBSE Materials\cbse_materials_index.json"
]

def format_size(bytes_num):
    if bytes_num < 1024:
        return f"{bytes_num} B"
    elif bytes_num < 1024 * 1024:
        return f"{bytes_num / 1024:.1f} KB"
    else:
        return f"{bytes_num / (1024 * 1024):.2f} MB"

def generate_id(rel_path):
    return hashlib.md5(rel_path.encode('utf-8')).hexdigest()[:12]

def clean_title(filename):
    name, _ = os.path.splitext(filename)
    # Replace underscores and hyphens with spaces
    cleaned = name.replace('_', ' ').replace('-', ' ')
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned

def extract_set_code(filename):
    s = filename.rsplit('.', 1)[0]
    # Clean common marking scheme prefixes
    s = re.sub(r'^(MS\s*041|MS\s*089|MS\s*086|MS\s*087|MS|J0\w+|X_002_\w+|Marking\s*scheme)\s*[_ -]*', '', s, flags=re.I)
    # 3 numbers like 30-1-1, 30_1_1, 30 1 1
    m = re.search(r'(\d+)[\s\-_]+(\d+)[\s\-_]+(\d+)', s)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    # 3-digit packed format like 311 -> 3-1-1
    m2 = re.search(r'\b([234]\d{2})\b', s)
    if m2:
        val = m2.group(1)
        return f"{val[0]}-{val[1]}-{val[2]}"
    # 30(B) or 30-B or 30 B
    m3 = re.search(r'(\d+)\s*[\(\-_]?\s*([A-Za-z])\s*\)?', s)
    if m3:
        return f"{m3.group(1)}-{m3.group(2).upper()}"
    m4 = re.search(r'Set[\s_-]*(\d+)', filename, re.IGNORECASE)
    if m4:
        return f"Set {m4.group(1)}"
    return None

def build_index():
    print(f"Scanning {SOURCE_DIR}...")
    materials = []
    
    # Track files for pairing
    qp_map = {} # (category, subject, year, code) -> item
    ms_map = {} # (category, subject, year, code) -> item

    for root, dirs, files in os.walk(SOURCE_DIR):
        for f in files:
            # Skip git / temporary / generated files
            if f.startswith('.') or f in ['cbse_materials_index.json', 'index.html', 'serve.py']:
                continue
            
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, SOURCE_DIR).replace('\\', '/')
            parts = rel_path.split('/')
            category = parts[0]
            
            size_bytes = os.path.getsize(full_path)
            ext = os.path.splitext(f)[1].lower()
            
            # Detect Subject
            subject = "General"
            low_rel = rel_path.lower()
            if "social science" in low_rel or "social_science" in low_rel or "sst" in low_rel:
                subject = "Social Science"
            elif "mathematics" in low_rel or "maths" in low_rel or "math" in low_rel:
                subject = "Mathematics"
            elif "science" in low_rel:
                subject = "Science"
            elif "english" in low_rel:
                subject = "English"
            elif "hindi" in low_rel:
                subject = "Hindi"
            elif "information technology" in low_rel or "information_technology" in low_rel or "it402" in low_rel:
                subject = "Information Technology"
                
            # Detect Year
            year = None
            for y in ['2027', '2026', '2025', '2024', '2023', '2022', '2021-22']:
                if y in rel_path:
                    year = y
                    break
                    
            # Detect Type
            item_type = "document"
            low_f = f.lower()
            if "sqp" in low_f or "sample" in low_f:
                if "_ms" in low_f or "marking" in low_f or "ms." in low_f:
                    item_type = "marking_scheme"
                else:
                    item_type = "sample_paper"
            elif "marking scheme" in low_rel or "_ms" in low_f or "ms " in low_f or "ms_" in low_f or "final.pdf" in low_f:
                item_type = "marking_scheme"
            elif "question paper" in low_rel or "practice_paper" in low_f:
                if "_ms" in low_f:
                    item_type = "marking_scheme"
                else:
                    item_type = "question_paper"
            elif "topper" in low_rel:
                item_type = "topper_script"
            elif "exemplar" in low_rel:
                if "answer" in low_f:
                    item_type = "exemplar_solution"
                else:
                    item_type = "exemplar_chapter"
            elif "laboratory manual" in low_rel:
                item_type = "lab_manual"
            elif "curriculum" in low_rel or "syllabus" in low_rel:
                item_type = "syllabus"
            elif "framework" in low_f or "learning_standards" in low_f:
                item_type = "framework"
            elif "question_bank" in low_f or "item_bank" in low_f:
                item_type = "question_bank"
            elif "chapter" in low_rel or ext == ".pdf" and "ncert" in low_rel:
                item_type = "textbook_chapter"
            elif ext == ".md" and "map" in low_rel:
                item_type = "guide"
            elif ext in ['.jpg', '.png']:
                item_type = "cover_image"
            elif ext == '.zip':
                item_type = "archive_bundle"
                
            # Format friendly title
            set_code = extract_set_code(f)
            title = clean_title(f)
            
            # Specific title cleanups
            if item_type == "sample_paper":
                title = f"{subject} Sample Question Paper {year or ''}".strip()
            elif item_type == "marking_scheme" and ("sqp" in low_f or "sample" in low_f):
                title = f"{subject} Marking Scheme (SQP) {year or ''}".strip()
            elif item_type == "topper_script":
                title = f"{subject} Topper Answer Script ({year or ''})".strip()
            elif item_type == "lab_manual":
                title = f"Science Practical - {title}"
            elif item_type == "exemplar_chapter":
                title = f"{subject} Exemplar - {title}"
            elif item_type == "exemplar_solution":
                title = f"{subject} Exemplar Solutions & Answers"
            elif item_type == "syllabus":
                title = f"{subject} Curriculum & Blueprint 2026-27"
            elif item_type in ["question_paper", "marking_scheme"] and set_code:
                prefix = "Question Paper" if item_type == "question_paper" else "Marking Scheme"
                title = f"{subject} {prefix} ({set_code}) {year or ''}".strip()
                
            item_id = generate_id(rel_path)
            
            item = {
                "id": item_id,
                "title": title,
                "filename": f,
                "category": category,
                "subject": subject,
                "year": year,
                "type": item_type,
                "set_code": set_code,
                "rel_path": rel_path,
                "extension": ext,
                "size_bytes": size_bytes,
                "size_formatted": format_size(size_bytes),
                "paired_id": None,
                "paired_title": None,
                "paired_path": None
            }
            
            materials.append(item)
            
            # Track for pairing
            key = (category, subject, year, set_code)
            if item_type in ["question_paper", "sample_paper"]:
                qp_map[key] = item
            elif item_type == "marking_scheme":
                ms_map[key] = item

    # Pair QPs and MSs
    pair_count = 0
    for key, qp in qp_map.items():
        if key in ms_map:
            ms = ms_map[key]
            qp["paired_id"] = ms["id"]
            qp["paired_title"] = ms["title"]
            qp["paired_path"] = ms["rel_path"]
            
            ms["paired_id"] = qp["id"]
            ms["paired_title"] = qp["title"]
            ms["paired_path"] = qp["rel_path"]
            pair_count += 1

    # Also handle SQP pairing where set_code is None
    for item in materials:
        if item["type"] == "sample_paper" and not item["paired_id"]:
            # find corresponding MS
            for other in materials:
                if other["type"] == "marking_scheme" and other["category"] == item["category"] and other["subject"] == item["subject"] and other["year"] == item["year"]:
                    item["paired_id"] = other["id"]
                    item["paired_title"] = other["title"]
                    item["paired_path"] = other["rel_path"]
                    other["paired_id"] = item["id"]
                    other["paired_title"] = item["title"]
                    other["paired_path"] = item["rel_path"]
                    pair_count += 1
                    break

    # Stats compilation
    stats = {
        "total_materials": len(materials),
        "total_size_bytes": sum(m["size_bytes"] for m in materials),
        "total_size_formatted": format_size(sum(m["size_bytes"] for m in materials)),
        "subjects": {},
        "categories": {},
        "years": {},
        "types": {},
        "paired_sets_count": pair_count
    }
    
    for m in materials:
        stats["subjects"][m["subject"]] = stats["subjects"].get(m["subject"], 0) + 1
        stats["categories"][m["category"]] = stats["categories"].get(m["category"], 0) + 1
        y = m["year"] or "Universal"
        stats["years"][y] = stats["years"].get(y, 0) + 1
        stats["types"][m["type"]] = stats["types"].get(m["type"], 0) + 1
        
    catalog = {
        "metadata": {
            "title": "CBSE Class 10 Academic Repository Index",
            "version": "2.0.0",
            "generated_at": "2026-11-05",
            "source_directory": SOURCE_DIR,
            "target_curriculum": "CBSE Secondary Examination (Class X)",
            "stats": stats
        },
        "materials": materials
    }
    
    for out_path in OUTPUT_PATHS:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, 'w', encoding='utf-8') as fh:
            json.dump(catalog, fh, indent=2, ensure_ascii=False)
        print(f"Index successfully written to {out_path} ({len(materials)} items, {stats['total_size_formatted']})")
        
    return catalog

if __name__ == "__main__":
    build_index()

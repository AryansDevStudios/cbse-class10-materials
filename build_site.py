import os
import json
import re

INDEX_JSON_PATH = r"D:\CBSE Materials\cbse_materials_index.json"
MAP_GUIDE_PATH = r"D:\CBSE Materials\Map Work\CBSE_Class_10_Social_Science_Complete_Map_Work_Guide.md"
SCRATCH_DIR = r"C:\Users\aryan\.gemini\antigravity\scratch\academic-command-center"
DEST_DIR = r"D:\CBSE Materials"

def load_data():
    with open(INDEX_JSON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def load_map_guide():
    if os.path.exists(MAP_GUIDE_PATH):
        with open(MAP_GUIDE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def build():
    data = load_data()
    map_guide_md = load_map_guide()
    data_json_str = json.dumps(data, ensure_ascii=False)
    map_guide_json_str = json.dumps(map_guide_md, ensure_ascii=False)

    html_content = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0" />
  <meta name="description" content="CBSE Class 10 Academic Command Center - High-efficiency archive of official board papers, marking schemes, textbooks, exemplars, and topper answers." />
  <title>CBSE Academic Command Center — Class 10 Vault</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    /* ============================================================
       DESIGN TOKENS — High-Efficiency Linear / DevDocs Dark Theme
       ============================================================ */
    :root {{
      --bg-canvas: #090b10;
      --bg-subtle: #0f131c;
      --bg-surface: #151a26;
      --bg-elevated: #1b2232;
      --bg-overlay: #232c40;
      --bg-hover: rgba(255, 255, 255, 0.05);
      --bg-active: rgba(99, 102, 241, 0.15);

      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-medium: rgba(255, 255, 255, 0.14);
      --border-focus: #6366f1;

      --text-primary: #f8fafc;
      --text-secondary: #94a3b8;
      --text-muted: #64748b;
      --text-inverse: #090b10;

      --accent-indigo: #6366f1;
      --accent-indigo-soft: rgba(99, 102, 241, 0.12);
      --accent-cyan: #06b6d4;
      --accent-cyan-soft: rgba(6, 182, 212, 0.12);
      --accent-emerald: #10b981;
      --accent-emerald-soft: rgba(16, 185, 129, 0.12);
      --accent-amber: #f59e0b;
      --accent-amber-soft: rgba(245, 158, 11, 0.12);
      --accent-rose: #f43f5e;
      --accent-rose-soft: rgba(244, 63, 94, 0.12);
      --accent-purple: #8b5cf6;
      --accent-purple-soft: rgba(139, 92, 246, 0.12);

      --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.3);
      --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.4);
      --shadow-lg: 0 12px 32px rgba(0, 0, 0, 0.5);
      --shadow-glow: 0 0 24px rgba(99, 102, 241, 0.25);

      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 14px;
      --radius-full: 9999px;

      --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;

      --sidebar-width: 290px;
      --header-height: 64px;
      --transition-fast: 150ms cubic-bezier(0.16, 1, 0.3, 1);
      --transition-smooth: 250ms cubic-bezier(0.16, 1, 0.3, 1);
    }}

    /* Light Theme Override */
    [data-theme="light"] {{
      --bg-canvas: #f8fafc;
      --bg-subtle: #f1f5f9;
      --bg-surface: #ffffff;
      --bg-elevated: #f8fafc;
      --bg-overlay: #ffffff;
      --bg-hover: rgba(0, 0, 0, 0.04);
      --bg-active: rgba(99, 102, 241, 0.1);

      --border-subtle: rgba(0, 0, 0, 0.08);
      --border-medium: rgba(0, 0, 0, 0.14);
      --border-focus: #4f46e5;

      --text-primary: #0f172a;
      --text-secondary: #475569;
      --text-muted: #94a3b8;
      --text-inverse: #ffffff;

      --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.06);
      --shadow-md: 0 4px 14px rgba(0, 0, 0, 0.08);
      --shadow-lg: 0 12px 28px rgba(0, 0, 0, 0.12);
      --shadow-glow: 0 0 20px rgba(99, 102, 241, 0.15);
    }}

    /* Reset & Base */
    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html, body {{
      height: 100%;
      font-family: var(--font-sans);
      background: var(--bg-canvas);
      color: var(--text-primary);
      overflow: hidden;
      -webkit-font-smoothing: antialiased;
    }}

    a {{ color: inherit; text-decoration: none; }}
    button, input, select {{ font: inherit; color: inherit; border: none; background: none; }}
    button {{ cursor: pointer; }}

    /* Layout Skeleton */
    .app-root {{
      display: flex;
      flex-direction: column;
      height: 100vh;
      width: 100vw;
      overflow: hidden;
    }}

    /* Header */
    .header {{
      height: var(--header-height);
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 20px;
      gap: 16px;
      z-index: 40;
      flex-shrink: 0;
    }}

    .header-left {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}

    .brand {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-weight: 800;
      font-size: 16px;
      letter-spacing: -0.02em;
    }}

    .brand-icon {{
      width: 32px;
      height: 32px;
      background: linear-gradient(135deg, #6366f1, #06b6d4);
      border-radius: var(--radius-sm);
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-weight: 800;
      font-size: 15px;
      box-shadow: 0 2px 8px rgba(99, 102, 241, 0.4);
    }}

    .brand-badge {{
      font-size: 11px;
      font-weight: 600;
      padding: 2px 8px;
      border-radius: var(--radius-full);
      background: var(--accent-indigo-soft);
      color: var(--accent-indigo);
      border: 1px solid rgba(99, 102, 241, 0.25);
    }}

    /* Omni Search Bar */
    .omni-search-btn {{
      display: flex;
      align-items: center;
      gap: 10px;
      background: var(--bg-subtle);
      border: 1px solid var(--border-subtle);
      padding: 7px 14px;
      border-radius: var(--radius-md);
      color: var(--text-muted);
      font-size: 13px;
      min-width: 280px;
      transition: var(--transition-fast);
    }}

    .omni-search-btn:hover {{
      border-color: var(--border-medium);
      color: var(--text-secondary);
      background: var(--bg-elevated);
    }}

    .search-key-badge {{
      margin-left: auto;
      font-size: 11px;
      font-family: var(--font-mono);
      background: var(--bg-surface);
      border: 1px solid var(--border-medium);
      padding: 2px 6px;
      border-radius: 4px;
      color: var(--text-muted);
    }}

    /* Header Right Actions */
    .header-right {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .stats-pill {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 12px;
      font-weight: 600;
      color: var(--text-secondary);
      background: var(--bg-subtle);
      padding: 6px 12px;
      border-radius: var(--radius-full);
      border: 1px solid var(--border-subtle);
    }}

    .stats-dot {{
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--accent-emerald);
      box-shadow: 0 0 8px var(--accent-emerald);
    }}

    .icon-btn {{
      width: 36px;
      height: 36px;
      border-radius: var(--radius-md);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--text-secondary);
      background: var(--bg-subtle);
      border: 1px solid var(--border-subtle);
      transition: var(--transition-fast);
    }}

    .icon-btn:hover {{
      background: var(--bg-elevated);
      color: var(--text-primary);
      border-color: var(--border-medium);
    }}

    /* Subject Pills Bar */
    .subject-bar {{
      height: 48px;
      background: var(--bg-subtle);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      padding: 0 20px;
      gap: 8px;
      overflow-x: auto;
      flex-shrink: 0;
    }}

    .subject-pill {{
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 6px 12px;
      border-radius: var(--radius-full);
      font-size: 13px;
      font-weight: 600;
      color: var(--text-secondary);
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      white-space: nowrap;
      transition: var(--transition-fast);
    }}

    .subject-pill:hover {{
      color: var(--text-primary);
      border-color: var(--border-medium);
      background: var(--bg-elevated);
    }}

    .subject-pill.active {{
      background: var(--accent-indigo);
      color: white;
      border-color: var(--accent-indigo);
      box-shadow: 0 2px 10px rgba(99, 102, 241, 0.35);
    }}

    .pill-count {{
      font-size: 11px;
      font-family: var(--font-mono);
      opacity: 0.8;
      background: rgba(0, 0, 0, 0.2);
      padding: 1px 6px;
      border-radius: var(--radius-full);
    }}

    /* Body Layout */
    .main-container {{
      display: flex;
      flex: 1;
      height: calc(100vh - var(--header-height) - 48px);
      overflow: hidden;
      position: relative;
    }}

    /* Left Sidebar */
    .sidebar {{
      width: var(--sidebar-width);
      background: var(--bg-surface);
      border-right: 1px solid var(--border-subtle);
      display: flex;
      flex-direction: column;
      overflow-y: auto;
      flex-shrink: 0;
      user-select: none;
    }}

    .sidebar-section {{
      padding: 16px;
      border-bottom: 1px solid var(--border-subtle);
    }}

    .sidebar-title {{
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-muted);
      font-weight: 700;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .nav-item {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 8px 10px;
      border-radius: var(--radius-sm);
      font-size: 13px;
      font-weight: 500;
      color: var(--text-secondary);
      margin-bottom: 2px;
      transition: var(--transition-fast);
      cursor: pointer;
    }}

    .nav-item:hover {{
      background: var(--bg-hover);
      color: var(--text-primary);
    }}

    .nav-item.active {{
      background: var(--accent-indigo-soft);
      color: var(--accent-indigo);
      font-weight: 600;
    }}

    .nav-item-left {{
      display: flex;
      align-items: center;
      gap: 10px;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }}

    .nav-icon {{
      font-size: 15px;
      flex-shrink: 0;
    }}

    .nav-badge {{
      font-size: 11px;
      font-family: var(--font-mono);
      color: var(--text-muted);
      background: var(--bg-elevated);
      padding: 1px 6px;
      border-radius: var(--radius-full);
      flex-shrink: 0;
    }}

    /* Filter Chips in Sidebar */
    .chip-group {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }}

    .chip {{
      padding: 4px 9px;
      border-radius: var(--radius-sm);
      font-size: 12px;
      font-weight: 500;
      background: var(--bg-elevated);
      color: var(--text-secondary);
      border: 1px solid var(--border-subtle);
      transition: var(--transition-fast);
      cursor: pointer;
    }}

    .chip:hover {{
      border-color: var(--border-medium);
      color: var(--text-primary);
    }}

    .chip.active {{
      background: var(--text-primary);
      color: var(--text-inverse);
      font-weight: 600;
      border-color: var(--text-primary);
    }}

    /* Main Content Stage */
    .content-stage {{
      flex: 1;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      background: var(--bg-canvas);
    }}

    /* Stage Toolbar */
    .stage-toolbar {{
      height: 52px;
      padding: 0 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--border-subtle);
      background: var(--bg-subtle);
      gap: 16px;
      flex-shrink: 0;
    }}

    .toolbar-left {{
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 13px;
      color: var(--text-secondary);
    }}

    .active-filter-badge {{
      font-size: 12px;
      font-weight: 600;
      padding: 3px 10px;
      background: var(--bg-surface);
      border: 1px solid var(--border-medium);
      border-radius: var(--radius-full);
      color: var(--text-primary);
    }}

    .toolbar-right {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .select-dropdown {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 6px 12px;
      font-size: 13px;
      color: var(--text-primary);
      outline: none;
      cursor: pointer;
    }}

    .toggle-switch-label {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 12px;
      font-weight: 600;
      color: var(--text-secondary);
      cursor: pointer;
      user-select: none;
    }}

    .toggle-checkbox {{
      accent-color: var(--accent-indigo);
      width: 16px;
      height: 16px;
      cursor: pointer;
    }}

    /* Stage Scroll Area */
    .stage-scroll {{
      flex: 1;
      overflow-y: auto;
      padding: 24px;
    }}

    /* Materials Grid */
    .materials-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 16px;
    }}

    /* Card Item */
    .card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 18px;
      display: flex;
      flex-direction: column;
      gap: 14px;
      transition: var(--transition-fast);
      position: relative;
    }}

    .card:hover {{
      border-color: var(--border-medium);
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
      background: var(--bg-elevated);
    }}

    .card.paired {{
      border-left: 3px solid var(--accent-emerald);
    }}

    .card-top {{
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 10px;
    }}

    .card-tags {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }}

    .tag {{
      font-size: 11px;
      font-weight: 600;
      padding: 2px 7px;
      border-radius: var(--radius-sm);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}

    .tag-subject-math {{ background: rgba(59, 130, 246, 0.15); color: #60a5fa; }}
    .tag-subject-science {{ background: rgba(16, 185, 129, 0.15); color: #34d399; }}
    .tag-subject-sst {{ background: rgba(245, 158, 11, 0.15); color: #fbbf24; }}
    .tag-subject-english {{ background: rgba(139, 92, 246, 0.15); color: #a78bfa; }}
    .tag-subject-hindi {{ background: rgba(244, 63, 94, 0.15); color: #fb7185; }}
    .tag-subject-it {{ background: rgba(6, 182, 212, 0.15); color: #22d3ee; }}
    .tag-subject-general {{ background: rgba(148, 163, 184, 0.15); color: #94a3b8; }}

    .tag-year {{
      background: var(--bg-subtle);
      color: var(--text-muted);
      border: 1px solid var(--border-subtle);
      font-family: var(--font-mono);
    }}

    .tag-type {{
      background: var(--bg-subtle);
      color: var(--text-secondary);
      border: 1px solid var(--border-subtle);
    }}

    .card-title {{
      font-size: 14px;
      font-weight: 600;
      color: var(--text-primary);
      line-height: 1.4;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }}

    .card-meta {{
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 12px;
      color: var(--text-muted);
      font-family: var(--font-mono);
    }}

    .card-actions {{
      margin-top: auto;
      display: flex;
      align-items: center;
      gap: 8px;
      padding-top: 10px;
      border-top: 1px solid var(--border-subtle);
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 7px 12px;
      border-radius: var(--radius-sm);
      font-size: 12px;
      font-weight: 600;
      transition: var(--transition-fast);
      cursor: pointer;
    }}

    .btn-primary {{
      background: var(--accent-indigo);
      color: white;
    }}

    .btn-primary:hover {{
      background: #4f46e5;
      box-shadow: 0 2px 8px rgba(99, 102, 241, 0.35);
    }}

    .btn-split {{
      background: linear-gradient(135deg, #10b981, #06b6d4);
      color: white;
      font-weight: 700;
    }}

    .btn-split:hover {{
      filter: brightness(1.1);
      box-shadow: 0 2px 10px rgba(16, 185, 129, 0.35);
    }}

    .btn-secondary {{
      background: var(--bg-elevated);
      color: var(--text-secondary);
      border: 1px solid var(--border-subtle);
    }}

    .btn-secondary:hover {{
      background: var(--bg-hover);
      color: var(--text-primary);
      border-color: var(--border-medium);
    }}

    /* Table View Layout */
    .materials-table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 13px;
    }}

    .materials-table th {{
      background: var(--bg-subtle);
      padding: 10px 14px;
      font-weight: 600;
      color: var(--text-muted);
      border-bottom: 1px solid var(--border-subtle);
    }}

    .materials-table td {{
      padding: 12px 14px;
      border-bottom: 1px solid var(--border-subtle);
      color: var(--text-secondary);
    }}

    .materials-table tr:hover td {{
      background: var(--bg-hover);
      color: var(--text-primary);
    }}

    /* ============================================================
       DUAL-PANE SPLIT WORKBENCH (THE STANDOUT HERO FEATURE)
       ============================================================ */
    .split-workbench {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: var(--bg-canvas);
      z-index: 100;
      display: none;
      flex-direction: column;
      animation: fadeIn 200ms ease;
    }}

    .split-workbench.active {{
      display: flex;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: scale(0.99); }}
      to {{ opacity: 1; transform: scale(1); }}
    }}

    .workbench-header {{
      height: 56px;
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 16px;
      gap: 16px;
      flex-shrink: 0;
    }}

    .workbench-titles {{
      display: flex;
      align-items: center;
      gap: 12px;
      flex: 1;
      overflow: hidden;
    }}

    .doc-pill {{
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 4px 10px;
      background: var(--bg-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      font-size: 12px;
      font-weight: 600;
      color: var(--text-primary);
      max-width: 45%;
      overflow: hidden;
      white-space: nowrap;
      text-overflow: ellipsis;
    }}

    .doc-pill.left {{ border-left: 3px solid var(--accent-indigo); }}
    .doc-pill.right {{ border-left: 3px solid var(--accent-emerald); }}

    .workbench-controls {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .workbench-body {{
      flex: 1;
      display: flex;
      overflow: hidden;
      position: relative;
    }}

    .workbench-pane {{
      flex: 1;
      height: 100%;
      background: #1e1e24;
      display: flex;
      flex-direction: column;
      position: relative;
      overflow: hidden;
      transition: width var(--transition-fast);
    }}

    .workbench-pane iframe {{
      width: 100%;
      height: 100%;
      border: none;
      background: white;
    }}

    .pane-divider {{
      width: 6px;
      background: var(--border-subtle);
      cursor: col-resize;
      transition: background var(--transition-fast);
    }}

    .pane-divider:hover {{
      background: var(--accent-indigo);
    }}

    /* Pane Top Bar */
    .pane-bar {{
      height: 38px;
      background: var(--bg-elevated);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 12px;
      font-size: 12px;
      font-weight: 600;
      color: var(--text-secondary);
    }}

    /* Companion Document Selector Dropdown */
    .companion-select {{
      background: var(--bg-surface);
      border: 1px solid var(--border-medium);
      border-radius: var(--radius-sm);
      color: var(--text-primary);
      font-size: 11px;
      font-weight: 600;
      padding: 3px 8px;
      outline: none;
      cursor: pointer;
    }}

    /* ============================================================
       OMNI-SEARCH MODAL (Ctrl + K)
       ============================================================ */
    .search-modal-backdrop {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(0, 0, 0, 0.7);
      backdrop-filter: blur(8px);
      z-index: 150;
      display: none;
      align-items: flex-start;
      justify-content: center;
      padding-top: 100px;
    }}

    .search-modal-backdrop.active {{
      display: flex;
    }}

    .search-modal {{
      width: 640px;
      max-width: 90vw;
      background: var(--bg-surface);
      border: 1px solid var(--border-medium);
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-lg);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      animation: modalSlide 180ms ease;
    }}

    @keyframes modalSlide {{
      from {{ transform: translateY(-16px); opacity: 0; }}
      to {{ transform: translateY(0); opacity: 1; }}
    }}

    .search-input-box {{
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 16px 20px;
      border-bottom: 1px solid var(--border-subtle);
    }}

    .search-input-box input {{
      flex: 1;
      font-size: 16px;
      font-weight: 500;
      color: var(--text-primary);
      outline: none;
    }}

    .search-results-list {{
      max-height: 400px;
      overflow-y: auto;
      padding: 10px;
    }}

    .search-result-item {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 10px 14px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      transition: var(--transition-fast);
      gap: 12px;
    }}

    .search-result-item:hover, .search-result-item.highlighted {{
      background: var(--bg-hover);
    }}

    .search-footer {{
      padding: 10px 20px;
      background: var(--bg-subtle);
      border-top: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 11px;
      color: var(--text-muted);
    }}

    /* ============================================================
       MAP WORK INTERACTIVE GUIDE MODAL
       ============================================================ */
    .map-modal-backdrop {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(8px);
      z-index: 140;
      display: none;
      align-items: center;
      justify-content: center;
    }}

    .map-modal-backdrop.active {{
      display: flex;
    }}

    .map-modal {{
      width: 900px;
      max-width: 94vw;
      height: 85vh;
      background: var(--bg-surface);
      border: 1px solid var(--border-medium);
      border-radius: var(--radius-lg);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      box-shadow: var(--shadow-lg);
    }}

    .map-header {{
      padding: 16px 24px;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: var(--bg-subtle);
    }}

    .map-content {{
      flex: 1;
      overflow-y: auto;
      padding: 24px;
      line-height: 1.6;
    }}

    .map-content h2 {{
      color: var(--accent-amber);
      font-size: 18px;
      margin: 20px 0 10px 0;
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 6px;
    }}

    .map-content h3 {{
      color: var(--text-primary);
      font-size: 15px;
      margin: 16px 0 8px 0;
    }}

    .map-content table {{
      width: 100%;
      border-collapse: collapse;
      margin: 12px 0 20px 0;
      font-size: 13px;
    }}

    .map-content th, .map-content td {{
      padding: 8px 12px;
      border: 1px solid var(--border-subtle);
      text-align: left;
    }}

    .map-content th {{
      background: var(--bg-subtle);
      color: var(--text-muted);
    }}

    .map-content ul, .map-content ol {{
      margin-left: 24px;
      margin-bottom: 16px;
    }}

    .map-content li {{
      margin-bottom: 6px;
    }}

    /* Scrollbars */
    ::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    ::-webkit-scrollbar-track {{ background: transparent; }}
    ::-webkit-scrollbar-thumb {{
      background: var(--border-medium);
      border-radius: 999px;
    }}
  </style>
</head>
<body>
  <div class="app-root">
    <!-- Top Header -->
    <header class="header">
      <div class="header-left">
        <div class="brand">
          <div class="brand-icon">⚡</div>
          <span>CBSE Command Center</span>
          <span class="brand-badge">Class 10 Vault</span>
        </div>

        <button class="omni-search-btn" id="openOmniSearch">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          <span>Search 896 documents, sets, years...</span>
          <span class="search-key-badge">Ctrl K</span>
        </button>
      </div>

      <div class="header-right">
        <div class="stats-pill">
          <span class="stats-dot"></span>
          <span id="headerStatsText">896 Verified Resources</span>
        </div>

        <button class="btn btn-secondary" id="openMapWorkBtn" title="CBSE Class 10 Social Science Map Work Guide">
          🗺️ Map Work Guide
        </button>

        <button class="icon-btn" id="themeToggleBtn" title="Toggle Theme (Dark / Light)">
          <span id="themeIcon">☀️</span>
        </button>
      </div>
    </header>

    <!-- Subject Selector Bar -->
    <div class="subject-bar" id="subjectBar">
      <button class="subject-pill active" data-subject="All">
        <span>✨ All Subjects</span>
        <span class="pill-count" id="countAll">896</span>
      </button>
      <button class="subject-pill" data-subject="Mathematics">
        <span>📐 Mathematics (Standard)</span>
        <span class="pill-count" id="countMath">172</span>
      </button>
      <button class="subject-pill" data-subject="Science">
        <span>🔬 Science</span>
        <span class="pill-count" id="countScience">164</span>
      </button>
      <button class="subject-pill" data-subject="Social Science">
        <span>🌍 Social Science</span>
        <span class="pill-count" id="countSST">220</span>
      </button>
      <button class="subject-pill" data-subject="English">
        <span>📖 English (L&L)</span>
        <span class="pill-count" id="countEnglish">147</span>
      </button>
      <button class="subject-pill" data-subject="Hindi">
        <span>🖋️ Hindi (Course A)</span>
        <span class="pill-count" id="countHindi">132</span>
      </button>
      <button class="subject-pill" data-subject="Information Technology">
        <span>💻 IT 402</span>
        <span class="pill-count" id="countIT">56</span>
      </button>
    </div>

    <!-- Main Workspace -->
    <div class="main-container">
      <!-- Left Category Sidebar -->
      <aside class="sidebar">
        <div class="sidebar-section">
          <div class="sidebar-title">Categories</div>
          <div id="categoryNavList">
            <!-- Dynamically populated -->
          </div>
        </div>

        <div class="sidebar-section">
          <div class="sidebar-title">Exam Year</div>
          <div class="chip-group" id="yearChipGroup">
            <button class="chip active" data-year="All">All</button>
            <button class="chip" data-year="2027">2027 SQP</button>
            <button class="chip" data-year="2026">2026</button>
            <button class="chip" data-year="2025">2025</button>
            <button class="chip" data-year="2024">2024</button>
            <button class="chip" data-year="2023">2023</button>
            <button class="chip" data-year="2022">2022</button>
            <button class="chip" data-year="2021-22">2021-22</button>
          </div>
        </div>

        <div class="sidebar-section">
          <div class="sidebar-title">Document Type</div>
          <div class="chip-group" id="typeChipGroup">
            <button class="chip active" data-type="All">All</button>
            <button class="chip" data-type="question_paper">Board Papers</button>
            <button class="chip" data-type="sample_paper">Sample Papers</button>
            <button class="chip" data-type="marking_scheme">Marking Schemes</button>
            <button class="chip" data-type="topper_script">Toppers</button>
            <button class="chip" data-type="textbook_chapter">Textbooks</button>
            <button class="chip" data-type="exemplar_chapter">Exemplar</button>
            <button class="chip" data-type="lab_manual">Practicals</button>
            <button class="chip" data-type="syllabus">Syllabus</button>
          </div>
        </div>
      </aside>

      <!-- Main Stage -->
      <main class="content-stage">
        <!-- Toolbar -->
        <div class="stage-toolbar">
          <div class="toolbar-left">
            <span id="activeFilterSummary">Showing all items</span>
            <span class="active-filter-badge" id="resultsCountBadge">896 items</span>
          </div>

          <div class="toolbar-right">
            <label class="toggle-switch-label" title="Only display items with paired Question Paper + Marking Scheme">
              <input type="checkbox" id="pairedOnlyToggle" class="toggle-checkbox" />
              <span>⚡ Paired Only (Split View)</span>
            </label>

            <select class="select-dropdown" id="sortSelect">
              <option value="year_desc">Year (Newest first)</option>
              <option value="year_asc">Year (Oldest first)</option>
              <option value="title_asc">Title (A to Z)</option>
              <option value="size_desc">File Size (Largest)</option>
            </select>

            <button class="icon-btn" id="viewModeToggle" title="Toggle Grid / Table view">
              <span id="viewModeIcon">⊞</span>
            </button>
          </div>
        </div>

        <!-- Scrollable Stage Area -->
        <div class="stage-scroll" id="stageScrollArea">
          <div class="materials-grid" id="materialsGrid">
            <!-- Dynamically populated cards -->
          </div>
          <table class="materials-table" id="materialsTable" style="display: none;">
            <thead>
              <tr>
                <th>Title & Series</th>
                <th>Subject</th>
                <th>Category</th>
                <th>Year</th>
                <th>Size</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody id="materialsTableBody">
              <!-- Dynamically populated rows -->
            </tbody>
          </table>
        </div>
      </main>
    </div>
  </div>

  <!-- ============================================================
       DUAL-PANE SPLIT WORKBENCH
       ============================================================ -->
  <div class="split-workbench" id="splitWorkbench">
    <div class="workbench-header">
      <div class="workbench-titles">
        <div class="doc-pill left" id="leftDocPill">
          <span>📄</span>
          <span id="leftDocTitle">Question Paper</span>
        </div>
        <div class="doc-pill right" id="rightDocPill">
          <span>🎯</span>
          <span id="rightDocTitle">Official Marking Scheme</span>
        </div>
      </div>

      <div class="workbench-controls">
        <select class="companion-select" id="companionSelector" title="Switch Right Pane Document">
          <option value="paired">Paired Marking Scheme / Solution</option>
          <option value="topper_2025">Topper Answer Script 2025</option>
          <option value="topper_2024">Topper Answer Script 2024</option>
          <option value="topper_2023">Topper Answer Script 2023</option>
          <option value="topper_2022">Topper Answer Script 2022</option>
        </select>

        <button class="btn btn-secondary" id="swapPanesBtn" title="Swap Left and Right Panes">⇄ Swap</button>
        <button class="btn btn-secondary" id="splitPreset50" title="50/50 Split View">50 / 50</button>
        <button class="btn btn-secondary" id="splitPresetLeft" title="Focus Left Pane">Left Focus</button>
        <button class="btn btn-secondary" id="splitPresetRight" title="Focus Right Pane">Right Focus</button>
        <button class="btn btn-secondary" id="popoutBtn" title="Open in dedicated browser tab">↗ Pop Out</button>
        <button class="btn btn-primary" id="closeWorkbenchBtn" title="Close Split Workbench (ESC)">✕ Close</button>
      </div>
    </div>

    <div class="workbench-body" id="workbenchBody">
      <div class="workbench-pane" id="leftPane">
        <div class="pane-bar">
          <span id="leftPaneLabel">Primary Document</span>
          <a href="#" id="leftDownloadLink" target="_blank" class="btn btn-secondary" style="padding: 2px 8px; font-size: 11px;">⬇ Download</a>
        </div>
        <iframe id="leftIframe" src="about:blank"></iframe>
      </div>

      <div class="pane-divider" id="paneDivider"></div>

      <div class="workbench-pane" id="rightPane">
        <div class="pane-bar">
          <span id="rightPaneLabel">Solution / Marking Scheme</span>
          <a href="#" id="rightDownloadLink" target="_blank" class="btn btn-secondary" style="padding: 2px 8px; font-size: 11px;">⬇ Download</a>
        </div>
        <iframe id="rightIframe" src="about:blank"></iframe>
      </div>
    </div>
  </div>

  <!-- ============================================================
       OMNI-SEARCH MODAL (Ctrl + K)
       ============================================================ -->
  <div class="search-modal-backdrop" id="searchModal">
    <div class="search-modal">
      <div class="search-input-box">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
        <input type="text" id="omniSearchInput" placeholder="Search across all 896 CBSE materials (type e.g. 30-1-1, SQP 2027, Topper Science)..." autofocus />
      </div>
      <div class="search-results-list" id="searchResultsList">
        <!-- Results rendered here -->
      </div>
      <div class="search-footer">
        <span>Press <kbd>↑</kbd> <kbd>↓</kbd> to navigate, <kbd>Enter</kbd> to preview, <kbd>ESC</kbd> to close</span>
        <span id="omniMatchCount">0 matches</span>
      </div>
    </div>
  </div>

  <!-- ============================================================
       MAP WORK GUIDE MODAL
       ============================================================ -->
  <div class="map-modal-backdrop" id="mapModal">
    <div class="map-modal">
      <div class="map-header">
        <div style="font-weight: 700; font-size: 16px;">🗺️ CBSE Class 10 Social Science — Complete Map Work Guide (5 Marks Guaranteed)</div>
        <button class="btn btn-secondary" id="closeMapModalBtn">✕ Close</button>
      </div>
      <div class="map-content" id="mapContentArea">
        <!-- Markdown parsed dynamically -->
      </div>
    </div>
  </div>

  <!-- Embedded Complete Dataset for Offline / Local File:// Compatibility -->
  <script>
    window.__CBSE_DATA__ = {data_json_str};
    window.__MAP_GUIDE_MD__ = {map_guide_json_str};
  </script>

  <!-- Application Logic -->
  <script>
    (function() {{
      const state = {{
        allMaterials: window.__CBSE_DATA__.materials || [],
        selectedSubject: 'All',
        selectedCategory: 'All',
        selectedYear: 'All',
        selectedType: 'All',
        pairedOnly: false,
        searchQuery: '',
        sortBy: 'year_desc',
        viewMode: 'grid', // 'grid' or 'table'
        theme: localStorage.getItem('cbse_theme') || 'dark',

        // Workbench state
        activeLeftItem: null,
        activeRightItem: null,
        splitMode: '50-50'
      }};

      // Category definitions with icons
      const categoryMetadata = [
        {{ id: 'All', name: 'All Categories', icon: '📂' }},
        {{ id: 'Board Examination Papers', name: 'Board Papers (2022-24)', icon: '📜' }},
        {{ id: 'Sample Question Papers', name: 'Sample Papers (2023-27)', icon: '📝' }},
        {{ id: 'Topper Model Answers', name: 'Topper Answer Scripts', icon: '🏆' }},
        {{ id: 'Books and Study Material', name: 'Textbooks & Books', icon: '📖' }},
        {{ id: 'NCERT Exemplar', name: 'NCERT Exemplar', icon: '💡' }},
        {{ id: 'Additional Practice Questions', name: 'Additional Practice', icon: '✍️' }},
        {{ id: 'Laboratory Manuals', name: 'Lab Manuals (Practicals)', icon: '🧪' }},
        {{ id: 'Question Banks and Competency', name: 'Question Banks', icon: '🎯' }},
        {{ id: 'Syllabus and Curriculum 2027', name: 'Syllabus 2026-27', icon: '📋' }}
      ];

      // Cache DOM
      const dom = {{
        categoryNavList: document.getElementById('categoryNavList'),
        materialsGrid: document.getElementById('materialsGrid'),
        materialsTable: document.getElementById('materialsTable'),
        materialsTableBody: document.getElementById('materialsTableBody'),
        subjectBar: document.getElementById('subjectBar'),
        yearChipGroup: document.getElementById('yearChipGroup'),
        typeChipGroup: document.getElementById('typeChipGroup'),
        pairedOnlyToggle: document.getElementById('pairedOnlyToggle'),
        sortSelect: document.getElementById('sortSelect'),
        viewModeToggle: document.getElementById('viewModeToggle'),
        viewModeIcon: document.getElementById('viewModeIcon'),
        resultsCountBadge: document.getElementById('resultsCountBadge'),
        activeFilterSummary: document.getElementById('activeFilterSummary'),
        themeToggleBtn: document.getElementById('themeToggleBtn'),
        themeIcon: document.getElementById('themeIcon'),
        
        // Workbench
        splitWorkbench: document.getElementById('splitWorkbench'),
        closeWorkbenchBtn: document.getElementById('closeWorkbenchBtn'),
        leftDocTitle: document.getElementById('leftDocTitle'),
        rightDocTitle: document.getElementById('rightDocTitle'),
        leftIframe: document.getElementById('leftIframe'),
        rightIframe: document.getElementById('rightIframe'),
        leftDownloadLink: document.getElementById('leftDownloadLink'),
        rightDownloadLink: document.getElementById('rightDownloadLink'),
        swapPanesBtn: document.getElementById('swapPanesBtn'),
        splitPreset50: document.getElementById('splitPreset50'),
        splitPresetLeft: document.getElementById('splitPresetLeft'),
        splitPresetRight: document.getElementById('splitPresetRight'),
        popoutBtn: document.getElementById('popoutBtn'),
        companionSelector: document.getElementById('companionSelector'),
        leftPane: document.getElementById('leftPane'),
        rightPane: document.getElementById('rightPane'),

        // Omni Search
        openOmniSearch: document.getElementById('openOmniSearch'),
        searchModal: document.getElementById('searchModal'),
        omniSearchInput: document.getElementById('omniSearchInput'),
        searchResultsList: document.getElementById('searchResultsList'),
        omniMatchCount: document.getElementById('omniMatchCount'),

        // Map Work
        openMapWorkBtn: document.getElementById('openMapWorkBtn'),
        mapModal: document.getElementById('mapModal'),
        closeMapModalBtn: document.getElementById('closeMapModalBtn'),
        mapContentArea: document.getElementById('mapContentArea')
      }};

      // Theme initialization
      function applyTheme(theme) {{
        document.documentElement.setAttribute('data-theme', theme);
        dom.themeIcon.textContent = theme === 'dark' ? '☀️' : '🌙';
        localStorage.setItem('cbse_theme', theme);
        state.theme = theme;
      }}
      applyTheme(state.theme);

      dom.themeToggleBtn.addEventListener('click', () => {{
        applyTheme(state.theme === 'dark' ? 'light' : 'dark');
      }});

      // Build Sidebar Category List
      function renderCategoryNav() {{
        dom.categoryNavList.innerHTML = '';
        categoryMetadata.forEach(cat => {{
          const count = cat.id === 'All' 
            ? state.allMaterials.length 
            : state.allMaterials.filter(m => m.category === cat.id).length;

          const div = document.createElement('div');
          div.className = `nav-item ${{state.selectedCategory === cat.id ? 'active' : ''}}`;
          div.innerHTML = `
            <div class="nav-item-left">
              <span class="nav-icon">${{cat.icon}}</span>
              <span>${{cat.name}}</span>
            </div>
            <span class="nav-badge">${{count}}</span>
          `;
          div.addEventListener('click', () => {{
            state.selectedCategory = cat.id;
            renderCategoryNav();
            renderMaterials();
          }});
          dom.categoryNavList.appendChild(div);
        }});
      }}

      // Filter Logic
      function getFilteredMaterials() {{
        return state.allMaterials.filter(m => {{
          // Exclude raw bundle zips or covers from direct list if desired, or keep all
          if (m.type === 'cover_image') return false;

          if (state.selectedSubject !== 'All' && m.subject !== state.selectedSubject) return false;
          if (state.selectedCategory !== 'All' && m.category !== state.selectedCategory) return false;
          if (state.selectedYear !== 'All' && m.year !== state.selectedYear) return false;
          if (state.selectedType !== 'All' && m.type !== state.selectedType) return false;
          if (state.pairedOnly && !m.paired_id) return false;

          if (state.searchQuery) {{
            const q = state.searchQuery.toLowerCase();
            const match = m.title.toLowerCase().includes(q) ||
                          m.filename.toLowerCase().includes(q) ||
                          (m.set_code && m.set_code.toLowerCase().includes(q)) ||
                          m.subject.toLowerCase().includes(q);
            if (!match) return false;
          }}
          return true;
        }}).sort((a, b) => {{
          if (state.sortBy === 'year_desc') return (b.year || '0').localeCompare(a.year || '0');
          if (state.sortBy === 'year_asc') return (a.year || '0').localeCompare(b.year || '0');
          if (state.sortBy === 'title_asc') return a.title.localeCompare(b.title);
          if (state.sortBy === 'size_desc') return b.size_bytes - a.size_bytes;
          return 0;
        }});
      }}

      // Subject tag class mapping
      function getSubjectTagClass(subj) {{
        const map = {{
          'Mathematics': 'tag-subject-math',
          'Science': 'tag-subject-science',
          'Social Science': 'tag-subject-sst',
          'English': 'tag-subject-english',
          'Hindi': 'tag-subject-hindi',
          'Information Technology': 'tag-subject-it'
        }};
        return map[subj] || 'tag-subject-general';
      }}

      function getCleanTypeLabel(type) {{
        const map = {{
          'question_paper': 'Question Paper',
          'marking_scheme': 'Marking Scheme',
          'sample_paper': 'Sample Paper',
          'topper_script': 'Topper Script',
          'textbook_chapter': 'Textbook Chapter',
          'exemplar_chapter': 'Exemplar Problem',
          'exemplar_solution': 'Exemplar Solution',
          'lab_manual': 'Practical Manual',
          'question_bank': 'Question Bank',
          'framework': 'Competency Framework',
          'syllabus': 'Curriculum'
        }};
        return map[type] || 'Document';
      }}

      // Render Materials Grid and Table
      function renderMaterials() {{
        const items = getFilteredMaterials();
        dom.resultsCountBadge.textContent = `${{items.length}} items`;

        // Update active summary text
        const subjText = state.selectedSubject === 'All' ? 'All Subjects' : state.selectedSubject;
        const catText = state.selectedCategory === 'All' ? 'All Categories' : state.selectedCategory;
        const yearText = state.selectedYear === 'All' ? '' : ` • ${{state.selectedYear}}`;
        dom.activeFilterSummary.textContent = `${{subjText}} / ${{catText}}${{yearText}}`;

        if (state.viewMode === 'grid') {{
          dom.materialsGrid.style.display = 'grid';
          dom.materialsTable.style.display = 'none';
          dom.materialsGrid.innerHTML = '';

          if (items.length === 0) {{
            dom.materialsGrid.innerHTML = `
              <div style="grid-column: 1/-1; text-align: center; padding: 60px 20px; color: var(--text-muted);">
                <div style="font-size: 32px; margin-bottom: 12px;">🔍</div>
                <div style="font-size: 16px; font-weight: 600; color: var(--text-secondary);">No documents match your filters</div>
                <div style="font-size: 13px; margin-top: 6px;">Try clearing some filters or searching for different keywords</div>
              </div>
            `;
            return;
          }}

          items.forEach(item => {{
            const card = document.createElement('div');
            card.className = `card ${{item.paired_id ? 'paired' : ''}}`;

            const hasPair = !!item.paired_id;
            const splitBtnHtml = hasPair 
              ? `<button class="btn btn-split open-split-btn" data-id="${{item.id}}">⚡ Split View (QP + MS)</button>` 
              : '';

            card.innerHTML = `
              <div class="card-top">
                <div class="card-tags">
                  <span class="tag ${{getSubjectTagClass(item.subject)}}">${{item.subject}}</span>
                  ${{item.year ? `<span class="tag tag-year">${{item.year}}</span>` : ''}}
                  ${{item.set_code ? `<span class="tag tag-year">${{item.set_code}}</span>` : ''}}
                  <span class="tag tag-type">${{getCleanTypeLabel(item.type)}}</span>
                </div>
              </div>

              <div class="card-title" title="${{item.title}}">${{item.title}}</div>

              <div class="card-meta">
                <span>📦 ${{item.size_formatted}}</span>
                ${{hasPair ? `<span style="color: var(--accent-emerald);">✔ Paired with Solution</span>` : ''}}
              </div>

              <div class="card-actions">
                ${{splitBtnHtml}}
                <button class="btn btn-primary open-single-btn" data-id="${{item.id}}">👁️ View</button>
                <a href="${{item.rel_path}}" target="_blank" download class="btn btn-secondary">⬇</a>
              </div>
            `;

            dom.materialsGrid.appendChild(card);
          }});
        }} else {{
          dom.materialsGrid.style.display = 'none';
          dom.materialsTable.style.display = 'table';
          dom.materialsTableBody.innerHTML = '';

          items.forEach(item => {{
            const tr = document.createElement('tr');
            tr.innerHTML = `
              <td>
                <div style="font-weight: 600; color: var(--text-primary);">${{item.title}}</div>
                <div style="font-size: 11px; color: var(--text-muted); font-family: var(--font-mono);">${{item.filename}}</div>
              </td>
              <td><span class="tag ${{getSubjectTagClass(item.subject)}}">${{item.subject}}</span></td>
              <td>${{item.category}}</td>
              <td>${{item.year || '-'}}</td>
              <td style="font-family: var(--font-mono);">${{item.size_formatted}}</td>
              <td>
                <div style="display: flex; gap: 6px;">
                  ${{item.paired_id ? `<button class="btn btn-split open-split-btn" data-id="${{item.id}}" style="padding: 4px 8px; font-size: 11px;">⚡ Split</button>` : ''}}
                  <button class="btn btn-primary open-single-btn" data-id="${{item.id}}" style="padding: 4px 8px; font-size: 11px;">View</button>
                  <a href="${{item.rel_path}}" target="_blank" download class="btn btn-secondary" style="padding: 4px 8px; font-size: 11px;">⬇</a>
                </div>
              </td>
            `;
            dom.materialsTableBody.appendChild(tr);
          }});
        }}

        // Attach Card Button Listeners
        document.querySelectorAll('.open-split-btn').forEach(b => {{
          b.addEventListener('click', (e) => {{
            const id = e.currentTarget.getAttribute('data-id');
            openWorkbench(id, true);
          }});
        }});

        document.querySelectorAll('.open-single-btn').forEach(b => {{
          b.addEventListener('click', (e) => {{
            const id = e.currentTarget.getAttribute('data-id');
            openWorkbench(id, false);
          }});
        }});
      }}

      // ============================================================
      // DUAL-PANE SPLIT WORKBENCH LOGIC
      // ============================================================
      function openWorkbench(itemId, isSplit) {{
        const primary = state.allMaterials.find(m => m.id === itemId);
        if (!primary) return;

        state.activeLeftItem = primary;
        dom.leftDocTitle.textContent = primary.title;
        dom.leftIframe.src = primary.rel_path;
        dom.leftDownloadLink.href = primary.rel_path;

        // Populate companion dropdown with matching Topper copies or paired schemes
        populateCompanionDropdown(primary);

        if (isSplit && primary.paired_id) {{
          const paired = state.allMaterials.find(m => m.id === primary.paired_id);
          if (paired) {{
            state.activeRightItem = paired;
            dom.rightDocTitle.textContent = paired.title;
            dom.rightIframe.src = paired.rel_path;
            dom.rightDownloadLink.href = paired.rel_path;
            setSplitPreset('50-50');
          }}
        }} else {{
          // Default right pane to either paired, topper copy, or exemplar solution
          if (primary.paired_id) {{
            const paired = state.allMaterials.find(m => m.id === primary.paired_id);
            state.activeRightItem = paired;
            dom.rightDocTitle.textContent = paired.title;
            dom.rightIframe.src = paired.rel_path;
            dom.rightDownloadLink.href = paired.rel_path;
            setSplitPreset('50-50');
          }} else {{
            // Single document focus
            state.activeRightItem = null;
            setSplitPreset('left-focus');
          }}
        }}

        dom.splitWorkbench.classList.add('active');
      }}

      function populateCompanionDropdown(primary) {{
        dom.companionSelector.innerHTML = '';

        if (primary.paired_id) {{
          const opt = document.createElement('option');
          opt.value = primary.paired_id;
          opt.textContent = `🎯 Paired Solution: ${{primary.paired_title || 'Official Marking Scheme'}}`;
          dom.companionSelector.appendChild(opt);
        }}

        // Find topper scripts for this subject
        const toppers = state.allMaterials.filter(m => m.type === 'topper_script' && m.subject === primary.subject);
        toppers.forEach(t => {{
          const opt = document.createElement('option');
          opt.value = t.id;
          opt.textContent = `🏆 ${{t.title}}`;
          dom.companionSelector.appendChild(opt);
        }});

        // If exemplar, add exemplar solutions
        if (primary.category === 'NCERT Exemplar') {{
          const sol = state.allMaterials.find(m => m.type === 'exemplar_solution' && m.subject === primary.subject);
          if (sol) {{
            const opt = document.createElement('option');
            opt.value = sol.id;
            opt.textContent = `💡 ${{sol.title}}`;
            dom.companionSelector.appendChild(opt);
          }}
        }}

        if (dom.companionSelector.options.length === 0) {{
          const opt = document.createElement('option');
          opt.value = '';
          opt.textContent = 'No alternate companion documents';
          dom.companionSelector.appendChild(opt);
        }}
      }}

      dom.companionSelector.addEventListener('change', (e) => {{
        const targetId = e.target.value;
        if (!targetId) return;
        const targetDoc = state.allMaterials.find(m => m.id === targetId);
        if (targetDoc) {{
          state.activeRightItem = targetDoc;
          dom.rightDocTitle.textContent = targetDoc.title;
          dom.rightIframe.src = targetDoc.rel_path;
          dom.rightDownloadLink.href = targetDoc.rel_path;
          setSplitPreset('50-50');
        }}
      }});

      function closeWorkbench() {{
        dom.splitWorkbench.classList.remove('active');
        dom.leftIframe.src = 'about:blank';
        dom.rightIframe.src = 'about:blank';
      }}

      dom.closeWorkbenchBtn.addEventListener('click', closeWorkbench);

      // Split Presets
      function setSplitPreset(preset) {{
        state.splitMode = preset;
        if (preset === '50-50') {{
          dom.leftPane.style.width = '50%';
          dom.rightPane.style.width = '50%';
          dom.rightPane.style.display = 'flex';
          dom.leftPane.style.display = 'flex';
        }} else if (preset === 'left-focus') {{
          dom.leftPane.style.width = '100%';
          dom.rightPane.style.width = '0%';
          dom.rightPane.style.display = 'none';
          dom.leftPane.style.display = 'flex';
        }} else if (preset === 'right-focus') {{
          dom.leftPane.style.width = '0%';
          dom.rightPane.style.width = '100%';
          dom.leftPane.style.display = 'none';
          dom.rightPane.style.display = 'flex';
        }}
      }}

      dom.splitPreset50.addEventListener('click', () => setSplitPreset('50-50'));
      dom.splitPresetLeft.addEventListener('click', () => setSplitPreset('left-focus'));
      dom.splitPresetRight.addEventListener('click', () => setSplitPreset('right-focus'));

      dom.swapPanesBtn.addEventListener('click', () => {{
        if (!state.activeLeftItem || !state.activeRightItem) return;
        const temp = state.activeLeftItem;
        state.activeLeftItem = state.activeRightItem;
        state.activeRightItem = temp;

        dom.leftDocTitle.textContent = state.activeLeftItem.title;
        dom.leftIframe.src = state.activeLeftItem.rel_path;
        dom.leftDownloadLink.href = state.activeLeftItem.rel_path;

        dom.rightDocTitle.textContent = state.activeRightItem.title;
        dom.rightIframe.src = state.activeRightItem.rel_path;
        dom.rightDownloadLink.href = state.activeRightItem.rel_path;
      }});

      dom.popoutBtn.addEventListener('click', () => {{
        if (state.activeLeftItem) window.open(state.activeLeftItem.rel_path, '_blank');
        if (state.activeRightItem) window.open(state.activeRightItem.rel_path, '_blank');
      }});

      // ============================================================
      // OMNI-SEARCH MODAL (Ctrl + K)
      // ============================================================
      function openOmniSearch() {{
        dom.searchModal.classList.add('active');
        dom.omniSearchInput.value = '';
        renderOmniResults('');
        dom.omniSearchInput.focus();
      }}

      function closeOmniSearch() {{
        dom.searchModal.classList.remove('active');
      }}

      dom.openOmniSearch.addEventListener('click', openOmniSearch);

      function renderOmniResults(q) {{
        const query = q.toLowerCase().trim();
        const matches = state.allMaterials.filter(m => {{
          if (!query) return true;
          return m.title.toLowerCase().includes(query) ||
                 m.filename.toLowerCase().includes(query) ||
                 (m.set_code && m.set_code.toLowerCase().includes(query)) ||
                 m.subject.toLowerCase().includes(query) ||
                 (m.year && m.year.includes(query));
        }}).slice(0, 30);

        dom.omniMatchCount.textContent = `${{matches.length}} matches`;
        dom.searchResultsList.innerHTML = '';

        matches.forEach((m, idx) => {{
          const item = document.createElement('div');
          item.className = `search-result-item ${{idx === 0 ? 'highlighted' : ''}}`;
          item.innerHTML = `
            <div style="display: flex; align-items: center; gap: 10px; overflow: hidden;">
              <span class="tag ${{getSubjectTagClass(m.subject)}}">${{m.subject}}</span>
              <div style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">
                <div style="font-weight: 600; color: var(--text-primary); font-size: 13px;">${{m.title}}</div>
                <div style="font-size: 11px; color: var(--text-muted); font-family: var(--font-mono);">${{m.rel_path}}</div>
              </div>
            </div>
            <div style="display: flex; align-items: center; gap: 8px; flex-shrink: 0;">
              ${{m.paired_id ? `<span style="font-size: 11px; color: var(--accent-emerald); font-weight: 600;">⚡ Split Ready</span>` : ''}}
              <span class="tag tag-year">${{m.year || 'Doc'}}</span>
            </div>
          `;
          item.addEventListener('click', () => {{
            closeOmniSearch();
            openWorkbench(m.id, !!m.paired_id);
          }});
          dom.searchResultsList.appendChild(item);
        }});
      }}

      dom.omniSearchInput.addEventListener('input', (e) => {{
        renderOmniResults(e.target.value);
      }});

      // Global Keyboard Shortcuts
      window.addEventListener('keydown', (e) => {{
        if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {{
          e.preventDefault();
          if (dom.searchModal.classList.contains('active')) closeOmniSearch();
          else openOmniSearch();
        }}
        if (e.key === 'Escape') {{
          if (dom.searchModal.classList.contains('active')) closeOmniSearch();
          if (dom.splitWorkbench.classList.contains('active')) closeWorkbench();
          if (dom.mapModal.classList.contains('active')) dom.mapModal.classList.remove('active');
        }}
      }});

      dom.searchModal.addEventListener('click', (e) => {{
        if (e.target === dom.searchModal) closeOmniSearch();
      }});

      // ============================================================
      // MAP WORK MODAL RENDERING
      // ============================================================
      function parseMarkdownToHtml(md) {{
        // Basic clean parser for tables, headings, and lists
        let html = md
          .replace(/^### (.*$)/gim, '<h3>$1</h3>')
          .replace(/^## (.*$)/gim, '<h2>$1</h2>')
          .replace(/^# (.*$)/gim, '<h1>$1</h1>')
          .replace(/\\*\\*(.*?)\\*\\*/gim, '<strong>$1</strong>')
          .replace(/\\*(.*?)\\*/gim, '<em>$1</em>');

        // Parse tables
        const lines = html.split('\\n');
        let inTable = false;
        let tableHtml = '';
        let parsedLines = [];

        for (let i = 0; i < lines.length; i++) {{
          const line = lines[i].trim();
          if (line.startsWith('|') && line.endsWith('|')) {{
            if (!inTable) {{
              inTable = true;
              tableHtml = '<table><thead>';
            }}
            const cells = line.split('|').slice(1, -1).map(c => c.trim());
            if (line.includes('---')) {{
              tableHtml += '</thead><tbody>';
            }} else if (!tableHtml.includes('tbody')) {{
              tableHtml += '<tr>' + cells.map(c => `<th>${{c}}</th>`).join('') + '</tr>';
            }} else {{
              tableHtml += '<tr>' + cells.map(c => `<td>${{c}}</td>`).join('') + '</tr>';
            }}
          }} else {{
            if (inTable) {{
              inTable = false;
              tableHtml += '</tbody></table>';
              parsedLines.push(tableHtml);
              tableHtml = '';
            }}
            parsedLines.push(line);
          }}
        }}
        if (inTable) {{
          tableHtml += '</tbody></table>';
          parsedLines.push(tableHtml);
        }}

        return parsedLines.join('<br>');
      }}

      dom.openMapWorkBtn.addEventListener('click', () => {{
        dom.mapContentArea.innerHTML = parseMarkdownToHtml(window.__MAP_GUIDE_MD__);
        dom.mapModal.classList.add('active');
      }});

      dom.closeMapModalBtn.addEventListener('click', () => {{
        dom.mapModal.classList.remove('active');
      }});
      dom.mapModal.addEventListener('click', (e) => {{
        if (e.target === dom.mapModal) dom.mapModal.classList.remove('active');
      }});

      // ============================================================
      // EVENT LISTENERS & FILTER WIRING
      // ============================================================
      dom.subjectBar.addEventListener('click', (e) => {{
        const pill = e.target.closest('.subject-pill');
        if (!pill) return;
        document.querySelectorAll('.subject-pill').forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        state.selectedSubject = pill.getAttribute('data-subject');
        renderMaterials();
      }});

      dom.yearChipGroup.addEventListener('click', (e) => {{
        const chip = e.target.closest('.chip');
        if (!chip) return;
        dom.yearChipGroup.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        state.selectedYear = chip.getAttribute('data-year');
        renderMaterials();
      }});

      dom.typeChipGroup.addEventListener('click', (e) => {{
        const chip = e.target.closest('.chip');
        if (!chip) return;
        dom.typeChipGroup.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        state.selectedType = chip.getAttribute('data-type');
        renderMaterials();
      }});

      dom.pairedOnlyToggle.addEventListener('change', (e) => {{
        state.pairedOnly = e.target.checked;
        renderMaterials();
      }});

      dom.sortSelect.addEventListener('change', (e) => {{
        state.sortBy = e.target.value;
        renderMaterials();
      }});

      dom.viewModeToggle.addEventListener('click', () => {{
        state.viewMode = state.viewMode === 'grid' ? 'table' : 'grid';
        dom.viewModeIcon.textContent = state.viewMode === 'grid' ? '⊞' : '☰';
        renderMaterials();
      }});

      // Initial Bootstrap
      renderCategoryNav();
      renderMaterials();

    }})();
  </script>
</body>
</html>
"""

    targets = [
        os.path.join(SCRATCH_DIR, "index.html"),
        os.path.join(DEST_DIR, "index.html")
    ]

    for target in targets:
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Website successfully written to {target} ({len(html_content)} bytes)")

if __name__ == "__main__":
    build()

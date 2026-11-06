import os
import json
import re

INDEX_JSON_PATH = r"D:\CBSE Materials\cbse_materials_index.json"
MAP_GUIDE_PATH = r"D:\CBSE Materials\Map Work\CBSE_Class_10_Social_Science_Complete_Map_Work_Guide.md"
SCRATCH_DIR = r"C:\Users\aryan\.gemini\antigravity\scratch\academic-command-center"
DEST_DIR = r"D:\CBSE Materials"

# GitHub & Storage Configurations
GITHUB_USER = "AryansDevStudios"
GITHUB_REPO = "cbse-class10-materials"
GITHUB_BRANCH = "main"

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
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover" />
  <meta name="theme-color" content="#090b10" />
  <meta name="apple-mobile-web-app-capable" content="yes" />
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
  <meta name="description" content="CBSE Class 10 Academic Command Center - High-efficiency mobile & desktop archive of board papers, marking schemes, textbooks, exemplars, and topper answers with Mozilla PDF.js viewer." />
  <title>CBSE Academic Command Center — Class 10 Vault</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    /* ============================================================
       DESIGN TOKENS — High-Efficiency Linear / DevDocs Theme
       ============================================================ */
    :root {{
      --bg-canvas: #090b10;
      --bg-subtle: #0f131c;
      --bg-surface: #151a26;
      --bg-elevated: #1b2232;
      --bg-overlay: #232c40;
      --bg-hover: rgba(255, 255, 255, 0.06);
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
      --accent-emerald-soft: rgba(16, 185, 129, 0.14);
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
      --header-height: 60px;
      --bottom-nav-height: 60px;
      --transition-fast: 150ms cubic-bezier(0.16, 1, 0.3, 1);
      --transition-smooth: 250ms cubic-bezier(0.16, 1, 0.3, 1);
    }}

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

    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}

    html, body {{
      height: 100%;
      width: 100%;
      font-family: var(--font-sans);
      background: var(--bg-canvas);
      color: var(--text-primary);
      overflow: hidden;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }}

    a {{ color: inherit; text-decoration: none; }}
    button, input, select {{ font: inherit; color: inherit; border: none; background: none; }}
    button {{ cursor: pointer; touch-action: manipulation; }}

    .app-root {{
      display: flex;
      flex-direction: column;
      height: 100vh;
      height: 100dvh;
      width: 100vw;
      overflow: hidden;
      position: relative;
    }}

    /* ============================================================
       TOP HEADER
       ============================================================ */
    .header {{
      height: var(--header-height);
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 16px;
      gap: 12px;
      z-index: 40;
      flex-shrink: 0;
    }}

    .header-left {{
      display: flex;
      align-items: center;
      gap: 12px;
      min-width: 0;
    }}

    .mobile-menu-btn {{
      display: none;
      width: 38px;
      height: 38px;
      border-radius: var(--radius-md);
      background: var(--bg-subtle);
      border: 1px solid var(--border-subtle);
      align-items: center;
      justify-content: center;
      font-size: 18px;
      color: var(--text-primary);
      flex-shrink: 0;
    }}

    .brand {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-weight: 800;
      font-size: 15px;
      letter-spacing: -0.02em;
      white-space: nowrap;
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
      font-size: 14px;
      box-shadow: 0 2px 8px rgba(99, 102, 241, 0.4);
      flex-shrink: 0;
    }}

    .brand-badge {{
      font-size: 10px;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: var(--radius-full);
      background: var(--accent-indigo-soft);
      color: var(--accent-indigo);
      border: 1px solid rgba(99, 102, 241, 0.25);
    }}

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
      min-width: 240px;
      max-width: 340px;
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
      padding: 1px 6px;
      border-radius: 4px;
      color: var(--text-muted);
    }}

    /* Header Progress Tracker */
    .header-progress-box {{
      display: flex;
      flex-direction: column;
      gap: 4px;
      min-width: 170px;
      padding: 4px 10px;
      background: var(--bg-subtle);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
    }}

    .progress-text-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 11px;
      font-weight: 600;
      color: var(--text-secondary);
      font-family: var(--font-mono);
    }}

    .progress-bar-track {{
      height: 4px;
      background: var(--bg-elevated);
      border-radius: var(--radius-full);
      overflow: hidden;
    }}

    .progress-bar-fill {{
      height: 100%;
      background: linear-gradient(90deg, #10b981, #06b6d4);
      border-radius: var(--radius-full);
      transition: width 0.3s ease;
      width: 0%;
    }}

    .header-right {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-shrink: 0;
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
      flex-shrink: 0;
    }}

    .icon-btn:hover {{
      background: var(--bg-elevated);
      color: var(--text-primary);
      border-color: var(--border-medium);
    }}

    /* ============================================================
       SUBJECT SCROLLER BAR
       ============================================================ */
    .subject-bar {{
      height: 48px;
      background: var(--bg-subtle);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      padding: 0 16px;
      gap: 8px;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      scroll-snap-type: x mandatory;
      flex-shrink: 0;
    }}

    .subject-bar::-webkit-scrollbar {{ display: none; }}
    .subject-bar {{ scrollbar-width: none; }}

    .subject-pill {{
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 6px 13px;
      border-radius: var(--radius-full);
      font-size: 13px;
      font-weight: 600;
      color: var(--text-secondary);
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      white-space: nowrap;
      transition: var(--transition-fast);
      scroll-snap-align: start;
      flex-shrink: 0;
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
      opacity: 0.85;
      background: rgba(0, 0, 0, 0.22);
      padding: 1px 6px;
      border-radius: var(--radius-full);
    }}

    /* ============================================================
       MAIN WORKSPACE
       ============================================================ */
    .main-container {{
      display: flex;
      flex: 1;
      height: calc(100vh - var(--header-height) - 48px);
      height: calc(100dvh - var(--header-height) - 48px);
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
      -webkit-overflow-scrolling: touch;
      flex-shrink: 0;
      user-select: none;
      z-index: 50;
    }}

    .drawer-header-bar {{
      display: none;
      align-items: center;
      justify-content: space-between;
      padding: 14px 16px;
      border-bottom: 1px solid var(--border-subtle);
      background: var(--bg-subtle);
    }}

    .sidebar-section {{
      padding: 14px 16px;
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
      padding: 9px 12px;
      border-radius: var(--radius-sm);
      font-size: 13px;
      font-weight: 500;
      color: var(--text-secondary);
      margin-bottom: 3px;
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
      padding: 1px 7px;
      border-radius: var(--radius-full);
      flex-shrink: 0;
    }}

    .chip-group {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }}

    .chip {{
      padding: 5px 10px;
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

    .drawer-backdrop {{
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.7);
      backdrop-filter: blur(4px);
      z-index: 45;
      opacity: 0;
      pointer-events: none;
      transition: opacity var(--transition-smooth);
    }}

    .drawer-backdrop.active {{
      opacity: 1;
      pointer-events: auto;
    }}

    /* Main Content Stage */
    .content-stage {{
      flex: 1;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      background: var(--bg-canvas);
      position: relative;
    }}

    /* Stage Toolbar */
    .stage-toolbar {{
      min-height: 50px;
      padding: 8px 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--border-subtle);
      background: var(--bg-subtle);
      gap: 12px;
      flex-wrap: wrap;
      flex-shrink: 0;
    }}

    .toolbar-left {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 13px;
      color: var(--text-secondary);
      flex-wrap: wrap;
    }}

    .active-filter-badge {{
      font-size: 11px;
      font-weight: 600;
      padding: 2px 8px;
      background: var(--bg-surface);
      border: 1px solid var(--border-medium);
      border-radius: var(--radius-full);
      color: var(--text-primary);
    }}

    .toolbar-right {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
      margin-left: auto;
    }}

    .select-dropdown {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 5px 10px;
      font-size: 12px;
      color: var(--text-primary);
      outline: none;
      cursor: pointer;
    }}

    .toggle-switch-label {{
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 12px;
      font-weight: 600;
      color: var(--text-secondary);
      cursor: pointer;
      user-select: none;
      white-space: nowrap;
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
      -webkit-overflow-scrolling: touch;
      padding: 20px;
    }}

    .materials-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(310px, 1fr));
      gap: 14px;
    }}

    /* Card Item */
    .card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
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

    .card.is-completed {{
      border-color: rgba(16, 185, 129, 0.4);
      background: rgba(16, 185, 129, 0.04);
    }}

    .card-top {{
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 8px;
    }}

    .card-tags {{
      display: flex;
      flex-wrap: wrap;
      gap: 5px;
    }}

    .tag {{
      font-size: 10px;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: var(--radius-sm);
      text-transform: uppercase;
      letter-spacing: 0.04em;
      white-space: nowrap;
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

    .tag-completed {{
      background: rgba(16, 185, 129, 0.2);
      color: var(--accent-emerald);
      border: 1px solid rgba(16, 185, 129, 0.4);
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
      font-size: 11px;
      color: var(--text-muted);
      font-family: var(--font-mono);
      flex-wrap: wrap;
    }}

    .card-actions {{
      margin-top: auto;
      display: flex;
      align-items: center;
      gap: 8px;
      padding-top: 10px;
      border-top: 1px solid var(--border-subtle);
      flex-wrap: wrap;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 7px 12px;
      min-height: 36px;
      border-radius: var(--radius-sm);
      font-size: 12px;
      font-weight: 600;
      transition: var(--transition-fast);
      cursor: pointer;
      white-space: nowrap;
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
      flex: 1;
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

    .btn-done {{
      background: var(--bg-elevated);
      color: var(--text-muted);
      border: 1px solid var(--border-subtle);
      font-size: 11px;
      padding: 6px 10px;
    }}

    .btn-done.done {{
      background: rgba(16, 185, 129, 0.16);
      color: var(--accent-emerald);
      border-color: rgba(16, 185, 129, 0.4);
      font-weight: 700;
    }}

    /* Table View Layout */
    .table-container {{
      width: 100%;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
    }}

    .materials-table {{
      width: 100%;
      min-width: 680px;
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
       MOBILE BOTTOM NAVIGATION BAR
       ============================================================ */
    .mobile-bottom-nav {{
      display: none;
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      height: var(--bottom-nav-height);
      background: var(--bg-surface);
      border-top: 1px solid var(--border-subtle);
      z-index: 60;
      align-items: center;
      justify-content: space-around;
      padding-bottom: env(safe-area-inset-bottom, 0px);
      box-shadow: 0 -4px 16px rgba(0, 0, 0, 0.25);
    }}

    .bottom-nav-item {{
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 3px;
      flex: 1;
      height: 100%;
      color: var(--text-secondary);
      font-size: 10px;
      font-weight: 600;
      transition: var(--transition-fast);
      position: relative;
    }}

    .bottom-nav-item:active, .bottom-nav-item.active {{
      color: var(--accent-indigo);
    }}

    .bottom-nav-icon {{
      font-size: 18px;
    }}

    /* ============================================================
       DUAL-PANE SPLIT WORKBENCH (MOZILLA PDF.JS INTEGRATED)
       ============================================================ */
    .split-workbench {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      height: 100dvh;
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
      min-height: 54px;
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 6px 14px;
      gap: 10px;
      flex-shrink: 0;
      flex-wrap: wrap;
    }}

    .workbench-titles {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex: 1;
      overflow: hidden;
      min-width: 200px;
    }}

    .doc-pill {{
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 4px 10px;
      background: var(--bg-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      font-size: 12px;
      font-weight: 600;
      color: var(--text-primary);
      max-width: 48%;
      overflow: hidden;
      white-space: nowrap;
      text-overflow: ellipsis;
    }}

    .doc-pill.left {{ border-left: 3px solid var(--accent-indigo); }}
    .doc-pill.right {{ border-left: 3px solid var(--accent-emerald); }}

    .mobile-tab-switcher {{
      display: none;
      background: var(--bg-subtle);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-full);
      padding: 3px;
      gap: 4px;
      width: 100%;
      margin: 4px 0;
    }}

    .mobile-tab-btn {{
      flex: 1;
      padding: 6px 10px;
      border-radius: var(--radius-full);
      font-size: 12px;
      font-weight: 600;
      color: var(--text-secondary);
      text-align: center;
      transition: var(--transition-fast);
    }}

    .mobile-tab-btn.active {{
      background: var(--accent-indigo);
      color: white;
      box-shadow: 0 1px 6px rgba(99, 102, 241, 0.4);
    }}

    .workbench-controls {{
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
    }}

    .split-controls-group {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}

    .workbench-body {{
      flex: 1;
      display: flex;
      overflow: hidden;
      position: relative;
    }}

    .workbench-body.is-resizing {{
      user-select: none !important;
      cursor: col-resize !important;
    }}

    .workbench-body.is-resizing iframe {{
      pointer-events: none !important;
    }}

    .workbench-body.is-resizing .workbench-pane {{
      transition: none !important;
    }}

    .workbench-pane {{
      height: 100%;
      background: #1e1e24;
      display: flex;
      flex-direction: column;
      position: relative;
      overflow: hidden;
      transition: width var(--transition-fast);
      min-width: 0;
    }}

    .workbench-pane iframe {{
      width: 100%;
      height: 100%;
      border: none;
      background: #2b2b2b;
      display: block;
    }}

    .pane-divider {{
      width: 10px;
      background: var(--bg-surface);
      border-left: 1px solid var(--border-subtle);
      border-right: 1px solid var(--border-subtle);
      cursor: col-resize;
      display: flex;
      align-items: center;
      justify-content: center;
      user-select: none;
      touch-action: none;
      flex-shrink: 0;
      position: relative;
      z-index: 20;
      transition: background var(--transition-fast);
    }}

    .pane-divider::after {{
      content: '';
      width: 2px;
      height: 32px;
      border-radius: 2px;
      background: var(--text-muted);
      opacity: 0.6;
      transition: background var(--transition-fast), height var(--transition-fast);
    }}

    .pane-divider:hover,
    .pane-divider.is-dragging {{
      background: var(--bg-elevated);
    }}

    .pane-divider:hover::after,
    .pane-divider.is-dragging::after {{
      background: var(--accent-indigo);
      opacity: 1;
      height: 48px;
    }}

    /* Single vs Split Workbench states */
    .split-workbench:not(.is-split) #rightPane,
    .split-workbench:not(.is-split) #paneDivider,
    .split-workbench:not(.is-split) #rightDocPill,
    .split-workbench:not(.is-split) #splitControlsGroup,
    .split-workbench:not(.is-split) #mobileTabSwitcher,
    .split-workbench:not(.is-split) #mobileFlipBtn {{
      display: none !important;
    }}

    .split-workbench:not(.is-split) #leftPane {{
      width: 100% !important;
      display: flex !important;
    }}

    .split-workbench.is-split #rightPane {{
      display: flex;
    }}

    .split-workbench.is-split #paneDivider {{
      display: flex;
    }}

    .split-workbench.is-split #rightDocPill {{
      display: flex;
    }}

    .split-workbench.is-split #splitControlsGroup {{
      display: inline-flex;
    }}

    .companion-select {{
      background: var(--bg-surface);
      border: 1px solid var(--border-medium);
      border-radius: var(--radius-sm);
      color: var(--text-primary);
      font-size: 11px;
      font-weight: 600;
      padding: 4px 8px;
      outline: none;
      cursor: pointer;
      max-width: 200px;
    }}

    .mobile-flip-btn {{
      display: none;
      position: fixed;
      bottom: 24px;
      right: 20px;
      z-index: 110;
      background: linear-gradient(135deg, #6366f1, #10b981);
      color: white;
      font-size: 13px;
      font-weight: 700;
      padding: 10px 18px;
      border-radius: var(--radius-full);
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
      border: 1px solid rgba(255, 255, 255, 0.2);
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
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(8px);
      z-index: 150;
      display: none;
      align-items: flex-start;
      justify-content: center;
      padding-top: 80px;
    }}

    .search-modal-backdrop.active {{
      display: flex;
    }}

    .search-modal {{
      width: 640px;
      max-width: 92vw;
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
      padding: 14px 18px;
      border-bottom: 1px solid var(--border-subtle);
    }}

    .search-input-box input {{
      flex: 1;
      font-size: 15px;
      font-weight: 500;
      color: var(--text-primary);
      outline: none;
    }}

    .search-results-list {{
      max-height: 400px;
      overflow-y: auto;
      -webkit-overflow-scrolling: touch;
      padding: 8px;
    }}

    .search-result-item {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 10px 12px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      transition: var(--transition-fast);
      gap: 10px;
    }}

    .search-result-item:hover, .search-result-item.highlighted {{
      background: var(--bg-hover);
    }}

    .search-footer {{
      padding: 10px 16px;
      background: var(--bg-subtle);
      border-top: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 11px;
      color: var(--text-muted);
    }}

    /* ============================================================
       MAP WORK GUIDE MODAL
       ============================================================ */
    .map-modal-backdrop {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(0, 0, 0, 0.8);
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
      padding: 14px 18px;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: var(--bg-subtle);
      gap: 12px;
    }}

    .map-content {{
      flex: 1;
      overflow-y: auto;
      -webkit-overflow-scrolling: touch;
      padding: 20px;
      line-height: 1.6;
    }}

    .map-content h2 {{
      color: var(--accent-amber);
      font-size: 17px;
      margin: 20px 0 10px 0;
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 6px;
    }}

    .map-content h3 {{
      color: var(--text-primary);
      font-size: 14px;
      margin: 16px 0 8px 0;
    }}

    .map-content table {{
      width: 100%;
      min-width: 500px;
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

    .map-table-wrap {{
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      margin-bottom: 16px;
    }}


    /* ============================================================
       DATESHEET & EXAM COUNTDOWN HUB
       ============================================================ */
    .btn-datesheet {{
      background: linear-gradient(135deg, rgba(99, 102, 241, 0.18), rgba(6, 182, 212, 0.18));
      border: 1px solid rgba(99, 102, 241, 0.45);
      color: #818cf8;
      font-weight: 700;
      position: relative;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      padding: 7px 13px;
      border-radius: var(--radius-md);
      transition: var(--transition-fast);
      cursor: pointer;
      font-size: 13px;
      flex-shrink: 0;
    }}

    .btn-datesheet:hover {{
      background: linear-gradient(135deg, rgba(99, 102, 241, 0.35), rgba(6, 182, 212, 0.35));
      border-color: #6366f1;
      color: #ffffff;
      box-shadow: 0 0 16px rgba(99, 102, 241, 0.35);
      transform: translateY(-1px);
    }}

    .datesheet-btn-pulse {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #10b981;
      box-shadow: 0 0 8px #10b981;
      animation: pulseGreen 1.8s infinite;
      flex-shrink: 0;
    }}

    @keyframes pulseGreen {{
      0%, 100% {{ opacity: 1; transform: scale(1); }}
      50% {{ opacity: 0.4; transform: scale(1.3); }}
    }}

    .sidebar-datesheet-box {{
      padding: 0 16px 12px 16px;
      border-bottom: 1px solid var(--border-subtle);
      margin-bottom: 12px;
    }}

    .sidebar-datesheet-btn {{
      width: 100%;
      padding: 10px 12px;
      border-radius: var(--radius-md);
      background: linear-gradient(135deg, rgba(99, 102, 241, 0.15), rgba(6, 182, 212, 0.12));
      border: 1px solid rgba(99, 102, 241, 0.3);
      text-align: left;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      gap: 4px;
      transition: var(--transition-fast);
    }}

    .sidebar-datesheet-btn:hover {{
      background: linear-gradient(135deg, rgba(99, 102, 241, 0.25), rgba(6, 182, 212, 0.22));
      border-color: var(--accent-indigo);
    }}

    .sidebar-datesheet-top {{
      display: flex;
      align-items: center;
      gap: 7px;
    }}

    .sidebar-datesheet-title {{
      font-size: 13px;
      font-weight: 700;
      color: var(--text-primary);
    }}

    .sidebar-datesheet-sub {{
      font-size: 11px;
      font-family: var(--font-mono);
      color: var(--accent-cyan);
    }}

    /* Datesheet Modal Backdrop & Card */
    .datesheet-modal-backdrop {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      height: 100dvh;
      background: rgba(0, 0, 0, 0.82);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      z-index: 150;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 16px;
      animation: fadeIn 200ms ease;
    }}

    .datesheet-modal-backdrop.active {{
      display: flex;
    }}

    .datesheet-modal {{
      width: 1000px;
      max-width: 96vw;
      height: 90vh;
      height: 90dvh;
      background: var(--bg-surface);
      border: 1px solid var(--border-medium);
      border-radius: var(--radius-lg);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6), 0 0 30px rgba(99, 102, 241, 0.2);
    }}

    .datesheet-header {{
      padding: 14px 20px;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: var(--bg-subtle);
      gap: 12px;
      flex-wrap: wrap;
      flex-shrink: 0;
    }}

    .datesheet-title-wrap {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }}

    .datesheet-title-text {{
      font-size: 16px;
      font-weight: 800;
      color: var(--text-primary);
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .datesheet-badge-live {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.3);
      color: #10b981;
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: var(--radius-full);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .datesheet-header-actions {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .datesheet-content {{
      flex: 1;
      overflow-y: auto;
      -webkit-overflow-scrolling: touch;
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 18px;
    }}

    /* Hero Countdown Section */
    .datesheet-hero {{
      background: linear-gradient(135deg, rgba(99, 102, 241, 0.12) 0%, rgba(6, 182, 212, 0.08) 50%, rgba(16, 185, 129, 0.1) 100%);
      border: 1px solid rgba(99, 102, 241, 0.3);
      border-radius: var(--radius-md);
      padding: 18px 20px;
      display: grid;
      grid-template-columns: 1.2fr 1fr;
      gap: 18px;
      align-items: center;
      position: relative;
      overflow: hidden;
    }}

    .datesheet-hero::after {{
      content: '';
      position: absolute;
      top: -50%;
      right: -20%;
      width: 260px;
      height: 260px;
      background: radial-gradient(circle, rgba(99, 102, 241, 0.15) 0%, transparent 70%);
      pointer-events: none;
    }}

    .hero-clock-box {{
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .hero-label {{
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.8px;
      text-transform: uppercase;
      color: var(--text-secondary);
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .hero-clock-display {{
      font-size: 20px;
      font-weight: 800;
      color: var(--text-primary);
      font-family: var(--font-mono);
      letter-spacing: -0.3px;
    }}

    .hero-exam-milestone {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 12px;
      color: var(--accent-indigo);
      background: var(--accent-indigo-soft);
      padding: 5px 10px;
      border-radius: var(--radius-sm);
      width: fit-content;
      margin-top: 4px;
      font-weight: 600;
      border: 1px solid rgba(99, 102, 241, 0.2);
    }}

    .hero-countdown-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 8px;
    }}

    .countdown-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-medium);
      border-radius: var(--radius-sm);
      padding: 10px 4px;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      box-shadow: var(--shadow-sm);
    }}

    .countdown-val {{
      font-size: 24px;
      font-weight: 800;
      font-family: var(--font-mono);
      color: var(--accent-cyan);
      line-height: 1.1;
    }}

    .countdown-unit {{
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--text-muted);
      margin-top: 3px;
    }}

    /* Tabs Bar inside modal */
    .datesheet-tabs-bar {{
      display: flex;
      gap: 8px;
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 8px;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      flex-shrink: 0;
    }}

    .datesheet-tab-btn {{
      padding: 8px 14px;
      border-radius: var(--radius-md);
      font-size: 13px;
      font-weight: 600;
      color: var(--text-secondary);
      background: var(--bg-subtle);
      border: 1px solid var(--border-subtle);
      transition: var(--transition-fast);
      white-space: nowrap;
      display: flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
    }}

    .datesheet-tab-btn:hover {{
      background: var(--bg-elevated);
      color: var(--text-primary);
    }}

    .datesheet-tab-btn.active {{
      background: var(--accent-indigo-soft);
      color: var(--accent-indigo);
      border-color: rgba(99, 102, 241, 0.35);
      font-weight: 700;
    }}

    /* Tab Panes */
    .datesheet-pane {{
      display: none;
      flex-direction: column;
      gap: 14px;
    }}

    .datesheet-pane.active {{
      display: flex;
    }}

    /* Schedule Cards */
    .schedule-list {{
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}

    .schedule-card {{
      background: var(--bg-subtle);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 16px;
      display: grid;
      grid-template-columns: 150px 1fr auto;
      gap: 16px;
      align-items: center;
      transition: var(--transition-fast);
      position: relative;
    }}

    .schedule-card:hover {{
      border-color: var(--border-medium);
      background: var(--bg-elevated);
      transform: translateY(-1px);
      box-shadow: var(--shadow-sm);
    }}

    .schedule-card.major-focus {{
      border-left: 4px solid var(--accent-indigo);
    }}

    .schedule-date-col {{
      display: flex;
      flex-direction: column;
      gap: 3px;
    }}

    .sched-date {{
      font-size: 14px;
      font-weight: 800;
      color: var(--text-primary);
      white-space: nowrap;
    }}

    .sched-day {{
      font-size: 11px;
      font-weight: 600;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    .sched-time {{
      font-size: 11px;
      color: var(--accent-cyan);
      font-family: var(--font-mono);
      margin-top: 2px;
    }}

    .schedule-info-col {{
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .sched-subject-title {{
      font-size: 15px;
      font-weight: 700;
      color: var(--text-primary);
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .sched-code-badge {{
      font-size: 11px;
      font-weight: 700;
      font-family: var(--font-mono);
      background: var(--bg-surface);
      border: 1px solid var(--border-medium);
      padding: 2px 7px;
      border-radius: 4px;
      color: var(--text-secondary);
    }}

    .sched-marks-badge {{
      font-size: 10px;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 4px;
      background: rgba(16, 185, 129, 0.12);
      color: #10b981;
      border: 1px solid rgba(16, 185, 129, 0.25);
    }}

    .sched-gap-row {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .gap-badge {{
      font-size: 11px;
      font-weight: 700;
      padding: 3px 9px;
      border-radius: var(--radius-full);
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }}

    .gap-generous {{
      background: rgba(16, 185, 129, 0.15);
      color: #10b981;
      border: 1px solid rgba(16, 185, 129, 0.35);
    }}

    .gap-moderate {{
      background: rgba(245, 158, 11, 0.15);
      color: #f59e0b;
      border: 1px solid rgba(245, 158, 11, 0.35);
    }}

    .gap-start {{
      background: rgba(99, 102, 241, 0.15);
      color: #818cf8;
      border: 1px solid rgba(99, 102, 241, 0.35);
    }}

    .sched-notes {{
      font-size: 12px;
      color: var(--text-secondary);
      line-height: 1.45;
    }}

    .schedule-action-col {{
      display: flex;
      flex-direction: column;
      gap: 6px;
      align-items: flex-end;
    }}

    /* Timetable Table for All Subjects */
    .timetable-search-bar {{
      display: flex;
      align-items: center;
      gap: 10px;
      background: var(--bg-subtle);
      border: 1px solid var(--border-subtle);
      padding: 8px 12px;
      border-radius: var(--radius-md);
    }}

    .timetable-search-bar input {{
      flex: 1;
      color: var(--text-primary);
      font-size: 13px;
    }}

    .timetable-table-wrap {{
      overflow-x: auto;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      background: var(--bg-subtle);
    }}

    .timetable-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
      text-align: left;
    }}

    .timetable-table th {{
      background: var(--bg-elevated);
      color: var(--text-muted);
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      padding: 10px 14px;
      border-bottom: 1px solid var(--border-subtle);
    }}

    .timetable-table td {{
      padding: 10px 14px;
      border-bottom: 1px solid var(--border-subtle);
      color: var(--text-secondary);
    }}

    .timetable-table tr:hover td {{
      background: var(--bg-elevated);
      color: var(--text-primary);
    }}

    .timetable-table tr.major-row td {{
      font-weight: 600;
      color: var(--text-primary);
    }}

    /* Gap Strategy Section */
    .strategy-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 14px;
    }}

    .strategy-card {{
      background: var(--bg-subtle);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}

    .strategy-card-title {{
      font-size: 14px;
      font-weight: 700;
      color: var(--text-primary);
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .strategy-card-body {{
      font-size: 12px;
      color: var(--text-secondary);
      line-height: 1.5;
    }}

    /* Circulars List */
    .circular-list {{
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}

    .circular-item {{
      background: var(--bg-subtle);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 14px 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      transition: var(--transition-fast);
    }}

    .circular-item:hover {{
      border-color: var(--border-medium);
      background: var(--bg-elevated);
    }}

    .circular-info {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .circular-title {{
      font-size: 14px;
      font-weight: 700;
      color: var(--text-primary);
    }}

    .circular-meta {{
      font-size: 11px;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .circular-summary {{
      font-size: 12px;
      color: var(--text-secondary);
      line-height: 1.45;
      margin-top: 2px;
    }}

    /* Print Styles */
    @media print {{
      body * {{
        visibility: hidden;
      }}
      .datesheet-modal-backdrop,
      .datesheet-modal,
      .datesheet-modal * {{
        visibility: visible;
      }}
      .datesheet-modal-backdrop {{
        position: absolute;
        left: 0;
        top: 0;
        width: 100%;
        height: auto;
        background: white !important;
        padding: 0;
      }}
      .datesheet-modal {{
        border: none !important;
        box-shadow: none !important;
        width: 100% !important;
        height: auto !important;
        background: white !important;
        color: black !important;
      }}
      .datesheet-header-actions,
      .datesheet-tabs-bar,
      .schedule-action-col {{
        display: none !important;
      }}
      .schedule-card {{
        border: 1px solid #ccc !important;
        background: #fafafa !important;
        color: black !important;
        page-break-inside: avoid;
        margin-bottom: 8px;
      }}
    }}

    /* ============================================================
       RESPONSIVE BREAKPOINTS (TABLET & MOBILE)
       ============================================================ */
    @media (max-width: 900px) {{
      :root {{
        --header-height: 54px;
      }}

      .mobile-menu-btn {{
        display: flex;
      }}

      .btn-datesheet span.datesheet-btn-text {{
        display: none;
      }}

      .btn-datesheet {{
        padding: 6px 10px;
      }}

      .omni-search-btn {{
        min-width: auto;
        padding: 7px 10px;
      }}

      .omni-search-btn span:first-of-type {{
        display: none;
      }}

      .search-key-badge {{
        display: none;
      }}

      .header-progress-box {{
        display: none;
      }}

      #openMapWorkBtn {{
        display: none;
      }}

      .sidebar {{
        position: fixed;
        top: 0;
        left: 0;
        bottom: 0;
        width: 310px;
        max-width: 85vw;
        height: 100vh;
        height: 100dvh;
        z-index: 120;
        transform: translateX(-100%);
        transition: transform var(--transition-smooth);
        box-shadow: var(--shadow-lg);
      }}

      .sidebar.drawer-open {{
        transform: translateX(0);
      }}

      .drawer-header-bar {{
        display: flex;
      }}

      .main-container {{
        height: calc(100vh - var(--header-height) - 48px);
        height: calc(100dvh - var(--header-height) - 48px);
      }}

      .content-stage {{
        padding-bottom: var(--bottom-nav-height);
      }}

      .mobile-bottom-nav {{
        display: flex;
      }}
    }}

    @media (max-width: 640px) {{
      .stage-scroll {{
        padding: 12px;
      }}

      .materials-grid {{
        grid-template-columns: 1fr;
        gap: 10px;
      }}

      .card {{
        padding: 14px;
      }}

      .card-actions {{
        gap: 6px;
      }}

      .btn-split {{
        width: 100%;
        order: -1;
      }}

      .workbench-header {{
        padding: 8px 12px;
      }}

      .split-workbench.is-split .workbench-titles {{
        display: none;
      }}

      .split-workbench:not(.is-split) .workbench-titles {{
        display: flex;
        max-width: 60vw;
      }}

      .split-workbench.is-split .mobile-tab-switcher {{
        display: flex;
      }}

      .split-workbench.is-split .pane-divider {{
        display: none !important;
      }}

      .split-workbench.is-split .mobile-flip-btn {{
        display: block;
      }}

      #splitPreset50, #splitPresetLeft, #splitPresetRight {{
        display: none;
      }}

      .search-modal-backdrop {{
        padding-top: 0;
      }}

      .search-modal {{
        width: 100vw;
        height: 100vh;
        height: 100dvh;
        max-width: 100vw;
        border-radius: 0;
        border: none;
      }}

      .search-results-list {{
        max-height: calc(100vh - 120px);
      }}

      .map-modal {{
        width: 100vw;
        height: 100vh;
        height: 100dvh;
        max-width: 100vw;
        border-radius: 0;
      }}

      .map-content {{
        padding: 14px;
      }}
    }}
  </style>
</head>
<body>
  <div class="app-root">
    <!-- Top Header -->
    <header class="header">
      <div class="header-left">
        <button class="mobile-menu-btn" id="mobileDrawerBtn" title="Open Categories & Filters">
          ☰
        </button>

        <div class="brand">
          <div class="brand-icon">⚡</div>
          <span>CBSE Command</span>
          <span class="brand-badge">Class 10</span>
        </div>

        <button class="omni-search-btn" id="openOmniSearch">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          <span>Search 896 materials...</span>
          <span class="search-key-badge">Ctrl K</span>
        </button>
      </div>

      <div class="header-right">
        <!-- Study Completion Progress Tracker -->
        <div class="header-progress-box" title="Study Completion Tracker">
          <div class="progress-text-row">
            <span>Completed</span>
            <span id="progressSummaryText">0 / 896 (0%)</span>
          </div>
          <div class="progress-bar-track">
            <div class="progress-bar-fill" id="progressBarFill"></div>
          </div>
        </div>

        <button class="btn btn-datesheet" id="openDatesheetBtn" title="CBSE Class 10 Board Exam Datesheet 2027, Live Countdown & Gap Analysis">
          <span class="datesheet-btn-pulse"></span>
          <span class="datesheet-btn-text">📅 Datesheet & Countdown</span>
        </button>

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
      <div class="drawer-backdrop" id="drawerBackdrop"></div>

      <!-- Left Category Sidebar / Mobile Drawer -->
      <aside class="sidebar" id="sidebarDrawer">
        <div class="drawer-header-bar">
          <div style="display: flex; align-items: center; gap: 8px; font-weight: 700; font-size: 14px;">
            <span>⚡ Filters & Categories</span>
          </div>
          <button class="icon-btn" id="closeDrawerBtn" title="Close Drawer">✕</button>
        </div>

        <div class="sidebar-datesheet-box">
          <button class="sidebar-datesheet-btn" id="sidebarDatesheetBtn" title="CBSE Class 10 Datesheet & Live Countdown">
            <div class="sidebar-datesheet-top">
              <span class="datesheet-btn-pulse"></span>
              <span class="sidebar-datesheet-title">📅 Exam Datesheet 2027</span>
            </div>
            <div class="sidebar-datesheet-sub" id="sidebarDatesheetSub">Loading countdown...</div>
          </button>
        </div>

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
            <!-- Study Status Filter -->
            <select class="select-dropdown" id="studyStatusFilter" title="Filter by Study Progress">
              <option value="all">Status: All (896)</option>
              <option value="unfinished">Status: ⬜ Unfinished Only</option>
              <option value="completed">Status: ✅ Completed Only</option>
            </select>

            <label class="toggle-switch-label" title="Only display items with paired Question Paper + Marking Scheme">
              <input type="checkbox" id="pairedOnlyToggle" class="toggle-checkbox" />
              <span>⚡ Paired (Split View)</span>
            </label>

            <select class="select-dropdown" id="sortSelect">
              <option value="year_desc">Year (Newest)</option>
              <option value="year_asc">Year (Oldest)</option>
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
          <div class="table-container">
            <table class="materials-table" id="materialsTable" style="display: none;">
              <thead>
                <tr>
                  <th>Status</th>
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
        </div>
      </main>
    </div>

    <!-- Mobile Bottom Navigation Bar -->
    <nav class="mobile-bottom-nav" id="mobileBottomNav">
      <button class="bottom-nav-item" id="bottomNavSearch">
        <span class="bottom-nav-icon">🔍</span>
        <span>Search</span>
      </button>
      <button class="bottom-nav-item" id="bottomNavFilters">
        <span class="bottom-nav-icon">⚡</span>
        <span>Filters</span>
      </button>
      <button class="bottom-nav-item" id="bottomNavMap">
        <span class="bottom-nav-icon">🗺️</span>
        <span>Map Work</span>
      </button>
      <button class="bottom-nav-item" id="bottomNavTheme">
        <span class="bottom-nav-icon" id="bottomNavThemeIcon">🌓</span>
        <span>Theme</span>
      </button>
      <button class="bottom-nav-item" id="bottomNavDatesheet">
        <span class="bottom-nav-icon">📅</span>
        <span>Datesheet</span>
      </button>
      <button class="bottom-nav-item" id="bottomNavTop">
        <span class="bottom-nav-icon">⬆️</span>
        <span>Top</span>
      </button>
    </nav>
  </div>

  <!-- ============================================================
       DUAL-PANE SPLIT WORKBENCH (MOZILLA PDF.JS INTEGRATED)
       ============================================================ -->
  <div class="split-workbench" id="splitWorkbench">
    <div class="workbench-header">
      <div class="workbench-titles">
        <div class="doc-pill left" id="leftDocPill">
          <span>📄</span>
          <span id="leftDocTitle">Document</span>
        </div>
        <div class="doc-pill right" id="rightDocPill">
          <span>🎯</span>
          <span id="rightDocTitle">Official Marking Scheme</span>
        </div>
      </div>

      <div class="mobile-tab-switcher" id="mobileTabSwitcher">
        <button class="mobile-tab-btn active" id="mobileTabLeft">📄 Question Paper</button>
        <button class="mobile-tab-btn" id="mobileTabRight">🎯 Solution / Marking Scheme</button>
      </div>

      <div class="workbench-controls">
        <!-- Toggle Split View Button (only shown when document has a pair) -->
        <button class="btn btn-split" id="toggleSplitViewBtn" style="display: none;">⚡ Split View (QP + MS)</button>

        <!-- Workbench Mark Complete Toggle -->
        <button class="btn btn-done" id="workbenchMarkDoneBtn">⬜ Mark Complete</button>

        <!-- Split View Controls Group (only visible when in split mode) -->
        <div class="split-controls-group" id="splitControlsGroup">
          <select class="companion-select" id="companionSelector" title="Switch Right Pane Document">
          </select>
          <button class="btn btn-secondary" id="swapPanesBtn" title="Swap Left and Right Panes">⇄ Swap</button>
          <button class="btn btn-secondary" id="splitPreset50" title="50/50 Split View">50 / 50</button>
          <button class="btn btn-secondary" id="splitPresetLeft" title="Focus Left Pane (70/30)">Left</button>
          <button class="btn btn-secondary" id="splitPresetRight" title="Focus Right Pane (30/70)">Right</button>
        </div>

        <button class="btn btn-secondary" id="popoutBtn" title="Open in browser tab">↗ Pop Out</button>
        <button class="btn btn-primary" id="closeWorkbenchBtn" title="Close Viewer (ESC)">✕ Close</button>
      </div>
    </div>

    <!-- Mobile Quick Flip Floating Button (only shown in split mode on mobile) -->
    <button class="mobile-flip-btn" id="mobileFlipBtn">⚡ Switch to Solution ➔</button>

    <div class="workbench-body" id="workbenchBody">
      <div class="workbench-pane" id="leftPane">
        <iframe id="leftIframe" src="about:blank" allow="fullscreen"></iframe>
      </div>

      <div class="pane-divider" id="paneDivider"></div>

      <div class="workbench-pane" id="rightPane">
        <iframe id="rightIframe" src="about:blank" allow="fullscreen"></iframe>
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
        <input type="search" id="omniSearchInput" placeholder="Search 896 materials (30-1-1, SQP, Topper, Science)..." autofocus />
        <button class="icon-btn" id="closeSearchModalBtn" style="width: 30px; height: 30px;">✕</button>
      </div>
      <div class="search-results-list" id="searchResultsList"></div>
      <div class="search-footer">
        <span>Press <kbd>↑</kbd> <kbd>↓</kbd> or tap to view, <kbd>ESC</kbd> to close</span>
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
        <div style="font-weight: 700; font-size: 15px;">🗺️ Class 10 SST Complete Map Work Guide (5 Marks)</div>
        <button class="btn btn-secondary" id="closeMapModalBtn">✕ Close</button>
      </div>
      <div class="map-content" id="mapContentArea"></div>
    </div>
  </div>

  <!-- ============================================================
       CBSE DATESHEET & COUNTDOWN HUB MODAL
       ============================================================ -->
  <div class="datesheet-modal-backdrop" id="datesheetModal">
    <div class="datesheet-modal">
      <div class="datesheet-header">
        <div class="datesheet-title-wrap">
          <div class="datesheet-title-text">
            <span>📅</span>
            <span>CBSE Class 10 Board Exam Datesheet 2027</span>
          </div>
          <div class="datesheet-badge-live">
            <span class="datesheet-pulse-dot"></span>
            <span>Official Release • 101 Days Notice</span>
          </div>
        </div>

        <div class="datesheet-header-actions">
          <a href="https://www.cbse.gov.in/cbsenew/documents/Datesheet_ClassX%20_XII_2027_Main_06112026.pdf" target="_blank" class="btn btn-secondary" title="Download Official CBSE Datesheet PDF (4.48 MB)">
            📥 Official PDF
          </a>
          <button class="btn btn-secondary" id="printDatesheetBtn" title="Print Clean Datesheet">
            🖨️ Print
          </button>
          <button class="btn btn-primary" id="closeDatesheetModalBtn">✕ Close</button>
        </div>
      </div>

      <div class="datesheet-content">
        <!-- Live Countdown & Clock Hero -->
        <div class="datesheet-hero">
          <div class="hero-clock-box">
            <div class="hero-label">
              <span>🕒 Live Clock (IST)</span>
            </div>
            <div class="hero-clock-display" id="heroClockDisplay">--:--:-- --</div>
            <div class="hero-exam-milestone" id="heroExamMilestone">
              <span>🚀 Target: First Exam • Tue, 16 Feb 2027 (10:30 AM)</span>
            </div>
          </div>

          <div class="hero-countdown-grid">
            <div class="countdown-card">
              <span class="countdown-val" id="cntDays">00</span>
              <span class="countdown-unit">Days</span>
            </div>
            <div class="countdown-card">
              <span class="countdown-val" id="cntHours">00</span>
              <span class="countdown-unit">Hours</span>
            </div>
            <div class="countdown-card">
              <span class="countdown-val" id="cntMins">00</span>
              <span class="countdown-unit">Mins</span>
            </div>
            <div class="countdown-card">
              <span class="countdown-val" id="cntSecs">00</span>
              <span class="countdown-unit">Secs</span>
            </div>
          </div>
        </div>

        <!-- Navigation Tabs inside Modal -->
        <div class="datesheet-tabs-bar">
          <button class="datesheet-tab-btn active" data-tab="major">
            <span>⭐ Major 6 Subjects</span>
          </button>
          <button class="datesheet-tab-btn" data-tab="all">
            <span>📋 All Class 10 Subjects (83)</span>
          </button>
          <button class="datesheet-tab-btn" data-tab="strategy">
            <span>⚡ Gap Analysis & Strategy</span>
          </button>
          <button class="datesheet-tab-btn" data-tab="circulars">
            <span>📢 Official Circulars & Rules</span>
          </button>
        </div>

        <!-- Tab 1: Major Core Subjects -->
        <div class="datesheet-pane active" id="paneMajor">
          <div class="schedule-list" id="majorSubjectsList">
            <!-- Dynamically populated -->
          </div>
        </div>

        <!-- Tab 2: Full Class 10 Timetable -->
        <div class="datesheet-pane" id="paneAll">
          <div class="timetable-search-bar">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
            <input type="text" id="timetableSearchInput" placeholder="Filter by subject code (041, 086) or subject name..." />
          </div>
          <div class="timetable-table-wrap">
            <table class="timetable-table">
              <thead>
                <tr>
                  <th>Date & Day</th>
                  <th>Time</th>
                  <th>Code</th>
                  <th>Subject Name</th>
                  <th>Action</th>
                </tr>
              </thead>
              <tbody id="allSubjectsTableBody">
                <!-- Dynamically populated -->
              </tbody>
            </table>
          </div>
        </div>

        <!-- Tab 3: Gap Analysis & Revision Strategy -->
        <div class="datesheet-pane" id="paneStrategy">
          <div class="strategy-grid">
            <div class="strategy-card">
              <div class="strategy-card-title">
                <span>🔥</span>
                <span>The 4-Day Science Gap (Feb 18 - 21)</span>
              </div>
              <div class="strategy-card-body">
                <strong>96 Hours of Pure Revision!</strong><br>
                • <strong>Day 1 (Feb 18):</strong> Physics Electricity & Magnetic Effects numericals and ray diagrams.<br>
                • <strong>Day 2 (Feb 19):</strong> Chemistry balancing, Carbon & its Compounds, Chemical Reactions.<br>
                • <strong>Day 3 (Feb 20):</strong> Biology Life Processes, Reproduction & Heredity diagrams.<br>
                • <strong>Day 4 (Feb 21):</strong> NCERT Exemplar MCQ practice & 2027 Sample Question Paper (SQP).
              </div>
            </div>

            <div class="strategy-card">
              <div class="strategy-card-title">
                <span>🖋️</span>
                <span>The 4-Day Hindi Gap (Feb 27 - Mar 2)</span>
              </div>
              <div class="strategy-card-body">
                <strong>Full Polish for Course A (002) / B (085):</strong><br>
                • <strong>Day 1:</strong> Vyakaran rules (Vachya, Pad Parichay, Vakya Bhed, Ras/Alankar).<br>
                • <strong>Day 2:</strong> Kshitij prose and poetry chapter key concepts.<br>
                • <strong>Day 3:</strong> Kritika supplementary reader chapters & character motivations.<br>
                • <strong>Day 4:</strong> Anuched, Patra, Sandesh, and Vigyapan Lekhan practice for full marks.
              </div>
            </div>

            <div class="strategy-card">
              <div class="strategy-card-title">
                <span>🌍</span>
                <span>The 4-Day Social Science Sprint (Mar 4 - 7)</span>
              </div>
              <div class="strategy-card-body">
                <strong>Grand Finale SST Master Plan:</strong><br>
                • <strong>Day 1:</strong> History Nationalism in Europe & India events & timelines.<br>
                • <strong>Day 2:</strong> Geography chapters + <strong>5-Marks Guaranteed Map Work</strong> (use our Map Guide!).<br>
                • <strong>Day 3:</strong> Political Science key institutions and case-based questions.<br>
                • <strong>Day 4:</strong> Economics key indicators & complete 3-hour mock board simulation.
              </div>
            </div>

            <div class="strategy-card">
              <div class="strategy-card-title">
                <span>⏰</span>
                <span>CBSE Official Exam Day Timings Checklist</span>
              </div>
              <div class="strategy-card-body">
                • <strong>10:00 AM:</strong> Strict Centre Entry Gate Closure. No entry allowed after 10:00 AM.<br>
                • <strong>10:15 AM:</strong> Question Paper distribution to students.<br>
                • <strong>10:15 AM - 10:30 AM:</strong> 15-Minute Reading Period (Plan your questions, do NOT write answers).<br>
                • <strong>10:30 AM:</strong> Answer booklet writing commences.<br>
                • <strong>01:30 PM:</strong> 3-Hour examination concludes.
              </div>
            </div>
          </div>
        </div>

        <!-- Tab 4: Official CBSE Circulars -->
        <div class="datesheet-pane" id="paneCirculars">
          <div class="circular-list" id="circularsList">
            <!-- Dynamically populated -->
          </div>
        </div>
      </div>
    </div>
  </div>

  <script>
    window.__CBSE_DATA__ = {data_json_str};
    window.__MAP_GUIDE_MD__ = {map_guide_json_str};
  </script>

  <!-- Application Logic -->
  <script>
    (function() {{
      const GITHUB_USER = "{GITHUB_USER}";
      const GITHUB_REPO = "{GITHUB_REPO}";
      const GITHUB_BRANCH = "{GITHUB_BRANCH}";
      const MOZILLA_VIEWER_BASE = "https://mozilla.github.io/pdf.js/web/viewer.html";

      const state = {{
        allMaterials: window.__CBSE_DATA__.materials || [],
        selectedSubject: 'All',
        selectedCategory: 'All',
        selectedYear: 'All',
        selectedType: 'All',
        selectedStudyStatus: 'all', // 'all', 'unfinished', 'completed'
        pairedOnly: false,
        searchQuery: '',
        sortBy: 'year_desc',
        viewMode: 'grid',
        theme: localStorage.getItem('cbse_theme') || 'dark',

        // Completed Document Tracking (localStorage)
        completedDocs: new Set(JSON.parse(localStorage.getItem('cbse_completed_docs') || '[]')),

        // Workbench state
        activeLeftItem: null,
        activeRightItem: null,
        splitPercent: parseFloat(localStorage.getItem('cbse_split_percent')) || 50,
        activeMobileTab: 'left'
      }};

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

      const dom = {{
        categoryNavList: document.getElementById('categoryNavList'),
        materialsGrid: document.getElementById('materialsGrid'),
        materialsTable: document.getElementById('materialsTable'),
        materialsTableBody: document.getElementById('materialsTableBody'),
        subjectBar: document.getElementById('subjectBar'),
        yearChipGroup: document.getElementById('yearChipGroup'),
        typeChipGroup: document.getElementById('typeChipGroup'),
        studyStatusFilter: document.getElementById('studyStatusFilter'),
        pairedOnlyToggle: document.getElementById('pairedOnlyToggle'),
        sortSelect: document.getElementById('sortSelect'),
        viewModeToggle: document.getElementById('viewModeToggle'),
        viewModeIcon: document.getElementById('viewModeIcon'),
        resultsCountBadge: document.getElementById('resultsCountBadge'),
        activeFilterSummary: document.getElementById('activeFilterSummary'),
        themeToggleBtn: document.getElementById('themeToggleBtn'),
        themeIcon: document.getElementById('themeIcon'),
        stageScrollArea: document.getElementById('stageScrollArea'),

        // Progress Tracking Elements
        progressSummaryText: document.getElementById('progressSummaryText'),
        progressBarFill: document.getElementById('progressBarFill'),

        // Mobile Drawer
        mobileDrawerBtn: document.getElementById('mobileDrawerBtn'),
        sidebarDrawer: document.getElementById('sidebarDrawer'),
        drawerBackdrop: document.getElementById('drawerBackdrop'),
        closeDrawerBtn: document.getElementById('closeDrawerBtn'),

        // Mobile Bottom Nav
        bottomNavSearch: document.getElementById('bottomNavSearch'),
        bottomNavFilters: document.getElementById('bottomNavFilters'),
        bottomNavMap: document.getElementById('bottomNavMap'),
        bottomNavTheme: document.getElementById('bottomNavTheme'),
        bottomNavThemeIcon: document.getElementById('bottomNavThemeIcon'),
        bottomNavTop: document.getElementById('bottomNavTop'),
        
        // Workbench
        splitWorkbench: document.getElementById('splitWorkbench'),
        workbenchBody: document.getElementById('workbenchBody'),
        closeWorkbenchBtn: document.getElementById('closeWorkbenchBtn'),
        leftDocTitle: document.getElementById('leftDocTitle'),
        rightDocTitle: document.getElementById('rightDocTitle'),
        leftDocPill: document.getElementById('leftDocPill'),
        rightDocPill: document.getElementById('rightDocPill'),
        leftIframe: document.getElementById('leftIframe'),
        rightIframe: document.getElementById('rightIframe'),
        paneDivider: document.getElementById('paneDivider'),
        swapPanesBtn: document.getElementById('swapPanesBtn'),
        splitPreset50: document.getElementById('splitPreset50'),
        splitPresetLeft: document.getElementById('splitPresetLeft'),
        splitPresetRight: document.getElementById('splitPresetRight'),
        popoutBtn: document.getElementById('popoutBtn'),
        companionSelector: document.getElementById('companionSelector'),
        splitControlsGroup: document.getElementById('splitControlsGroup'),
        toggleSplitViewBtn: document.getElementById('toggleSplitViewBtn'),
        workbenchMarkDoneBtn: document.getElementById('workbenchMarkDoneBtn'),
        leftPane: document.getElementById('leftPane'),
        rightPane: document.getElementById('rightPane'),

        // Mobile Workbench Tabs
        mobileTabSwitcher: document.getElementById('mobileTabSwitcher'),
        mobileTabLeft: document.getElementById('mobileTabLeft'),
        mobileTabRight: document.getElementById('mobileTabRight'),
        mobileFlipBtn: document.getElementById('mobileFlipBtn'),

        // Omni Search
        openOmniSearch: document.getElementById('openOmniSearch'),
        searchModal: document.getElementById('searchModal'),
        omniSearchInput: document.getElementById('omniSearchInput'),
        searchResultsList: document.getElementById('searchResultsList'),
        omniMatchCount: document.getElementById('omniMatchCount'),
        closeSearchModalBtn: document.getElementById('closeSearchModalBtn'),

        // Map Work
        openMapWorkBtn: document.getElementById('openMapWorkBtn'),
        mapModal: document.getElementById('mapModal'),
        closeMapModalBtn: document.getElementById('closeMapModalBtn'),
        mapContentArea: document.getElementById('mapContentArea'),

        // Datesheet & Countdown Hub
        openDatesheetBtn: document.getElementById('openDatesheetBtn'),
        datesheetModal: document.getElementById('datesheetModal'),
        closeDatesheetModalBtn: document.getElementById('closeDatesheetModalBtn'),
        bottomNavDatesheet: document.getElementById('bottomNavDatesheet'),
        sidebarDatesheetBtn: document.getElementById('sidebarDatesheetBtn'),
        sidebarDatesheetSub: document.getElementById('sidebarDatesheetSub'),
        printDatesheetBtn: document.getElementById('printDatesheetBtn'),
        heroClockDisplay: document.getElementById('heroClockDisplay'),
        heroExamMilestone: document.getElementById('heroExamMilestone'),
        cntDays: document.getElementById('cntDays'),
        cntHours: document.getElementById('cntHours'),
        cntMins: document.getElementById('cntMins'),
        cntSecs: document.getElementById('cntSecs'),
        majorSubjectsList: document.getElementById('majorSubjectsList'),
        allSubjectsTableBody: document.getElementById('allSubjectsTableBody'),
        timetableSearchInput: document.getElementById('timetableSearchInput'),
        circularsList: document.getElementById('circularsList')
      }};

      // ============================================================
      // NAVIGATION & URL STATE SYNCHRONIZATION
      // ============================================================
      function getUrlParams() {{
        let search = window.location.search;
        if (!search && window.location.hash) {{
          const h = window.location.hash.slice(1);
          search = h.includes('?') ? h.slice(h.indexOf('?')) : (h.includes('=') ? '?' + h : '');
        }}
        return new URLSearchParams(search || '');
      }}

      function updateUrl(push = false) {{
        const params = new URLSearchParams();
        if (state.selectedSubject && state.selectedSubject !== 'All') params.set('subject', state.selectedSubject);
        if (state.selectedCategory && state.selectedCategory !== 'All') params.set('category', state.selectedCategory);
        if (state.selectedYear && state.selectedYear !== 'All') params.set('year', state.selectedYear);
        if (state.selectedType && state.selectedType !== 'All') params.set('type', state.selectedType);
        if (state.selectedStudyStatus && state.selectedStudyStatus !== 'all') params.set('status', state.selectedStudyStatus);
        if (state.sortBy && state.sortBy !== 'year_desc') params.set('sort', state.sortBy);
        if (state.pairedOnly) params.set('paired', '1');
        if (state.viewMode && state.viewMode !== 'grid') params.set('view', state.viewMode);
        if (state.searchQuery) params.set('q', state.searchQuery);

        if (dom.splitWorkbench.classList.contains('active') && state.activeLeftItem) {{
          params.set('doc', state.activeLeftItem.id);
          if (dom.splitWorkbench.classList.contains('is-split') && state.activeRightItem) {{
            params.set('right', state.activeRightItem.id);
            if (state.splitPercent) {{
              params.set('split', Math.round(state.splitPercent).toString());
            }}
            if (state.activeMobileTab && state.activeMobileTab !== 'left') {{
              params.set('tab', state.activeMobileTab);
            }}
          }}
        }}

        if (dom.mapModal.classList.contains('active')) {{
          params.set('map', '1');
        }}

        if (dom.datesheetModal && dom.datesheetModal.classList.contains('active')) {{
          params.set('datesheet', '1');
        }}

        const qs = params.toString();
        const newUrl = qs ? (window.location.pathname + '?' + qs) : window.location.pathname;

        try {{
          if (window.location.protocol.startsWith('http')) {{
            if (push) {{
              window.history.pushState({{ ...state }}, '', newUrl);
            }} else {{
              window.history.replaceState({{ ...state }}, '', newUrl);
            }}
          }} else {{
            const hashVal = qs ? '#' + qs : '';
            if (window.location.hash !== hashVal) {{
              if (push) window.location.hash = hashVal;
              else window.location.replace(window.location.pathname + hashVal);
            }}
          }}
        }} catch (e) {{
          try {{
            const hashVal = qs ? '#' + qs : '';
            if (window.location.hash !== hashVal) {{
              window.location.hash = hashVal;
            }}
          }} catch (err) {{}}
        }}
      }}

      function initNavigationAndState() {{
        const urlParams = getUrlParams();
        const hasUrlParams = Array.from(urlParams.keys()).length > 0;

        if (urlParams.has('subject')) {{
          state.selectedSubject = urlParams.get('subject');
        }} else if (localStorage.getItem('cbse_subject')) {{
          state.selectedSubject = localStorage.getItem('cbse_subject');
        }}

        if (urlParams.has('category')) {{
          state.selectedCategory = urlParams.get('category');
        }} else if (localStorage.getItem('cbse_category')) {{
          state.selectedCategory = localStorage.getItem('cbse_category');
        }}

        if (urlParams.has('year')) {{
          state.selectedYear = urlParams.get('year');
        }} else if (localStorage.getItem('cbse_year')) {{
          state.selectedYear = localStorage.getItem('cbse_year');
        }}

        if (urlParams.has('type')) {{
          state.selectedType = urlParams.get('type');
        }} else if (localStorage.getItem('cbse_type')) {{
          state.selectedType = localStorage.getItem('cbse_type');
        }}

        if (urlParams.has('status')) {{
          state.selectedStudyStatus = urlParams.get('status');
        }} else if (localStorage.getItem('cbse_study_status')) {{
          state.selectedStudyStatus = localStorage.getItem('cbse_study_status');
        }}

        if (urlParams.has('sort')) {{
          state.sortBy = urlParams.get('sort');
        }} else if (localStorage.getItem('cbse_sort_by')) {{
          state.sortBy = localStorage.getItem('cbse_sort_by');
        }}

        if (urlParams.has('paired')) {{
          state.pairedOnly = urlParams.get('paired') === '1' || urlParams.get('paired') === 'true';
        }} else if (localStorage.getItem('cbse_paired_only') !== null) {{
          state.pairedOnly = localStorage.getItem('cbse_paired_only') === 'true';
        }}

        if (urlParams.has('view')) {{
          state.viewMode = urlParams.get('view');
        }} else if (localStorage.getItem('cbse_view_mode')) {{
          state.viewMode = localStorage.getItem('cbse_view_mode');
        }}

        if (urlParams.has('q')) {{
          state.searchQuery = urlParams.get('q');
        }}

        if (urlParams.has('split')) {{
          state.splitPercent = parseFloat(urlParams.get('split'));
        }} else if (localStorage.getItem('cbse_split_percent')) {{
          state.splitPercent = parseFloat(localStorage.getItem('cbse_split_percent'));
        }}

        if (urlParams.has('tab')) {{
          state.activeMobileTab = urlParams.get('tab');
        }} else if (localStorage.getItem('cbse_active_mobile_tab')) {{
          state.activeMobileTab = localStorage.getItem('cbse_active_mobile_tab');
        }}
      }}

      function syncFilterControls() {{
        if (dom.studyStatusFilter) dom.studyStatusFilter.value = state.selectedStudyStatus;
        if (dom.sortSelect) dom.sortSelect.value = state.sortBy;
        if (dom.pairedOnlyToggle) dom.pairedOnlyToggle.checked = state.pairedOnly;
        if (dom.viewModeIcon) dom.viewModeIcon.textContent = state.viewMode === 'grid' ? '⊞' : '☰';

        document.querySelectorAll('.subject-pill').forEach(pill => {{
          if (pill.getAttribute('data-subject') === state.selectedSubject) {{
            pill.classList.add('active');
            try {{ pill.scrollIntoView({{ inline: 'nearest', block: 'nearest' }}); }} catch (e) {{}}
          }} else {{
            pill.classList.remove('active');
          }}
        }});

        dom.yearChipGroup.querySelectorAll('.chip').forEach(chip => {{
          if (chip.getAttribute('data-year') === state.selectedYear) {{
            chip.classList.add('active');
          }} else {{
            chip.classList.remove('active');
          }}
        }});

        dom.typeChipGroup.querySelectorAll('.chip').forEach(chip => {{
          if (chip.getAttribute('data-type') === state.selectedType) {{
            chip.classList.add('active');
          }} else {{
            chip.classList.remove('active');
          }}
        }});
      }}

      function restoreOpenDocuments() {{
        const urlParams = getUrlParams();
        const docIdFromUrl = urlParams.get('doc');
        const docIdFromStorage = localStorage.getItem('cbse_workbench_open') === 'true' 
          ? localStorage.getItem('cbse_active_doc_id') 
          : null;

        const targetDocId = docIdFromUrl || docIdFromStorage;

        if (targetDocId) {{
          const rightId = urlParams.get('right') || (localStorage.getItem('cbse_is_split') === 'true' ? localStorage.getItem('cbse_active_right_id') : null);
          const isSplit = !!rightId;
          if (urlParams.get('split')) {{
            state.splitPercent = parseFloat(urlParams.get('split'));
          }} else if (localStorage.getItem('cbse_split_percent')) {{
            state.splitPercent = parseFloat(localStorage.getItem('cbse_split_percent'));
          }}
          openWorkbench(targetDocId, isSplit, false, rightId);
          return;
        }}

        if (urlParams.get('map') === '1' || localStorage.getItem('cbse_map_open') === 'true') {{
          openMapModal(false);
        }}

        if (urlParams.get('datesheet') === '1' || localStorage.getItem('cbse_datesheet_open') === 'true') {{
          openDatesheetModal(false);
        }}
      }}

      // Save & Update Completed Documents
      function saveCompletedDocs() {{
        localStorage.setItem('cbse_completed_docs', JSON.stringify(Array.from(state.completedDocs)));
        updateProgressMetrics();
      }}

      function toggleDocCompletion(id) {{
        if (state.completedDocs.has(id)) {{
          state.completedDocs.delete(id);
        }} else {{
          state.completedDocs.add(id);
        }}
        saveCompletedDocs();
        renderMaterials();
        updateWorkbenchDoneBtn();
      }}

      function updateProgressMetrics() {{
        const total = state.allMaterials.length;
        const completedCount = state.completedDocs.size;
        const pct = total > 0 ? ((completedCount / total) * 100).toFixed(1) : 0;

        dom.progressSummaryText.textContent = `${{completedCount}} / ${{total}} (${{pct}}%)`;
        dom.progressBarFill.style.width = `${{pct}}%`;

        dom.studyStatusFilter.options[0].textContent = `Status: All (${{total}})`;
        dom.studyStatusFilter.options[1].textContent = `Status: ⬜ Unfinished (${{total - completedCount}})`;
        dom.studyStatusFilter.options[2].textContent = `Status: ✅ Completed (${{completedCount}})`;
      }}

      // PDF URL Resolver (Always official GitHub Raw via Mozilla PDF.js viewer)
      function getRawPdfUrl(relPath) {{
        return `https://raw.githubusercontent.com/${{GITHUB_USER}}/${{GITHUB_REPO}}/${{GITHUB_BRANCH}}/${{encodeURI(relPath)}}`;
      }}

      function buildViewerUrl(relPath) {{
        const rawUrl = getRawPdfUrl(relPath);
        return `${{MOZILLA_VIEWER_BASE}}?file=${{encodeURIComponent(rawUrl)}}`;
      }}

      // Theme toggle
      function applyTheme(theme) {{
        document.documentElement.setAttribute('data-theme', theme);
        dom.themeIcon.textContent = theme === 'dark' ? '☀️' : '🌙';
        dom.bottomNavThemeIcon.textContent = theme === 'dark' ? '☀️' : '🌙';
        localStorage.setItem('cbse_theme', theme);
        state.theme = theme;
      }}
      applyTheme(state.theme);

      dom.themeToggleBtn.addEventListener('click', () => {{
        applyTheme(state.theme === 'dark' ? 'light' : 'dark');
      }});
      dom.bottomNavTheme.addEventListener('click', () => {{
        applyTheme(state.theme === 'dark' ? 'light' : 'dark');
      }});

      // Mobile Drawer Controls
      function openDrawer() {{
        dom.sidebarDrawer.classList.add('drawer-open');
        dom.drawerBackdrop.classList.add('active');
        document.body.style.overflow = 'hidden';
      }}

      function closeDrawer() {{
        dom.sidebarDrawer.classList.remove('drawer-open');
        dom.drawerBackdrop.classList.remove('active');
        document.body.style.overflow = '';
      }}

      dom.mobileDrawerBtn.addEventListener('click', openDrawer);
      dom.closeDrawerBtn.addEventListener('click', closeDrawer);
      dom.drawerBackdrop.addEventListener('click', closeDrawer);
      dom.bottomNavFilters.addEventListener('click', openDrawer);

      dom.bottomNavTop.addEventListener('click', () => {{
        dom.stageScrollArea.scrollTo({{ top: 0, behavior: 'smooth' }});
      }});

      // Render Categories
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
            localStorage.setItem('cbse_category', state.selectedCategory);
            updateUrl(false);
            renderCategoryNav();
            renderMaterials();
            if (window.innerWidth <= 900) closeDrawer();
          }});
          dom.categoryNavList.appendChild(div);
        }});
      }}

      // Filter Logic
      function getFilteredMaterials() {{
        return state.allMaterials.filter(m => {{
          if (m.type === 'cover_image') return false;

          if (state.selectedSubject !== 'All' && m.subject !== state.selectedSubject) return false;
          if (state.selectedCategory !== 'All' && m.category !== state.selectedCategory) return false;
          if (state.selectedYear !== 'All' && m.year !== state.selectedYear) return false;
          if (state.selectedType !== 'All' && m.type !== state.selectedType) return false;
          if (state.pairedOnly && !m.paired_id) return false;

          // Study Completion Status Filter
          const isDone = state.completedDocs.has(m.id);
          if (state.selectedStudyStatus === 'unfinished' && isDone) return false;
          if (state.selectedStudyStatus === 'completed' && !isDone) return false;

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

      function renderMaterials() {{
        const items = getFilteredMaterials();
        dom.resultsCountBadge.textContent = `${{items.length}} items`;

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
              <div style="grid-column: 1/-1; text-align: center; padding: 50px 16px; color: var(--text-muted);">
                <div style="font-size: 32px; margin-bottom: 12px;">🔍</div>
                <div style="font-size: 16px; font-weight: 600; color: var(--text-secondary);">No documents match your filters</div>
                <div style="font-size: 13px; margin-top: 6px;">Try adjusting filters or clearing status filters</div>
              </div>
            `;
            return;
          }}

          items.forEach(item => {{
            const card = document.createElement('div');
            const isCompleted = state.completedDocs.has(item.id);
            card.className = `card ${{item.paired_id ? 'paired' : ''}} ${{isCompleted ? 'is-completed' : ''}}`;

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
                  ${{isCompleted ? `<span class="tag tag-completed">✔ Completed</span>` : ''}}
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
                <button class="btn btn-done toggle-done-btn ${{isCompleted ? 'done' : ''}}" data-id="${{item.id}}" title="Toggle complete status">
                  ${{isCompleted ? '✅ Done' : '⬜ Mark Done'}}
                </button>
                <a href="${{getRawPdfUrl(item.rel_path)}}" target="_blank" download class="btn btn-secondary" title="Download file">⬇</a>
              </div>
            `;

            dom.materialsGrid.appendChild(card);
          }});
        }} else {{
          dom.materialsGrid.style.display = 'none';
          dom.materialsTable.style.display = 'table';
          dom.materialsTableBody.innerHTML = '';

          items.forEach(item => {{
            const isCompleted = state.completedDocs.has(item.id);
            const tr = document.createElement('tr');
            tr.innerHTML = `
              <td>
                <button class="btn btn-done toggle-done-btn ${{isCompleted ? 'done' : ''}}" data-id="${{item.id}}" style="padding: 2px 6px; font-size: 10px;">
                  ${{isCompleted ? '✅' : '⬜'}}
                </button>
              </td>
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
                  <a href="${{getRawPdfUrl(item.rel_path)}}" target="_blank" download class="btn btn-secondary" style="padding: 4px 8px; font-size: 11px;">⬇</a>
                </div>
              </td>
            `;
            dom.materialsTableBody.appendChild(tr);
          }});
        }}

        // Card button events
        document.querySelectorAll('.open-split-btn').forEach(b => {{
          b.addEventListener('click', (e) => {{
            const id = e.currentTarget.getAttribute('data-id');
            openWorkbench(id, true, true);
          }});
        }});

        document.querySelectorAll('.open-single-btn').forEach(b => {{
          b.addEventListener('click', (e) => {{
            const id = e.currentTarget.getAttribute('data-id');
            openWorkbench(id, false, true);
          }});
        }});

        document.querySelectorAll('.toggle-done-btn').forEach(b => {{
          b.addEventListener('click', (e) => {{
            const id = e.currentTarget.getAttribute('data-id');
            toggleDocCompletion(id);
          }});
        }});
      }}

      // ============================================================
      // WORKBENCH LOGIC (MOZILLA PDF.JS VIEWER INTEGRATED)
      // ============================================================
      function updateWorkbenchDoneBtn() {{
        if (!state.activeLeftItem) return;
        const isDone = state.completedDocs.has(state.activeLeftItem.id);
        dom.workbenchMarkDoneBtn.textContent = isDone ? '✅ Completed' : '⬜ Mark Complete';
        if (isDone) dom.workbenchMarkDoneBtn.classList.add('done');
        else dom.workbenchMarkDoneBtn.classList.remove('done');
      }}

      dom.workbenchMarkDoneBtn.addEventListener('click', () => {{
        if (state.activeLeftItem) {{
          toggleDocCompletion(state.activeLeftItem.id);
        }}
      }});

      function applySplitPercent(pct) {{
        pct = Math.max(15, Math.min(85, pct));
        state.splitPercent = pct;
        dom.leftPane.style.width = pct.toFixed(2) + '%';
        dom.rightPane.style.width = (100 - pct).toFixed(2) + '%';
      }}

      function openWorkbench(itemId, isSplit, pushHistory = true, rightItemId = null) {{
        const primary = state.allMaterials.find(m => m.id === itemId);
        if (!primary) return;

        state.activeLeftItem = primary;
        dom.leftDocTitle.textContent = primary.title;
        dom.leftIframe.src = buildViewerUrl(primary.rel_path);

        updateWorkbenchDoneBtn();

        const hasPair = !!primary.paired_id;
        const isMobile = window.innerWidth <= 640;

        let shouldSplit = false;
        if (rightItemId) {{
          const specifiedRight = state.allMaterials.find(m => m.id === rightItemId);
          if (specifiedRight) {{
            state.activeRightItem = specifiedRight;
            shouldSplit = true;
          }}
        }} else if (isSplit && hasPair) {{
          const paired = state.allMaterials.find(m => m.id === primary.paired_id);
          if (paired) {{
            state.activeRightItem = paired;
            shouldSplit = true;
          }}
        }}

        if (hasPair) {{
          dom.toggleSplitViewBtn.style.display = 'inline-flex';
          populateCompanionDropdown(primary);
        }} else {{
          dom.toggleSplitViewBtn.style.display = 'none';
        }}

        if (shouldSplit && state.activeRightItem) {{
          // Dual-Pane Split Mode
          dom.splitWorkbench.classList.add('is-split');
          dom.toggleSplitViewBtn.textContent = '🗖 Single View';
          dom.toggleSplitViewBtn.className = 'btn btn-secondary';

          dom.rightDocTitle.textContent = state.activeRightItem.title;
          dom.rightIframe.src = buildViewerUrl(state.activeRightItem.rel_path);
          if (dom.companionSelector) dom.companionSelector.value = state.activeRightItem.id;

          if (isMobile) {{
            switchMobileTab(state.activeMobileTab || 'left');
          }} else {{
            const savedPct = parseFloat(localStorage.getItem('cbse_split_percent')) || 50;
            applySplitPercent(savedPct);
          }}
        }} else {{
          // Single View Mode (100% full width, no division)
          state.activeRightItem = null;
          dom.splitWorkbench.classList.remove('is-split');
          if (hasPair) {{
            dom.toggleSplitViewBtn.textContent = '⚡ Split View (QP + MS)';
            dom.toggleSplitViewBtn.className = 'btn btn-split';
          }}
          dom.rightIframe.src = 'about:blank';
          dom.leftPane.style.width = '100%';
          dom.rightPane.style.width = '0%';
        }}

        dom.splitWorkbench.classList.add('active');
        document.body.style.overflow = 'hidden';

        // Persist to localStorage
        localStorage.setItem('cbse_workbench_open', 'true');
        localStorage.setItem('cbse_active_doc_id', primary.id);
        if (state.activeRightItem) {{
          localStorage.setItem('cbse_active_right_id', state.activeRightItem.id);
        }} else {{
          localStorage.removeItem('cbse_active_right_id');
        }}
        localStorage.setItem('cbse_is_split', shouldSplit ? 'true' : 'false');

        // Synchronize URL
        updateUrl(pushHistory);
      }}

      function switchMobileTab(tab) {{
        state.activeMobileTab = tab;
        localStorage.setItem('cbse_active_mobile_tab', tab);
        updateUrl(false);
        if (tab === 'left') {{
          dom.mobileTabLeft.classList.add('active');
          dom.mobileTabRight.classList.remove('active');
          dom.leftPane.style.width = '100%';
          dom.leftPane.style.display = 'flex';
          dom.rightPane.style.width = '0%';
          dom.rightPane.style.display = 'none';
          dom.mobileFlipBtn.textContent = '⚡ Switch to Solution ➔';
        }} else {{
          dom.mobileTabRight.classList.add('active');
          dom.mobileTabLeft.classList.remove('active');
          dom.rightPane.style.width = '100%';
          dom.rightPane.style.display = 'flex';
          dom.leftPane.style.width = '0%';
          dom.leftPane.style.display = 'none';
          dom.mobileFlipBtn.textContent = '⬅ Back to Question Paper';
        }}
      }}

      dom.mobileTabLeft.addEventListener('click', () => switchMobileTab('left'));
      dom.mobileTabRight.addEventListener('click', () => switchMobileTab('right'));
      dom.mobileFlipBtn.addEventListener('click', () => {{
        switchMobileTab(state.activeMobileTab === 'left' ? 'right' : 'left');
      }});

      function populateCompanionDropdown(primary) {{
        dom.companionSelector.innerHTML = '';

        if (primary.paired_id) {{
          const opt = document.createElement('option');
          opt.value = primary.paired_id;
          opt.textContent = `🎯 Paired: ${{primary.paired_title || 'Official Marking Scheme'}}`;
          dom.companionSelector.appendChild(opt);
        }}

        const toppers = state.allMaterials.filter(m => m.type === 'topper_script' && m.subject === primary.subject);
        toppers.forEach(t => {{
          const opt = document.createElement('option');
          opt.value = t.id;
          opt.textContent = `🏆 ${{t.title}}`;
          dom.companionSelector.appendChild(opt);
        }});

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
          dom.rightIframe.src = buildViewerUrl(targetDoc.rel_path);
          localStorage.setItem('cbse_active_right_id', targetDoc.id);
          updateUrl(false);
          if (window.innerWidth <= 640) switchMobileTab('right');
          else applySplitPercent(state.splitPercent || 50);
        }}
      }});

      dom.toggleSplitViewBtn.addEventListener('click', () => {{
        if (!state.activeLeftItem || !state.activeLeftItem.paired_id) return;
        const currentlySplit = dom.splitWorkbench.classList.contains('is-split');
        openWorkbench(state.activeLeftItem.id, !currentlySplit, false);
      }});

      function closeWorkbench(updateHistory = true) {{
        dom.splitWorkbench.classList.remove('active');
        dom.splitWorkbench.classList.remove('is-split');
        dom.leftIframe.src = 'about:blank';
        dom.rightIframe.src = 'about:blank';
        document.body.style.overflow = '';

        state.activeLeftItem = null;
        state.activeRightItem = null;

        localStorage.setItem('cbse_workbench_open', 'false');
        localStorage.removeItem('cbse_active_doc_id');
        localStorage.removeItem('cbse_active_right_id');
        localStorage.removeItem('cbse_is_split');

        if (updateHistory) {{
          updateUrl(false);
        }}
      }}

      dom.closeWorkbenchBtn.addEventListener('click', () => closeWorkbench(true));

      dom.splitPreset50.addEventListener('click', () => {{
        applySplitPercent(50);
        localStorage.setItem('cbse_split_percent', '50');
        updateUrl(false);
      }});

      dom.splitPresetLeft.addEventListener('click', () => {{
        applySplitPercent(70);
        localStorage.setItem('cbse_split_percent', '70');
        updateUrl(false);
      }});

      dom.splitPresetRight.addEventListener('click', () => {{
        applySplitPercent(30);
        localStorage.setItem('cbse_split_percent', '30');
        updateUrl(false);
      }});

      dom.swapPanesBtn.addEventListener('click', () => {{
        if (!state.activeLeftItem || !state.activeRightItem) return;
        const temp = state.activeLeftItem;
        state.activeLeftItem = state.activeRightItem;
        state.activeRightItem = temp;

        dom.leftDocTitle.textContent = state.activeLeftItem.title;
        dom.leftIframe.src = buildViewerUrl(state.activeLeftItem.rel_path);

        dom.rightDocTitle.textContent = state.activeRightItem.title;
        dom.rightIframe.src = buildViewerUrl(state.activeRightItem.rel_path);

        localStorage.setItem('cbse_active_doc_id', state.activeLeftItem.id);
        localStorage.setItem('cbse_active_right_id', state.activeRightItem.id);
        updateUrl(false);

        updateWorkbenchDoneBtn();
      }});

      // Draggable Split Divider Resizing
      let isDraggingDivider = false;

      function onDividerPointerDown(e) {{
        if (!state.activeRightItem || !dom.splitWorkbench.classList.contains('is-split')) return;
        isDraggingDivider = true;
        dom.paneDivider.classList.add('is-dragging');
        dom.workbenchBody.classList.add('is-resizing');
        try {{
          dom.paneDivider.setPointerCapture(e.pointerId);
        }} catch (err) {{}}
        e.preventDefault();
      }}

      function onDividerPointerMove(e) {{
        if (!isDraggingDivider) return;
        const rect = dom.workbenchBody.getBoundingClientRect();
        if (rect.width <= 0) return;
        const offsetPx = e.clientX - rect.left;
        let pct = (offsetPx / rect.width) * 100;
        applySplitPercent(pct);
      }}

      function onDividerPointerUp(e) {{
        if (!isDraggingDivider) return;
        isDraggingDivider = false;
        dom.paneDivider.classList.remove('is-dragging');
        dom.workbenchBody.classList.remove('is-resizing');
        try {{
          dom.paneDivider.releasePointerCapture(e.pointerId);
        }} catch (err) {{}}
        if (state.splitPercent) {{
          localStorage.setItem('cbse_split_percent', state.splitPercent.toFixed(1));
          updateUrl(false);
        }}
      }}

      dom.paneDivider.addEventListener('pointerdown', onDividerPointerDown);
      dom.paneDivider.addEventListener('pointermove', onDividerPointerMove);
      dom.paneDivider.addEventListener('pointerup', onDividerPointerUp);
      dom.paneDivider.addEventListener('pointercancel', onDividerPointerUp);

      dom.popoutBtn.addEventListener('click', () => {{
        if (state.activeLeftItem) window.open(buildViewerUrl(state.activeLeftItem.rel_path), '_blank');
        if (state.activeRightItem && dom.splitWorkbench.classList.contains('is-split')) {{
          window.open(buildViewerUrl(state.activeRightItem.rel_path), '_blank');
        }}
      }});

      // Omni-Search
      function openOmniSearch() {{
        dom.searchModal.classList.add('active');
        dom.omniSearchInput.value = '';
        renderOmniResults('');
        dom.omniSearchInput.focus();
        document.body.style.overflow = 'hidden';
      }}

      function closeOmniSearch() {{
        dom.searchModal.classList.remove('active');
        document.body.style.overflow = '';
      }}

      dom.openOmniSearch.addEventListener('click', openOmniSearch);
      dom.bottomNavSearch.addEventListener('click', openOmniSearch);
      dom.closeSearchModalBtn.addEventListener('click', closeOmniSearch);

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
          const isDone = state.completedDocs.has(m.id);
          const item = document.createElement('div');
          item.className = `search-result-item ${{idx === 0 ? 'highlighted' : ''}}`;
          item.innerHTML = `
            <div style="display: flex; align-items: center; gap: 8px; overflow: hidden; min-width: 0;">
              <span class="tag ${{getSubjectTagClass(m.subject)}}" style="font-size: 9px;">${{m.subject}}</span>
              <div style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">
                <div style="font-weight: 600; color: var(--text-primary); font-size: 13px;">${{m.title}}</div>
                <div style="font-size: 11px; color: var(--text-muted); font-family: var(--font-mono);">${{m.rel_path}}</div>
              </div>
            </div>
            <div style="display: flex; align-items: center; gap: 6px; flex-shrink: 0;">
              ${{isDone ? `<span style="font-size: 10px; color: var(--accent-emerald);">✔ Done</span>` : ''}}
              ${{m.paired_id ? `<span style="font-size: 10px; color: var(--accent-emerald); font-weight: 700;">⚡ Paired</span>` : ''}}
              <span class="tag tag-year">${{m.year || 'Doc'}}</span>
            </div>
          `;
          item.addEventListener('click', () => {{
            closeOmniSearch();
            openWorkbench(m.id, !!m.paired_id, true);
          }});
          dom.searchResultsList.appendChild(item);
        }});
      }}

      dom.omniSearchInput.addEventListener('input', (e) => {{
        renderOmniResults(e.target.value);
      }});

      window.addEventListener('keydown', (e) => {{
        if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {{
          e.preventDefault();
          if (dom.searchModal.classList.contains('active')) closeOmniSearch();
          else openOmniSearch();
        }}
        if (e.key === 'Escape') {{
          if (dom.searchModal.classList.contains('active')) closeOmniSearch();
          if (dom.splitWorkbench.classList.contains('active')) closeWorkbench(true);
          if (dom.mapModal.classList.contains('active')) closeMapModal(true);
          if (dom.datesheetModal && dom.datesheetModal.classList.contains('active')) closeDatesheetModal(true);
          closeDrawer();
        }}
      }});

      dom.searchModal.addEventListener('click', (e) => {{
        if (e.target === dom.searchModal) closeOmniSearch();
      }});

      // Map Work Markdown parser
      function parseMarkdownToHtml(md) {{
        let html = md
          .replace(/^### (.*$)/gim, '<h3>$1</h3>')
          .replace(/^## (.*$)/gim, '<h2>$1</h2>')
          .replace(/^# (.*$)/gim, '<h1>$1</h1>')
          .replace(/\\*\\*(.*?)\\*\\*/gim, '<strong>$1</strong>')
          .replace(/\\*(.*?)\\*/gim, '<em>$1</em>');

        const lines = html.split('\\n');
        let inTable = false;
        let tableHtml = '';
        let parsedLines = [];

        for (let i = 0; i < lines.length; i++) {{
          const line = lines[i].trim();
          if (line.startsWith('|') && line.endsWith('|')) {{
            if (!inTable) {{
              inTable = true;
              tableHtml = '<div class="map-table-wrap"><table><thead>';
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
              tableHtml += '</tbody></table></div>';
              parsedLines.push(tableHtml);
              tableHtml = '';
            }}
            parsedLines.push(line);
          }}
        }}
        if (inTable) {{
          tableHtml += '</tbody></table></div>';
          parsedLines.push(tableHtml);
        }}

        return parsedLines.join('<br>');
      }}

      function openMapModal(pushHistory = true) {{
        dom.mapContentArea.innerHTML = parseMarkdownToHtml(window.__MAP_GUIDE_MD__);
        dom.mapModal.classList.add('active');
        document.body.style.overflow = 'hidden';
        localStorage.setItem('cbse_map_open', 'true');
        updateUrl(pushHistory);
      }}

      function closeMapModal(updateHistory = true) {{
        dom.mapModal.classList.remove('active');
        document.body.style.overflow = '';
        localStorage.setItem('cbse_map_open', 'false');
        if (updateHistory) {{
          updateUrl(false);
        }}
      }}

      dom.openMapWorkBtn.addEventListener('click', () => openMapModal(true));
      dom.bottomNavMap.addEventListener('click', () => openMapModal(true));

      dom.closeMapModalBtn.addEventListener('click', () => closeMapModal(true));
      dom.mapModal.addEventListener('click', (e) => {{
        if (e.target === dom.mapModal) {{
          closeMapModal(true);
        }}
      }});

      // Filter Handlers
      dom.subjectBar.addEventListener('click', (e) => {{
        const pill = e.target.closest('.subject-pill');
        if (!pill) return;
        document.querySelectorAll('.subject-pill').forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        state.selectedSubject = pill.getAttribute('data-subject');
        localStorage.setItem('cbse_subject', state.selectedSubject);
        updateUrl(false);
        renderMaterials();
      }});

      dom.yearChipGroup.addEventListener('click', (e) => {{
        const chip = e.target.closest('.chip');
        if (!chip) return;
        dom.yearChipGroup.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        state.selectedYear = chip.getAttribute('data-year');
        localStorage.setItem('cbse_year', state.selectedYear);
        updateUrl(false);
        renderMaterials();
        if (window.innerWidth <= 900) closeDrawer();
      }});

      dom.typeChipGroup.addEventListener('click', (e) => {{
        const chip = e.target.closest('.chip');
        if (!chip) return;
        dom.typeChipGroup.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        state.selectedType = chip.getAttribute('data-type');
        localStorage.setItem('cbse_type', state.selectedType);
        updateUrl(false);
        renderMaterials();
        if (window.innerWidth <= 900) closeDrawer();
      }});

      dom.studyStatusFilter.addEventListener('change', (e) => {{
        state.selectedStudyStatus = e.target.value;
        localStorage.setItem('cbse_study_status', state.selectedStudyStatus);
        updateUrl(false);
        renderMaterials();
      }});

      dom.pairedOnlyToggle.addEventListener('change', (e) => {{
        state.pairedOnly = e.target.checked;
        localStorage.setItem('cbse_paired_only', state.pairedOnly);
        updateUrl(false);
        renderMaterials();
      }});

      dom.sortSelect.addEventListener('change', (e) => {{
        state.sortBy = e.target.value;
        localStorage.setItem('cbse_sort_by', state.sortBy);
        updateUrl(false);
        renderMaterials();
      }});

      dom.viewModeToggle.addEventListener('click', () => {{
        state.viewMode = state.viewMode === 'grid' ? 'table' : 'grid';
        dom.viewModeIcon.textContent = state.viewMode === 'grid' ? '⊞' : '☰';
        localStorage.setItem('cbse_view_mode', state.viewMode);
        updateUrl(false);
        renderMaterials();
      }});

      // Browser History PopState & HashChange Navigation
      function onHistoryNavigation() {{
        const params = getUrlParams();

        state.selectedSubject = params.get('subject') || 'All';
        state.selectedCategory = params.get('category') || 'All';
        state.selectedYear = params.get('year') || 'All';
        state.selectedType = params.get('type') || 'All';
        state.selectedStudyStatus = params.get('status') || 'all';
        state.sortBy = params.get('sort') || 'year_desc';
        state.pairedOnly = params.get('paired') === '1' || params.get('paired') === 'true';
        state.viewMode = params.get('view') || 'grid';
        state.searchQuery = params.get('q') || '';

        syncFilterControls();
        renderCategoryNav();
        renderMaterials();

        const docId = params.get('doc');
        if (docId) {{
          const rightId = params.get('right');
          const isSplit = !!rightId;
          if (params.get('split')) state.splitPercent = parseFloat(params.get('split'));
          if (params.get('tab')) state.activeMobileTab = params.get('tab');
          if (!dom.splitWorkbench.classList.contains('active') || !state.activeLeftItem || state.activeLeftItem.id !== docId || dom.splitWorkbench.classList.contains('is-split') !== isSplit) {{
            openWorkbench(docId, isSplit, false, rightId);
          }}
        }} else {{
          if (dom.splitWorkbench.classList.contains('active')) {{
            closeWorkbench(false);
          }}
        }}

        if (params.get('map') === '1') {{
          if (!dom.mapModal.classList.contains('active')) {{
            openMapModal(false);
          }}
        }} else {{
          if (dom.mapModal.classList.contains('active')) {{
            closeMapModal(false);
          }}
        }}

        if (params.get('datesheet') === '1') {{
          if (dom.datesheetModal && !dom.datesheetModal.classList.contains('active')) {{
            openDatesheetModal(false);
          }}
        }} else {{
          if (dom.datesheetModal && dom.datesheetModal.classList.contains('active')) {{
            closeDatesheetModal(false);
          }}
        }}
      }}

      window.addEventListener('popstate', onHistoryNavigation);
      window.addEventListener('hashchange', onHistoryNavigation);

      // Initial Bootstrap
      initNavigationAndState();
      syncFilterControls();
      renderCategoryNav();
      updateProgressMetrics();
      renderMaterials();
      restoreOpenDocuments();
      updateUrl(false);

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
        print(f"Website successfully compiled to {target} ({len(html_content)} bytes)")

if __name__ == "__main__":
    build()

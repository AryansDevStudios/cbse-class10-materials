# ⚡ CBSE Class 10 Academic Command Center

A high-performance, dark/light mode interactive academic portal and digital vault built for **CBSE Class 10**. Inspired by Linear, Raycast, and modern developer documentation systems.

---

## 🚀 Quick Start

### Option A: Local Streaming Server (Recommended)
Run the bundled streaming Python server (features HTTP Byte-Ranges for instant large PDF scrolling and auto-opens your browser):
```bash
python serve.py
```
Open **[http://localhost:5050](http://localhost:5050)** in any browser.

### Option B: Direct Offline Double-Click
You can also directly double-click **`index.html`** in Windows Explorer. All 896 resource records are pre-embedded for zero-friction 100% offline usage!

---

## 💎 Key Features

### 1. ⚡ Dual-Pane Synchronized Split Viewer (The Standout Feature)
- Click **"⚡ Split View (QP + MS)"** on any paired past board paper, sample question paper, or practice paper.
- **Left Pane**: Question Paper with zoom, page navigation, and download.
- **Right Pane**: Official CBSE Marking Scheme / Solution key.
- **Companion Switcher**: Switch the right pane to authentic **Topper Handwritten Answer Scripts** (2022–2025) or Exemplar Solutions with a single click.
- **Layout Presets**: Instant toggle between `50/50 Split`, `Left Focus (100%)`, `Right Focus (100%)`, or `⇄ Swap Panes`.

### 2. 🔍 Global Omni-Search (`Ctrl + K` / `⌘K`)
- Press `Ctrl + K` anywhere to bring up the Raycast/Linear-style command palette.
- Real-time instant search across series codes (e.g. `30-1-1`, `2-1-1`, `311`), subjects, years, and categories.
- Keyboard navigation: use `↑` and `↓` arrow keys and press `Enter` to preview immediately.

### 3. 🏷️ Subject & Category Hierarchy Tree
- **Subject Bar**: One-click filtering across Mathematics (Standard 041), Science, Social Science, English (L&L), Hindi (Course A), and Information Technology (IT 402).
- **Sidebar Categories**:
  - 📜 **Board Examination Papers** (2022–2024, all sets and marking schemes)
  - 📝 **Sample Question Papers** (2023–2027 SQP + MS)
  - 🏆 **Topper Model Answers** (Handwritten All-India topper copies 2022–2025)
  - 📖 **NCERT Textbooks & Books** (Complete chapter-by-chapter library)
  - 💡 **NCERT Exemplar** (Problems & complete answer keys)
  - ✍️ **Additional Practice Questions** (CBSE practice sets & marking schemes)
  - 🧪 **Laboratory Manuals** (Science practicals Units 1 to 6)
  - 🎯 **Question Banks & Competency** (CBSE & British Council item banks)
  - 📋 **Syllabus & Curriculum 2027** (Latest blueprints and specifications)
  - 🗺️ **Interactive Map Work Guide** (Complete 5-mark guaranteed SST guide)

### 4. 📱 Mobile-First Experience & Thumb Navigation
- **Off-Canvas Filter Drawer**: Tap `☰` or the bottom `⚡ Filters` tab to slide out a clean drawer with categories, years, and document types.
- **Mobile Bottom Navigation Bar**: Quick-access thumb bar for `Search`, `Filters`, `Map Work`, `Theme`, and `Scroll to Top`.
- **Mobile Segmented Split Workbench**: Instead of cramped 50/50 panes on phones, automatically provides a full-width **Segmented Switcher** (`[ 📄 Question Paper ]` | `[ 🎯 Marking Scheme ]`) with a floating **`⚡ Switch to Solution ➔`** quick-flip button for rapid comparing without losing your scroll position!
- **Touch-Friendly Controls**: Generous tap targets (44px), inertia scrolling (`-webkit-overflow-scrolling: touch`), and safe-area insets for notched phones.

### 5. 🌓 Theme & View Density
- Toggle between sleek **Dark Theme** and crisp **Light Theme** (persisted in `localStorage`).
- Switch between **Grid Cards View** and **Compact Data Table View**.

---

## 🛠️ Rebuilding & Updating the Archive

If you add new PDF files or materials to the repository in the future:

1. **Re-generate the JSON Index**:
   ```bash
   python generate_index.py
   ```
2. **Re-build the Web Application**:
   ```bash
   python build_site.py
   ```

---

## 📁 Repository Structure
```text
D:\CBSE Materials\
├── index.html                   # Interactive Academic Command Center SPA
├── serve.py                     # Byte-range streaming HTTP server
├── generate_index.py            # Automated metadata crawler & QP/MS pairer
├── build_site.py                # Standalone site builder
├── cbse_materials_index.json    # Complete catalog index (896 items)
├── Board Examination Papers/    # 2022, 2023, 2024 (QP + MS sets)
├── Sample Question Papers/      # 2023 to 2027 (SQP + MS pairs)
├── Topper Model Answers/        # 2022 to 2025 handwritten copies
├── Books and Study Material/    # Full NCERT Textbooks
├── NCERT Exemplar/              # Class 10 Exemplar problems + answers
├── Additional Practice Questions/
├── Laboratory Manuals/          # Science practicals (Units 1-6)
├── Question Banks and Competency/
├── Syllabus and Curriculum 2027/
└── Map Work/                    # Complete SST Map Work guide
```

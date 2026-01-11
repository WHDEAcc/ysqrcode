# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

YanShu Restaurant (彦纾餐厅) - A fun, childlike landing page featuring a welcome screen with portrait, interactive menu gallery with futuristic transitions, and a custom Totoro QR code. Hosted on GitHub Pages.

**Live URL**: https://ysqrcode.pages.dev/

## Tech Stack

- Pure HTML/CSS/JavaScript (no frameworks)
- Python 3 for QR code generation (`qrcode` + `Pillow`)

## Development Commands

### QR Code Generation
```bash
# Regenerate Totoro QR code (outputs to images/qrcode-totoro.png)
python generate_qr.py
```

**Dependencies for QR generation**:
```bash
pip install qrcode pillow
```

### Local Development
```bash
# Serve locally (any static file server works)
python -m http.server 8000
```

### Deploy to GitHub Pages
```bash
# One-command deploy: add, commit, and push all changes
git add -A && git commit -m "Update site" && git push
```

## Architecture

### Frontend (`index.html`)
Single-page application with two main views:
1. **Welcome Screen** - Full-screen overlay with portrait, animated entrance, dismissible via button/keyboard/tap
2. **Menu Gallery** - Image carousel with 8 menu pages

Key JavaScript functions:
- `enterGallery()` - Transitions from welcome to gallery
- `goToImage(index)` - Handles image switching
- Touch/swipe and keyboard navigation built-in

### QR Code Generator (`generate_qr.py`)
- `create_circular_photo(photo_path, size)` - Crops photo into a circle
- `generate_qr_with_photo(url, output_path, photo_path)` - Creates QR with high error correction (30%) and circular photo in center

### Image Assets (`images/`)
- `yangshuo-portrait.png` - Welcome screen portrait (also used in QR code center)
- `menu-0.jpg` through `menu-7.jpg` - Compressed JPEG menu images (9:16 aspect ratio)
- `qrcode-totoro.png` - Generated QR code with portrait

## Key Patterns

- Menu images are numbered sequentially (`menu-0.jpg` to `menu-7.jpg`). To add/remove pages, update both the image files and `totalImages` constant in `index.html`
- Uses `fonts.loli.net` (China-accessible mirror) instead of Google Fonts
- QR code URL is hardcoded in `generate_qr.py` (`URL` variable at top of file)
- All CSS animations and styles are inline in `index.html` (no external stylesheets)

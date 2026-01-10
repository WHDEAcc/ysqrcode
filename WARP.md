# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

YanShu Restaurant (彦纾餐厅) - A fun, childlike landing page featuring a welcome screen with portrait, interactive menu gallery with futuristic transitions, and a custom Totoro QR code. Hosted on GitHub Pages.

**Live URL**: https://whdeacc.github.io/ysqrcode/

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

## Architecture

### Frontend (`index.html`)
Single-page application with two main views:
1. **Welcome Screen** - Full-screen overlay with portrait, animated entrance, dismissible via button/keyboard/tap
2. **Menu Gallery** - Image carousel with 8 menu pages, futuristic CSS transitions (glitch effects, scan lines)

Key JavaScript functions:
- `enterGallery()` - Transitions from welcome to gallery
- `goToImage(index)` - Handles image transitions with animation locking
- Touch/swipe and keyboard navigation built-in

### QR Code Generator (`generate_qr.py`)
- `create_totoro_image(size)` - Programmatically draws Totoro character using PIL
- `generate_qr_with_totoro(url, output_path)` - Creates QR with high error correction (30%) to allow center logo embedding

### Image Assets (`images/`)
- `yangshuo-portrait.png` - Welcome screen portrait
- `menu-0.png` through `menu-7.png` - Menu page images (9:16 aspect ratio expected)
- `qrcode-totoro.png` - Generated QR code

## Key Patterns

- Menu images are numbered sequentially (`menu-0.png` to `menu-7.png`). To add/remove pages, update both the image files and `totalImages` constant in `index.html`
- QR code URL is hardcoded in `generate_qr.py` (`URL` variable at top of file)
- All CSS animations and styles are inline in `index.html` (no external stylesheets)

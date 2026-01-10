#!/usr/bin/env python3
"""
Generate a QR code in SVG format for 3D printing in Blender.
"""

import qrcode
import qrcode.image.svg
import os

# GitHub Pages URL
URL = "https://whdeacc.github.io/ysqrcode/"

def generate_qr_svg(url, output_path):
    """Generate a QR code as SVG file for Blender import."""
    
    # Create QR code with high error correction
    qr = qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # 30% error correction
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create SVG image (path-based for clean geometry)
    factory = qrcode.image.svg.SvgPathImage
    img = qr.make_image(image_factory=factory)
    
    # Save SVG
    img.save(output_path)
    print(f"SVG QR code saved to: {output_path}")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, "images", "qrcode-3d.svg")
    
    # Ensure images directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    print(f"Generating SVG QR code for: {URL}")
    generate_qr_svg(URL, output_path)
    print("Done!")
    print(f"\nImport this SVG into Blender for 3D extrusion.")

if __name__ == "__main__":
    main()

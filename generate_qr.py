#!/usr/bin/env python3
"""
Generate a QR code with a cute Totoro character in the center.
The QR code links to the GitHub Pages URL for YanShu Restaurant.
"""

import qrcode
from PIL import Image, ImageDraw
import os

# GitHub Pages URL (will be updated after deployment)
URL = "https://whdeacc.github.io/ysqrcode/"

def create_totoro_image(size=150):
    """Create a cute Totoro character image."""
    # Create a square image with transparent background
    img = Image.new('RGBA', (size, size), (255, 255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Colors
    body_color = (140, 150, 160)  # Gray-blue
    belly_color = (230, 230, 220)  # Cream
    nose_color = (60, 60, 60)  # Dark gray
    eye_white = (255, 255, 255)
    eye_black = (30, 30, 30)
    whisker_color = (80, 80, 80)
    
    # Scale factor
    s = size / 150
    
    # Body (rounded bottom shape)
    # Main body ellipse
    draw.ellipse([20*s, 25*s, 130*s, 140*s], fill=body_color)
    
    # Ears (two triangular shapes at top)
    # Left ear
    draw.polygon([(35*s, 35*s), (25*s, 5*s), (55*s, 25*s)], fill=body_color)
    # Right ear
    draw.polygon([(115*s, 35*s), (125*s, 5*s), (95*s, 25*s)], fill=body_color)
    
    # Ear inner (pink/cream)
    draw.polygon([(38*s, 30*s), (32*s, 12*s), (50*s, 25*s)], fill=(220, 180, 180))
    draw.polygon([(112*s, 30*s), (118*s, 12*s), (100*s, 25*s)], fill=(220, 180, 180))
    
    # Belly patch (cream colored, chevron pattern area)
    draw.ellipse([35*s, 55*s, 115*s, 130*s], fill=belly_color)
    
    # Belly markings (chevron shapes)
    for i, y_offset in enumerate([70, 85, 100]):
        if i < 3:
            # Draw small chevron marks
            y = y_offset * s
            for x_pos in [50, 65, 80, 95]:
                x = x_pos * s
                w = 8 * s
                h = 6 * s
                draw.polygon([
                    (x, y),
                    (x + w/2, y + h),
                    (x + w, y)
                ], fill=body_color)
    
    # Eyes (large white circles with black pupils)
    # Left eye
    draw.ellipse([40*s, 40*s, 65*s, 65*s], fill=eye_white, outline=nose_color, width=int(2*s))
    draw.ellipse([48*s, 45*s, 60*s, 58*s], fill=eye_black)
    draw.ellipse([52*s, 48*s, 56*s, 52*s], fill=eye_white)  # Highlight
    
    # Right eye
    draw.ellipse([85*s, 40*s, 110*s, 65*s], fill=eye_white, outline=nose_color, width=int(2*s))
    draw.ellipse([90*s, 45*s, 102*s, 58*s], fill=eye_black)
    draw.ellipse([94*s, 48*s, 98*s, 52*s], fill=eye_white)  # Highlight
    
    # Nose (small black triangle/oval in center)
    draw.ellipse([68*s, 55*s, 82*s, 68*s], fill=nose_color)
    
    # Whiskers (3 on each side)
    whisker_width = int(2*s)
    # Left whiskers
    draw.line([(30*s, 55*s), (10*s, 50*s)], fill=whisker_color, width=whisker_width)
    draw.line([(30*s, 62*s), (8*s, 62*s)], fill=whisker_color, width=whisker_width)
    draw.line([(30*s, 69*s), (10*s, 74*s)], fill=whisker_color, width=whisker_width)
    
    # Right whiskers
    draw.line([(120*s, 55*s), (140*s, 50*s)], fill=whisker_color, width=whisker_width)
    draw.line([(120*s, 62*s), (142*s, 62*s)], fill=whisker_color, width=whisker_width)
    draw.line([(120*s, 69*s), (140*s, 74*s)], fill=whisker_color, width=whisker_width)
    
    # Mouth (simple curved smile)
    # Using arc or simple lines
    draw.arc([60*s, 60*s, 90*s, 80*s], start=0, end=180, fill=nose_color, width=int(2*s))
    
    return img

def generate_qr_with_totoro(url, output_path):
    """Generate a QR code with Totoro in the center."""
    
    # Create QR code with high error correction (allows for center logo)
    qr = qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # 30% error correction
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create QR code image with nice colors
    qr_img = qr.make_image(fill_color="#2d3748", back_color="white").convert('RGBA')
    
    # Get QR code size
    qr_width, qr_height = qr_img.size
    
    # Create Totoro image (about 25% of QR code size for safe embedding)
    totoro_size = int(min(qr_width, qr_height) * 0.28)
    totoro = create_totoro_image(totoro_size)
    
    # Create white circular background for Totoro
    bg_size = int(totoro_size * 1.15)
    bg = Image.new('RGBA', (bg_size, bg_size), (255, 255, 255, 0))
    bg_draw = ImageDraw.Draw(bg)
    bg_draw.ellipse([0, 0, bg_size, bg_size], fill=(255, 255, 255, 255))
    
    # Calculate center position
    pos_bg = ((qr_width - bg_size) // 2, (qr_height - bg_size) // 2)
    pos_totoro = ((qr_width - totoro_size) // 2, (qr_height - totoro_size) // 2)
    
    # Paste white background circle first
    qr_img.paste(bg, pos_bg, bg)
    
    # Paste Totoro on top
    qr_img.paste(totoro, pos_totoro, totoro)
    
    # Save the result
    qr_img.save(output_path, 'PNG')
    print(f"QR code saved to: {output_path}")
    
    return qr_img

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, "images", "qrcode-totoro.png")
    
    # Ensure images directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    print(f"Generating QR code for: {URL}")
    generate_qr_with_totoro(URL, output_path)
    print("Done!")
    print(f"\nThe QR code links to: {URL}")
    print("After pushing to GitHub and enabling GitHub Pages, the QR code will work!")

if __name__ == "__main__":
    main()

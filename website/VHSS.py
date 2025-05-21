from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import random
import os
import datetime

def process_VHS_image(image: Image.Image) -> Image.Image:
# Resize and convert image
    image = image.convert("RGB")
    width, height = image.size

    # Add scan lines
    scanlined = image.copy()
    draw = ImageDraw.Draw(scanlined)
    for y in range(0, height, 2):
        draw.line((0, y, width, y), fill=(0, 0, 0), width=1)

    # Add noise overlay
    noise = Image.effect_noise((width, height), 16).convert("L")
    noise_rgb = Image.merge("RGB", (noise, noise, noise))
    image = Image.blend(scanlined, noise_rgb, alpha=0.2)

    # Apply RGB split (chromatic aberration)
    r, g, b = image.split()
    r = ImageChops.offset(r, -1, 0)
    b = ImageChops.offset(b, 1, 0)
    image = Image.merge("RGB", (r, g, b))

    # Load VHS-style font (you must have this in your static folder)
    font_path = os.path.join(os.path.dirname(__file__), "static", "vcr_osd_mono.ttf")
    font = ImageFont.truetype(font_path, 36)

    draw = ImageDraw.Draw(image)
    
    # Overlay VHS labels
    draw.text((20, 20), "PLAY", font=font, fill="white")
    draw.text((20, height - 60), "SP", font=font, fill="white")

    # Timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
    draw.text((width // 2 - 120, height - 60), timestamp, font=font, fill="white")

    # Optional: add horizontal glitch lines
    for i in range(5):
        glitch_y = random.randint(0, height - 10)
        glitch_height = random.randint(2, 5)
        box = (0, glitch_y, width, glitch_y + glitch_height)
        glitch_strip = image.crop(box)
        glitch_strip = ImageChops.offset(glitch_strip, random.randint(-20, 20), 0)
        image.paste(glitch_strip, (0, glitch_y))

            # Load and paste logo watermark
    logo_path = os.path.join(os.path.dirname(__file__), "static", "Logo.png")
    if os.path.exists(logo_path):
        logo = Image.open(logo_path).convert("RGBA")
        logo = logo.resize((64, 64))

        # Define bottom-right corner with padding
        logo_x = width - 64 - 20
        logo_y = height - 64 - 20

        image.paste(logo, (logo_x, logo_y), mask=logo)

    return image

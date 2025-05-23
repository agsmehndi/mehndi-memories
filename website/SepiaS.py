from PIL import Image
import os

def process_sepia_image(image: Image.Image) -> Image.Image:
    # Ensure the image is in RGB mode
    image = image.convert("RGB")
    width, height = image.size

    pixels = image.load()  # Access the pixel data

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            # Apply sepia formula
            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)

            # Clamp values to max 255
            pixels[x, y] = (
                min(tr, 255),
                min(tg, 255),
                min(tb, 255)
            )

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

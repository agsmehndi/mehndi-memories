from PIL import Image, ImageDraw, ImageFont
import os

def process_polaroid_image(image: Image.Image) -> Image.Image:
    current_dir = os.path.dirname(__file__)
    template_path = os.path.join(current_dir, 'static', 'PolaroidTemplate.png')
    template = Image.open(template_path).convert("RGBA")

    # Convert uploaded image to RGBA and resize to fit placeholder
    user_img = image.convert("RGBA")
    photo_box_size = (924, 924)  # Placeholder size in template
    user_img = user_img.resize(photo_box_size)

    # Coordinates where the user image should be placed on the template
    photo_position = (84, 35)

    # Paste the user image onto the template
    template.paste(user_img, photo_position, mask=user_img)

    return template

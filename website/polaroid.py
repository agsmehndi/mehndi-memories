from flask import Blueprint, render_template, request, redirect, url_for, send_file
from io import BytesIO
import base64
from PIL import Image
from website.PolaroidS import process_polaroid_image  # Import your custom script

polaroid = Blueprint('polaroid', __name__)

# Global temporary image buffer
processed_image_bytes = BytesIO()

@polaroid.route('/polaroid/en')
def polaroid_capture_en():
    return render_template('/Polaroid/PolaroidPicEn.html')

@polaroid.route('/polaroid/hi')
def polaroid_capture_hi():
    return render_template('/Polaroid/PolaroidPicHi.html')

@polaroid.route('/upload/polaroid/en', methods=['POST'])
def handle_polaroid_upload_en():
    global processed_image_bytes

    img_data = request.form['image_data']
    if ',' in img_data:
        img_data = img_data.split(',')[1]  # Remove data:image/png;base64,...
    img_bytes = base64.b64decode(img_data)
    img = Image.open(BytesIO(img_bytes))

    txt = request.form['text']
    print(txt)

    # Process the image using your custom script
    result_img = process_polaroid_image(img)  # This returns a PIL.Image object

    # Save result into memory
    processed_image_bytes = BytesIO()
    result_img.save(processed_image_bytes, format='PNG')
    processed_image_bytes.seek(0)

    return redirect(url_for('polaroid.polaroid_result_en'))

@polaroid.route('/upload/polaroid/hi', methods=['POST'])
def handle_polaroid_upload_hi():
    global processed_image_bytes

    img_data = request.form['image_data']
    if ',' in img_data:
        img_data = img_data.split(',')[1]  # Remove data:image/png;base64,...
    img_bytes = base64.b64decode(img_data)
    img = Image.open(BytesIO(img_bytes))

    # Process the image using your custom script
    result_img = process_polaroid_image(img)  # This returns a PIL.Image object

    # Save result into memory
    processed_image_bytes = BytesIO()
    result_img.save(processed_image_bytes, format='PNG')
    processed_image_bytes.seek(0)

    return redirect(url_for('polaroid.polaroid_result_hi'))

@polaroid.route('/polaroid/result/en')
def polaroid_result_en():
    return render_template('/Polaroid/PolaroidResultEn.html')

@polaroid.route('/polaroid/result/hi')
def polaroid_result_hi():
    return render_template('/Polaroid/PolaroidResultHi.html')

@polaroid.route('/polaroid/result/image')
def serve_processed_image():
    global processed_image_bytes
    return send_file(processed_image_bytes, mimetype='image/png')

from flask import Blueprint, render_template, request, redirect, url_for, send_file
from io import BytesIO
import base64
from PIL import Image
from website.SepiaS import process_sepia_image  # Import your custom script

sepia = Blueprint('sepia', __name__)

# Global temporary image buffer
processed_image_bytes = BytesIO()

@sepia.route('/sepia/en')
def sepia_capture_en():
    return render_template('/Sepia/SepiaPicEn.html')

@sepia.route('/sepia/hi')
def sepia_capture_hi():
    return render_template('/Sepia/SepiaPicHi.html')

@sepia.route('/upload/sepia/en', methods=['POST'])
def handle_sepia_upload_en():
    global processed_image_bytes

    img_data = request.form['image_data']
    if ',' in img_data:
        img_data = img_data.split(',')[1]  # Remove data:image/png;base64,...
    img_bytes = base64.b64decode(img_data)
    img = Image.open(BytesIO(img_bytes))

    # Process the image using your custom script
    result_img = process_sepia_image(img)  # This returns a PIL.Image object

    # Save result into memory
    processed_image_bytes = BytesIO()
    result_img.save(processed_image_bytes, format='PNG')
    processed_image_bytes.seek(0)

    return redirect(url_for('sepia.sepia_result_en'))

@sepia.route('/upload/sepia/hi', methods=['POST'])
def handle_sepia_upload_hi():
    global processed_image_bytes

    img_data = request.form['image_data']
    if ',' in img_data:
        img_data = img_data.split(',')[1]  # Remove data:image/png;base64,...
    img_bytes = base64.b64decode(img_data)
    img = Image.open(BytesIO(img_bytes))

    # Process the image using your custom script
    result_img = process_sepia_image(img)  # This returns a PIL.Image object

    # Save result into memory
    processed_image_bytes = BytesIO()
    result_img.save(processed_image_bytes, format='PNG')
    processed_image_bytes.seek(0)

    return redirect(url_for('sepia.sepia_result_hi'))

@sepia.route('/sepia/result/en')
def sepia_result_en():
    return render_template('/Sepia/SepiaResultEn.html')

@sepia.route('/sepia/result/hi')
def sepia_result_hi():
    return render_template('/Sepia/SepiaResultHi.html')

@sepia.route('/sepia/result/image')
def serve_processed_image():
    global processed_image_bytes
    return send_file(processed_image_bytes, mimetype='image/png')

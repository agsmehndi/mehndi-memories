from flask import Blueprint, render_template, request, redirect, url_for, send_file
from io import BytesIO
import base64
from PIL import Image
from website.VHSS import process_VHS_image  # Import your custom script

VHS = Blueprint('VHS', __name__)

# Global temporary image buffer
processed_image_bytes = BytesIO()

@VHS.route('/VHS/en')
def VHS_capture_en():
    return render_template('/VHS/VHSPicEn.html')

@VHS.route('/VHS/hi')
def VHS_capture_hi():
    return render_template('/VHS/VHSPicHi.html')

@VHS.route('/upload/VHS/en', methods=['POST'])
def handle_VHS_upload_en():
    global processed_image_bytes

    img_data = request.form['image_data']
    if ',' in img_data:
        img_data = img_data.split(',')[1]  # Remove data:image/png;base64,...
    img_bytes = base64.b64decode(img_data)
    img = Image.open(BytesIO(img_bytes))

    # Process the image using your custom script
    result_img = process_VHS_image(img)  # This returns a PIL.Image object

    # Save result into memory
    processed_image_bytes = BytesIO()
    result_img.save(processed_image_bytes, format='PNG')
    processed_image_bytes.seek(0)

    return redirect(url_for('VHS.VHS_result_en'))

@VHS.route('/upload/VHS/hi', methods=['POST'])
def handle_VHS_upload_hi():
    global processed_image_bytes

    img_data = request.form['image_data']
    if ',' in img_data:
        img_data = img_data.split(',')[1]  # Remove data:image/png;base64,...
    img_bytes = base64.b64decode(img_data)
    img = Image.open(BytesIO(img_bytes))

    # Process the image using your custom script
    result_img = process_VHS_image(img)  # This returns a PIL.Image object

    # Save result into memory
    processed_image_bytes = BytesIO()
    result_img.save(processed_image_bytes, format='PNG')
    processed_image_bytes.seek(0)

    return redirect(url_for('VHS.VHS_result_hi'))

@VHS.route('/VHS/result/en')
def VHS_result_en():
    return render_template('/VHS/VHSResultEn.html')

@VHS.route('/VHS/result/hi')
def VHS_result_hi():
    return render_template('/VHS/VHSResultHi.html')

@VHS.route('/VHS/result/image')
def serve_processed_image():
    global processed_image_bytes
    return send_file(processed_image_bytes, mimetype='image/png')

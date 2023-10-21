import os
from flask import render_template, request, send_from_directory, redirect, Flask

from website.watermarker import watermark_image

app = Flask(__name__)
app.secret_key = 'EvAnGeLiOn11111001011'

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'image' not in request.files:
            return redirect(request.url)

        image = request.files['image']

        if image.filename == '':
            return redirect(request.url)

        if image and allowed_file(image.filename):
            image_path = os.path.join(UPLOAD_FOLDER, image.filename)
            image.save(image_path)

            watermark_image(image_path, 'static/watermarked_image.jpg', 'watermark/watermark.png')

            return render_template('result.html')

    return render_template('index.html')

@app.route('/download')
def download_image():
    return send_from_directory('../static', 'watermarked_image.jpg')
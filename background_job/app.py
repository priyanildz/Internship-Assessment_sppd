from flask import Flask, request, render_template
from PIL import Image, ImageDraw, ImageFont
import os
from threading import Thread
from flask import send_from_directory

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

def process_image(image_path, filename):
    img = Image.open(image_path)

    # Create thumbnails
    for size in [(200, 200), (100, 100)]:
        thumb = img.copy()
        thumb.thumbnail(size)
        thumb.save(os.path.join(PROCESSED_FOLDER, f"{size[0]}x{size[1]}_{filename}"))

    # Watermark
    watermark = img.copy()
    draw = ImageDraw.Draw(watermark)
    font = ImageFont.load_default()
    try:
        font = ImageFont.truetype("arial.ttf", 80)  # Adjust size her
    except IOError:
        font = ImageFont.load_default()
    draw.text((200, 250), "Watermark", fill="grey", font=font)
    watermark.save(os.path.join(PROCESSED_FOLDER, f"watermarked_{filename}"))

@app.route('/', methods=['GET', 'POST'])
def index():
    thumbnails = []
    watermark = None

    if request.method == 'POST':
        file = request.files['image']
        filename = file.filename
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        thread = Thread(target=process_image, args=(filepath, filename))
        thread.start()
        thread.join()  # Wait until processing is done

        thumbnails = [f"{size[0]}x{size[1]}_{filename}" for size in [(200, 200), (100, 100)]]
        watermark = f"watermarked_{filename}"

    return render_template('upload_form.html', thumbnails=thumbnails, watermark=watermark)

@app.route('/processed/<filename>')
def processed_file(filename):
    return send_from_directory('processed', filename)

if __name__ == '__main__':
    app.run(debug=True)
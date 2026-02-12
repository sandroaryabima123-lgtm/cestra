from flask import Flask, request, send_file
from flask_cors import CORS
from rembg import remove, new_session
import io
import os

app = Flask(__name__)
CORS(app)

# Gunakan model u2netp (versi ringan/pocket) agar tidak membebani server gratis
model_name = "u2netp" 
session = new_session(model_name)

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image_file' not in request.files:
        return "No file uploaded", 400
    
    file = request.files['image_file'].read()
    
    # Proses hapus background menggunakan session yang sudah disiapkan
    output = remove(file, session=session)
    
    return send_file(io.BytesIO(output), mimetype='image/png')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

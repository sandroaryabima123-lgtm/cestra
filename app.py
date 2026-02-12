from flask import Flask, request, send_file
from flask_cors import CORS
from rembg import remove, new_session
import io
import os

app = Flask(__name__)
CORS(app)

# Buat session khusus agar lebih stabil
session = new_session("u2netp") # Versi 'u2netp' lebih ringan dari default

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image_file' not in request.files:
        return "No file", 400
    
    file = request.files['image_file'].read()
    
    # Proses hapus background dengan session ringan
    output = remove(file, session=session)
    
    return send_file(io.BytesIO(output), mimetype='image/png')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

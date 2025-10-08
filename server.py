import os
from flask import Flask, jsonify, send_from_directory

SIGNAGE_FOLDER = '/home/shecl/signage_media'
URL_FILE = '/home/shecl/signage_urls.txt'

app = Flask(__name__)

@app.route('/files')
def list_files():
    allowed_exts = ('.png', '.jpg', '.jpeg', '.gif', '.mp4')
    # Get all files with their modification time
    files_with_time = []
    for f in os.listdir(SIGNAGE_FOLDER):
        if f.lower().endswith(allowed_exts):
            path = os.path.join(SIGNAGE_FOLDER, f)
            mtime = os.path.getmtime(path)  # modification time
            files_with_time.append((f, mtime))
    # Sort by mtime ascending
    files_sorted = [f for f, t in sorted(files_with_time, key=lambda x: x[1])]
    return jsonify(files_sorted)

@app.route('/urls')
def list_urls():
    urls = []
    if os.path.exists(URL_FILE):
        with open(URL_FILE, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]
    return jsonify(urls)

@app.route('/media/<path:filename>')
def media(filename):
    return send_from_directory(SIGNAGE_FOLDER, filename)

@app.route('/')
def index():
    return send_from_directory('.', 'slideshow.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

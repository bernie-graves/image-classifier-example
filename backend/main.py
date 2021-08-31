import os
import urllib.request
from app import app
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = set(['jpeg','png','gif'])

# File extension must be from ALLOWED_EXTENSIONS
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Upload file API
@app.route('/image-upload', methods=["POST"])
def image_upload():
    if 'file' not in request.files:
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file']
    if file.filename =='':
        resp = jsonify({'message': "No Image selected for upload"})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        resp = jsonify({'message' : 'Image successfully uploaded'})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify({'message': 'Allowed file types are jpeg, png, gif'})
        resp.status_code = 400
        return resp

# Start Flask App
if __name__ == "__main__":
    app.run()
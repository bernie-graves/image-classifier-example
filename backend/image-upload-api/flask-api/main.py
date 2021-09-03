
from app import app
from flask import Flask, request, redirect, jsonify


# Allowed file types
ALLOWED_EXTENSIONS = set(['jpeg','png','jpg'])

# File extension must be from ALLOWED_EXTENSIONS
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# API to validate the Image file
@app.route('/image-upload', methods=["POST"])
def image_upload():
    # Check if the post request has the file part
    if 'file' not in request.files:
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp

    file = request.files['file']
    # Check if a file was selected in the request
    if file.filename =='':
        resp = jsonify({'message': "No Image selected for upload"})
        resp.status_code = 400
        return resp

    # Correct request
    if file and allowed_file(file.filename):
        resp = jsonify({'message' : 'Success!'})
        resp.status_code = 201
        return resp

    else:
        resp = jsonify({'message': 'Allowed file types are jpeg, png, jpg'})
        resp.status_code = 400
        return resp

# Start Flask App
if __name__ == "__main__":
    app.run()
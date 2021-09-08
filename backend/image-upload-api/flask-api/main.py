# Imports
from app import app
from flask import Flask, request, redirect, jsonify, send_from_directory

import pickle
import os

# Allowed file types
ALLOWED_EXTENSIONS = set(['jpeg', 'png', 'jpg'])


# File extension must be from ALLOWED_EXTENSIONS
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# serving index.html on flask
@app.route('/')  # routing it to the home page
def home():
    return send_from_directory('frontend', 'index.html')


# API to validate the Image file
@app.route('/image-upload', methods=["POST"])
def image_upload():
    # Check if the post request has the file part
    if 'file' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp

    file = request.files['file']
    # Check if a file was selected in the request
    if file.filename == '':
        resp = jsonify({'message': "No Image selected for upload"})
        resp.status_code = 400
        return resp

    # Correct request
    if file and allowed_file(file.filename):
        resp = jsonify({'message': 'Success!'})
        resp.status_code = 201
        return resp

    else:
        resp = jsonify({'message': 'Allowed file types are jpeg, png, jpg'})
        resp.status_code = 400
        return resp
# Deserialization ---------------------------------------------------------------------------------

model = open('./notebooks/models/'+'2021-09-04-SVC.pkl','rb')
new_dict = pickle.load(model)
model.close()
print(new_dict)


# Start Flask App
if __name__ == "__main__":
    app.run()

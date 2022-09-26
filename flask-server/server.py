import flask
from flask import Flask, json, request, jsonify
from werkzeug.utils import secure_filename
import time
import os 

app = flask.Flask(__name__)

@app.route('/test', methods = ['GET'])
def test():
    return "Hello"

@app.route('/uploader', methods = ['POST'])
def handle_request():
    image_files = request.files.getlist('files')
    category = request.form.get('category')
    
    current_path = os.getcwd()
    upload_path = os.path.join(current_path, category)
    if not os.path.exists(upload_path):
        os.makedirs(upload_path)

    for image in image_files:
        image_filename = secure_filename(image.filename)
        timestr = time.strftime("%Y%m%d-%H%M%S")
        image.save(os.path.join(upload_path, timestr+'_'+image_filename))
    
    resp = jsonify({'message':'Image uploaded successfully!'})
    resp.status_code = 201
    return resp

app.run(host="0.0.0.0", port=10001, debug=True)





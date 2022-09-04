import flask
import werkzeug
import time
import os 

app = flask.Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/Users/sandhyabalaji/Desktop/'

@app.route('/uploader', methods = ['GET', 'POST'])
def handle_request():
    files_ids = list(flask.request.files)
    #file_ids = flask.request.form
    category = flask.request.args.get("category")
    
    print(category)
    
    #print("\nNumber of Received Images : ", len(files_ids))
    image_num = 1
    
    print("\nSaving Image ", str(image_num), "/", len(file_ids))
    imagefile = flask.request.files[file_ids]
    filename = werkzeug.utils.secure_filename(imagefile.filename)
    print("Image Filename : " + imagefile.filename)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    imagefile.save(timestr+'_'+filename)
    user_folder = os.path.join(app.config['UPLOAD_FOLDER'])
    os.mkdir(category+"_folder")
    
   
    return "Image(s) Uploaded Successfully. Come Back Soon."

app.run(host="0.0.0.0", port=5000, debug=True)
from flask import Flask,render_template
import json
from flask import request,session
from werkzeug.utils import secure_filename
import os
from video_transcription import video_to_audio
from picovoice import audio_to_text,show

app=Flask(__name__)

with open('config.json','r') as c:
    params=json.load(c)["params"]

app.config['UPLOAD_FOLDER']=params['upload_location']

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/uploader',methods=['GET','POST'])
def uploader():
    if request.method=='POST':
        f = request.files['file1']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        video_to_audio()
        audio_to_text()
        show()
        return render_template('transcribe.html')

# @app.route('/trans')
# def display():
#     return render_template('transcribe.html')

if __name__ == "__main__":
    app.run()
from flask import Flask
from flask import render_template
from flask import url_for
import os

app = Flask(__name__)

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path, endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/About_us')
def about_us():
    return render_template('About_us.html')

@app.route('/FAQ')
def faq():
    return render_template('FAQ.html')

#app.run()
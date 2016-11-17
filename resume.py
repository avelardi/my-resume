#my-resume
#v2.0

from flask import Flask, render_template
import yaml
import os
app = Flask(__name__)

##for testing and stuff
app.config['PROPAGATE_EXCEPTIONS'] = True

def get_file(filename):
    try:
        src = os.path.join(os.path.abspath(os.path.dirname(__file__)) + "/static/assets", filename)
        return open(src).read()
    except IOError as exc:
        return str(exc)

infofile = get_file("resume.yaml")
info = yaml.load(infofile)

@app.route('/')
def resume():
    return render_template('index.html',info=info)

@app.route('/keybase.txt')
def keybase():
    keybasefile = get_file("keybase.txt")
    return keybasefile

if __name__ == '__main__':
    app.run()

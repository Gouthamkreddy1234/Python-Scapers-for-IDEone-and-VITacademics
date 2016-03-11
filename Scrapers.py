from flask import Flask
from IdeONE import Scrape
from VIT.VIT import scrape

app = Flask(__name__)
UPLOAD_FOLDER = '/path/to/the/uploads'


@app.route('/')
def hello_world():
    return 'Included 2 scrapers!'

@app.route('/Ideone')
def Ideone():
            sc = Scrape()
            sc.getjson()
            return str(sc.parseJson())

@app.route('/VITacademics')
def VITacademics():
             print "hi"
             scr =scrape()
             scr.req()
             return str(scr.req())

if __name__ == '__main__':
    app.run()
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


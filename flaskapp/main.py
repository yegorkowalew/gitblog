from flask import Flask, render_template, send_from_directory
from api.blueprint import api
from blog.blueprint import blog

from modules.themes import fol

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(blog, url_prefix='/blog')

@app.route('/')
def index():
    return render_template('index.html', first=fol())

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.debug = True
    app.run()




#app/routes.py

from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Main page aka Hello World!"

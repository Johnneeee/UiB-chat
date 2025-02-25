from app import app, cssData
from flask import send_from_directory, make_response
from flask_login import current_user

@app.route('/favicon.ico')
def favicon_ico():
    return send_from_directory(app.root_path, 'resourses/favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/favicon.png')
def favicon_png():
    return send_from_directory(app.root_path, 'resourses/favicon.png', mimetype='image/png')

@app.get('/highlight.css')
def highlightStyle():
    resp = make_response(cssData)
    resp.content_type = 'text/css'
    return resp

@app.get('/user')
def user():
    u = {"name" : current_user.id}
    return u

import os
from bottle import route, jinja2_template as template, run, static_file

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static')

@route('/')
def home():
    return template("templates/lp.html")

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    run(host="0.0.0.0", port=port, debug=True)

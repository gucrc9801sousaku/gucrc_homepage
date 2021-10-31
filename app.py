from bottle import route, jinja2_template as template, run, static_file

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static')

@route('/')
def home():
    return template("templates/lp.html")

if __name__ == '__main__':
    run(host='localhost', port=5000, reloader=True, debug=True)

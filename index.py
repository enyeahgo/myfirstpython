from bottle import Bottle, get, post, request, static_file, run # or route

app = Bottle()

@app.get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@app.post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if ((username == 'egoy') and (password == 'egoy')):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./public/')

run(app, host='localhost', port=8080)
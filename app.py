from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded credentials
USERNAME = "admin"
PASSWORD = "password"

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    if username == USERNAME and password == PASSWORD:
        return redirect(url_for('home'))
    else:
        return "Invalid credentials. Try again."

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


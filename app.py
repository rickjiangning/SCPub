from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

urls_EXT = [
        'http://209.202.207.141', #905
        'http://209.202.207.141', #905 
        'http://209.202.207.141', #905 
        'http://99.250.143.55', #350 Driveway
        ]
urls_INT = [
        'http://192.168.0.122', #905
        'http://192.168.0.122', #905
        'http://192.168.0.122', #905
        'http://99.250.143.55', #350 Driveway
        ]

@app.route('/')
@app.route('/login')
def home():
    if  session.get('logged_in_INT'):
        return render_template('index.html', urls=urls_INT)
    if  session.get('logged_in_EXT'):
        return render_template('index.html', urls=urls_EXT)
    
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'admin123' and request.form['username'] == 'adminext':
        session['logged_in_EXT'] = True
        return render_template('index.html', urls=urls_EXT)
    
    if request.form['password'] == 'admin321' and request.form['username'] == 'adminint':
        session['logged_in_INT'] = True
        return render_template('index.html', urls=urls_INT)

    
    #else:
    flash('wrong password!')
    return home()

@app.route("/logout")
def logout():
    if  session.get('logged_in_EXT'):
        session['logged_in_EXT'] = False
    if  session.get('logged_in_INT'):
        session['logged_in_INT'] = False
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    #app.run(debug=True,host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0', port=8080) 

from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os






Ext905=os.getenv('Ext_IP_905',"")
Int905=os.getenv('Int_IP_905',"")
EXT350=os.getenv('Ext_IP_350',"")
PASSWDINT=os.getenv('PWDINT',"")
PASSWDEXT=os.getenv('PWDEXT',"")

app = Flask(__name__)

urls_EXT = [
        Ext905, #905
        Ext905, #905 
        Ext905, #905 
        EXT350, #350 
        ]
urls_INT = [
        Int905, #905
        Int905, #905
        Int905, #905
        EXT350, #350
        ]

@app.route('/')
#@app.route('/login')
def home():
    if  session.get('logged_in_INT'):
        return render_template('index.html', urls=urls_INT)
    if  session.get('logged_in_EXT'):
        return render_template('index.html', urls=urls_EXT)
    
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == PASSWDEXT and request.form['username'] == 'adminext':
        session['logged_in_EXT'] = True
        return render_template('index.html', urls=urls_EXT)
    
    if request.form['password'] == PASSWDINT and request.form['username'] == 'adminint':
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

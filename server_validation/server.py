from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


app = Flask(__name__)

app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process', methods=['POST','GET'])
def process():
        if not EMAIL_REGEX.match(request.form['email']):
          flash("Invalid email")
          print 4
        if len(request.form['firstname']) < 1:
          flash("Name cannot be empty!") 
          print 1
        if len(request.form['lastname']) < 1:
          print 2
          flash("Lastname cannot be empty!") 

        if len(request.form['email']) < 1:
          flash("email cannot be empty")
          print 3
        if len(request.form['password']) < 8:
          flash("invalid password must be 8 chararcters")
          print 5
        if len(request.form['validation']) < 1:
          flash("please validate password")
          print 6
        if str(request.form['validation']) != str(request.form['password']):
          print 7
          flash("Password and confirmation do not match!")
        else:
          flash("Thank You")

        return redirect('/')

app.run(debug=True)   
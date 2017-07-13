from flask import Flask, render_template,request,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name="man")

@app.route('/dojo')
def dojo():
    return render_template('dojo.html')

@app.route('/result',methods=['POST', 'GET'])
def ninja():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    return render_template('ninja.html', firstname=firstname, lastname=lastname)

app.run(debug=True)

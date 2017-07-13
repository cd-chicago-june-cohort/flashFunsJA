from flask import Flask, render_template,request,redirect

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('sub.html')

@app.route('/index',methods=['POST', 'GET'])
def ninja():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    comment = request.form['comment']
    return render_template('index.html', firstname=firstname, lastname=lastname, comment=comment)

app.run(debug=True)

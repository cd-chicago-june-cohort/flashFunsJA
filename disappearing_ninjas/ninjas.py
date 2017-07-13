from flask import Flask, render_template,request,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninja():
    return render_template('all.html')

@app.route('/ninjas/<color>')
def ninja_color(color):
    return render_template('red.html',color=color)

app.run(debug=True)

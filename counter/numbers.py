from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'very secret'


@app.route('/')
def counter():
    try:
        session['visits'] += 1
    except:
        session['visits'] = 1
    return render_template('index.html',visits= session['visits'])

@app.route('/add2', methods=['POST'])
def increment():
    print 'hello again'
    session['visits'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    print "button"
    session['visits']=-1
    return redirect('/')

@app.route('/2', methods=['POST'])
def two():
    print "button"
    session['visits'] +=1
    return redirect('/')

app.run(debug=True)
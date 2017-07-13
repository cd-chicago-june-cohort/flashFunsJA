from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'very secret'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    points = session['gold']
    if 'activities' not in session:
        session['activities'] = "Nothing to show"
    activitiesT = session['activities']
    if 'message' not in session:
        session['message']= " Lets find coins "
    message = session['message']
    session['activities']+= message
    
    print session['activities']

    return render_template('index.html',event=message,gold=points, activities=activitiesT)

@app.route('/farm', methods=['POST', 'GET'])
def farm():
    chance=random.randint(10, 21)
    print chance
    session['message']= " :you found "+ str(chance)+" coins at the farm! "
    session['gold']+=chance
  
    
    return redirect('/')

@app.route('/cave', methods=['POST', 'GET'])
def cave():
    chance=random.randint(5, 11)
    print chance
    session['message']= " :you found "+ str(chance)+" coins at the Cave! "
    session['gold']+=chance
    
    return redirect('/')

@app.route('/house', methods=['POST', 'GET'])
def house():
    chance=random.randint(2, 6)
    print chance
    session['message']= " :you found "+ str(chance)+" coins at the House! "
    session['gold']+=chance
    
    return redirect('/')

@app.route('/casino', methods=['POST', 'GET'])
def casino():
    chance=random.randint(0,100)
    if chance > 70:
        amt = random.randint(0,50)
        session['message']= " :you won "+ str(amt)+" coins at the Casino! "
        session['gold']+=amt
    if chance < 70:
        amt = random.randint(0,50)
        session['message']= " :you lost "+ str(amt)+" coins at the Casino! "
        session['gold']-=amt
    return redirect('/')


@app.route('/reset', methods=['POST', 'GET'])
def clear():
    session.clear()
    return redirect('/')

app.run(debug=True)
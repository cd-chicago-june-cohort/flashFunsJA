from flask import Flask, render_template, session, request, redirect
import random



app = Flask(__name__)

app.secret_key= "abc"

@app.route('/')
def index():
    if 'randnum' not in session:
        session['randnum']= random.randint(1, 100)
        print session['randnum']
    randnum = session['randnum']
    
    print session['randnum'],"< rand num"
    if 'message' not in session:
        session['message']="Would you like to play a game?"
    message = session['message']

    if 'guess' not in session: 
        session['guess']="0"
    guessnum=session['guess']
    print guessnum,"< num guessed"

    return render_template('index.html',instructions=message,guess=guessnum )
    
@app.route('/guess', methods=['POST'])
def guess():
    session['guess']= request.form['guess']

    if int(session['guess'])  > int(session['randnum']):
            message = "too high Try Again"
    elif int(session['guess'])  < int(session['randnum']):
            message = "too low, Try again"
    elif int(session['guess'])  == int(session['randnum']):
            message = "You Win!, click new game to play again"
    session['message']= message
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset(): 
    session.clear()
    return redirect('/')
    
app.run(debug=True)   
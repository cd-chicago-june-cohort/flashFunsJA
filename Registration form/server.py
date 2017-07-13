from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
  if len(request.form['firstname']) < 1:
    flash("Name cannot be empty!") 
  # else:
  #   flash("Success! Your name is {}".format(request.form['name']))
    
  elif len(request.form['lastname']) < 1:
    flash("Lastname cannot be empty!") 
  
  elif len(request.form['lastname']) < 1:
    flash("leave comment ugly")

  elif len(request.form['comment']) < 1:
        flash("leave comment ugly")
        
  elif len(request.form['comment']) > 120:
        flash("YOU WRITE TEW MUCH")

  else:
    flash("yay")

  return redirect('/')

app.run(debug=True)   
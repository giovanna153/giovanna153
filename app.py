from flask  import Flask 
from flask import render_template

app = Flask(__name__)

@app.route("/")
def incio():
    frutas = ['maça','banana',"seila"]
   
    return render_template("incio.html", f = frutas)



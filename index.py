from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/") #首頁
def index():    #一定要有return
    return render_template("index.html")

@app.route("/f")
def first():
    return render_template("firstpage.html")
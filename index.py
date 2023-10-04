from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/") #首頁
def index():    #一定要有return
    return render_template("index.html")

@app.route("/first")
def hello():
    return render_template("first_page.html")
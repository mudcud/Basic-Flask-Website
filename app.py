from flask import Flask,render_template,request

app=Flask(__name__) #turn this file serve.py to a web app

@app.route("/", methods =["GET","POST"])# app that listen to forward slash. .When Flask sees a request from slash from user do the following. retun me

def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        return render_template("greet.html", name=request.view_args.get("name", "Friend"))



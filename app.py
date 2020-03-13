from flask import Flask, render_template, url_for, request, redirect , send_from_directory


app = Flask(__name__)

@app.route("/")
def approot():
    return  render_template('index.html')

@app.route("/login")
def approot():
    return  render_template('login.html')

@app.route("/search")
def approot():
    return  render_template('search.html')

@app.route("/")
def approot():
    return  render_template('index.html')

@app.route("/")
def approot():
    return  render_template('index.html')



app.run(debug=True)

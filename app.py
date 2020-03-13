from flask import Flask, render_template, url_for, request, redirect , send_from_directory


app = Flask(__name__)

@app.route("/")
def viewpage():
    return  render_template('index.html')

@app.route("/login")
def login():
    return  render_template('login.html')

@app.route("/search")
def search():
    return  render_template('search.html')

@app.route("/crt")
def create():
    return  render_template('crt.html')


@app.route("/allrec")
def allrec():
    return  render_template('allrec.html')



# Error Handlers
def page_not_found(e):
  return render_template('404.html'), 404

def create_app(config_filename):
    app = Flask(__name__)
    app.register_error_handler(404, page_not_found)
    return app




app.run(debug=True)

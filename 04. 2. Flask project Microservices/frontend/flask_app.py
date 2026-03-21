from IPython.lib.pretty import Printable
from flask import Flask, render_template,request
from datetime import datetime
import requests

backend_url="http://127.0.0.1:8000"
app = Flask(__name__,template_folder="templates")

@app.route("/")
def home():
    date = datetime.now().strftime("%A")
    return render_template("index.html",day_of_week=date)

@app.route("/submit",methods=["POST"])
def submit():
    form_data=dict(request.form)
    requests.post(backend_url+"/submit",json=form_data)
    return "Success"

if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0",port=9000,use_reloader=False)
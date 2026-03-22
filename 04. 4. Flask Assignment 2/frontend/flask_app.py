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
    try:
        form_data=dict(request.form)
        if form_data.get("password") != form_data.get("confirm_password"):
            return render_template("index.html",error="Passwords do not match",day_of_week=datetime.now().strftime("%A"))
        requests.post(backend_url+"/submit",json=form_data)
        return render_template("success.html")
    except Exception as e:
        return render_template("index.html",error=str(e))

if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0",port=9000,use_reloader=False)
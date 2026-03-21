from flask import Flask, request, redirect, url_for, render_template
import os
from dotenv import load_dotenv
load_dotenv()
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Create a new client and connect to the server
MONGO_URI = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

db=client.test
collection=db['flask_tutorial']

app = Flask(__name__,template_folder="../frontend/templates")

@app.route("/submit",methods=["POST"])
def submit():
    try:
        form_data = dict(request.form)
        # Insert into MongoDB
        collection.insert_one(form_data)
        # Redirect on success
        return redirect(url_for("success"))
    except Exception as e:
        # Show error on same page
        return render_template("success.html", error=str(e))

@app.route("/view")
def view():
    data=collection.find()
    data=list(data)
    for item in data:
        print(item)
        del item['_id']
    data={'data':data}
    return data

if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0",port=8000,use_reloader=False)
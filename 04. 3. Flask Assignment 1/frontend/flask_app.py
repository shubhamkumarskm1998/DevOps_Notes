from flask import Flask, json, jsonify

app = Flask(__name__)

@app.route("/api")
def get_data():
    with open("../backend/data.json") as f:
        data = json.load(f)
    return jsonify(data)

if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0",port=9000,use_reloader=False)
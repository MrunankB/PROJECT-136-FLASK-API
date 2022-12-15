from flask import Flask, jsonify, request
from data import data
app = Flask(__name__)
@app.route("/")
def index():
    return jsonify({
        "data": data,
        "message": "Success"
    }), 200
@app.route("/stars")
def star():
    name = request.args.get("name")
    stars_data = next(item for item in data if item["name"]==name)
    return jsonify({
        "data": stars_data,
        "message": "Success"
    }), 200
if (__name__=="__main__"):
    app.run()
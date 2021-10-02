from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.json_util import dumps
import json

client = MongoClient('mongodb://localhost:27017/')
database = client["HackatonBB-5"]
collection = database["top_10"]

app = Flask(__name__)


@app.route("/api/all_top", methods = ['GET'])
def get_all_top():
    try:
        top_10 = collection.find()
        return dumps(top_10)

    except Exception:
        return Exception
    
@app.route("/api/pais", methods = ['GET'])
def get_paises():
    try:
        json_ = [{'id':1, 'Pais':'Argentina', 'ISO':'AR'}, {'id':2, 'Pais':'Estados Unidos', 'ISO':'EN'}, {'id':3, 'Pais':'Canada', 'ISO':'CA'}, {'id':4, 'Pais':'Chile', 'ISO':'CL'}]
        return jsonify(json_)
    except Exception as e:
        return e
app.run(debug=False)
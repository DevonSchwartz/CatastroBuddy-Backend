from flask import Flask, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
import os
from schema import Fields

app = Flask(__name__)
client = MongoClient('localhost', os.getenv('MONGO_LOCAL_PORT'))
db = client.CatastroBuddy
collection = db.HouseholdItems

@app.route("/entry/<client_id>", methods=['GET'])
def get_client_items(client_id):

    entry = collection.find_one({Fields.clientId.name: client_id})

    if entry:
        entry['_id'] = str(entry['_id'])
        return jsonify(entry)
    else:
        return jsonify({"Error": "Entry not found"}), 400

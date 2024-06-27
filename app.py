from flask import Flask, jsonify, request
from pymongo import MongoClient
from schema import Fields
from objects import item
from bson.objectid import ObjectId
import os

app = Flask(__name__)
client = MongoClient('localhost', os.getenv('MONGO_LOCAL_PORT'))
db = client.CatastroBuddy
collection = db.HouseholdItems

'''
Read and return the whole items list for a client_id. Client_ids are expected to be unique in 
the database
'''
@app.route("/entry/<client_id>", methods=['GET'])
def get_client_items(client_id):
    entry = collection.find_one({Fields.clientId.name: client_id})
    if entry and entry[Fields.items.name]:
        return jsonify(entry[Fields.items.name])
    else:
        return jsonify({"Error": "Entry not found"}), 400
    

'''
Add a new household for a specific client_id 
'''
@app.route("/entry/<client_id>", methods=['POST'])
def add_client_items(client_id):
    request_data = request.get_json()
    new_item = item.Item(request_data[Fields.itemName.name], request_data[Fields.description.name],
                            request_data[Fields.originalPhoto.name], request_data[Fields.price.name],
                            request_data[Fields.damaged.name], request_data[Fields.damagedPhoto.name],
                            None)
    
    new_data = collection.update_one({Fields.clientId.name: client_id}, 
                                     {"$push": {Fields.items.name: new_item.to_dict()}}, upsert=False)

    if new_data.modified_count == 0:
        return jsonify({"Error": "Entry not found"}), 400
    else:
        return jsonify({"Success": "Item added", '_item_id': str(new_item._item_id)})
    
'''
Delete a specific item for a specific client_id based on an object id
'''
@app.route("/entry/<client_id>/<_item_id>", methods=['DELETE'])
def delete_client_item(client_id, _item_id):
    delete_data = collection.update_one({Fields.clientId.name: client_id}, 
                                        {"$pull": {Fields.items.name: {"_item_id": ObjectId(_item_id)}}})
    if delete_data.modified_count == 0:
        return jsonify({"Error": "Entry not found"}), 400
    else:
        return jsonify({"Success": "Item deleted"}) 

''''
Update a specific item for a specific client_id based on the object id
'''
@app.route("/entry/<client_id>/<_item_id>", methods=['PUT'])
def update_client_item(client_id, _item_id):
    request_data = request.get_json()
    updated_item = item.Item(request_data[Fields.itemName.name], request_data[Fields.description.name],
                            request_data[Fields.originalPhoto.name], request_data[Fields.price.name],
                            request_data[Fields.damaged.name], request_data[Fields.damagedPhoto.name],
                            _item_id)
    
    update_data = collection.update_one({Fields.clientId.name: client_id, Fields.items.name + "." + Fields._item_id.name: ObjectId(_item_id)}, 
                                        {"$set": {Fields.items.name + ".$": updated_item.to_dict()}})
    if update_data.modified_count == 0:
        return jsonify({"Error": "Entry not found"}), 400
    else:
        return jsonify({"Success": "Item updated"})

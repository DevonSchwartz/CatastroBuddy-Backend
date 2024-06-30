from schema import Fields
from bson.objectid import ObjectId

'''
An item object. This represents each household item that belongs to a client
'''
class Item:
    def __init__(self, item_name, description, original_photo, price, damaged, damaged_photo, _item_id):
        self.item_name = item_name
        self.description = description
        self.original_photo = original_photo
        self.price = price
        self.damaged = damaged
        self.damaged_photo = damaged_photo
        self._item_id = ObjectId(_item_id) if _item_id else ObjectId()

    '''
    Convert the object to a dictionary for easy serialization
    '''
    def to_dict(self):
        return {
            Fields.itemName.name: self.item_name,
            Fields.description.name: self.description,
            Fields.originalPhoto.name: self.original_photo,
            Fields.price.name: self.price,
            Fields.damaged.name: self.damaged,
            Fields.damagedPhoto.name: self.damaged_photo,
            Fields._item_id.name: self._item_id
        }
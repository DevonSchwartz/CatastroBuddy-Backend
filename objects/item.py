from schema import Fields

'''
An item object. This represents each household item that belongs to a client
'''
class Item:
    def __init__(self, item_name, description, original_photo, price, damaged, damaged_photo):
        self.item_name = item_name
        self.description = description
        self.original_photo = original_photo
        self.price = price
        self.damaged = damaged
        self.damaged_photo = damaged_photo

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
            Fields.damagedPhoto.name: self.damaged_photo
        }
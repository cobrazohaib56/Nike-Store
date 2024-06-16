import json
from shoe import Shoe

INVENTORY_FILE = 'database.json'

def load_inventory():
    try:
        with open(INVENTORY_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_inventory(inventory):
    with open(INVENTORY_FILE, 'w') as file:
        json.dump(inventory, file)

def add_shoe(name, size, color, quantity, sku):
    inventory = load_inventory()
    shoe = Shoe(name, size, color, quantity, sku).__dict__
    inventory.append(shoe)
    save_inventory(inventory)

def search_shoe(sku):
    inventory = load_inventory()
    for shoe in inventory:
        if shoe['sku'] == sku:
            return shoe
    return None

def update_shoe(sku, **kwargs):
    inventory = load_inventory()
    for shoe in inventory:
        if shoe['sku'] == sku:
            shoe.update(kwargs)
            save_inventory(inventory)
            return shoe
    return None

def delete_shoe(sku):
    inventory = load_inventory()
    inventory = [shoe for shoe in inventory if shoe['sku'] != sku]
    save_inventory(inventory)

def list_shoes():
    return load_inventory()
import json
import os

def setup():
    if not os.path.exists("data"):
        os.makedirs("data")

    initial_menu = {
        "M1": {
            "item_id": "M1",
            "name": "Classic Burger",
            "price": 120.0,
            "category": "mains",
            "available": True,
            "vegetarian": False
        },
        "M2": {
            "item_id": "M2",
            "name": "Margarita Pizza",
            "price": 150.0,
            "category": "mains",
            "available": True,
            "vegetarian": True
        },
        "S1": {
            "item_id": "S1",
            "name": "Garlic Bread",
            "price": 60.0,
            "category": "starters",
            "available": True,
            "vegetarian": True
        },
        "D1": {
            "item_id": "D1",
            "name": "Coca Cola",
            "price": 40.0,
            "category": "beverages",
            "available": True,
            "vegetarian": True
        }
    }

    initial_tables = [
        {"table_number": 1, "capacity": 2, "server_name": None, "status": "Free"},
        {"table_number": 2, "capacity": 4, "server_name": None, "status": "Free"},
        {"table_number": 3, "capacity": 6, "server_name": None, "status": "Free"},
        {"table_number": 4, "capacity": 8, "server_name": None, "status": "Free"}
    ]

    with open("data/menu.json", "w") as f:
        json.dump(initial_menu, f, indent=4)

    with open("data/tables.json", "w") as f:
        json.dump(initial_tables, f, indent=4)

    with open("data/orders.json", "w") as f:
        json.dump([], f, indent=4)

if __name__ == "__main__":
    setup()
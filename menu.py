import json

class MenuItem:
    def __init__(self, item_id, name, price, category, available=True, vegetarian=False):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.category = category
        self.available = available
        self.vegetarian = vegetarian

    def to_dict(self):
        return self.__dict__

def load_menu(path: str) -> dict:
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except:
        return {}

def save_menu(path: str, menu: dict) -> None:
    with open(path, 'w') as f:
        json.dump(menu, f, indent=4)

def add_menu_item(menu: dict, item: dict) -> dict:
    new_item = MenuItem(**item)
    menu[new_item.item_id] = new_item.to_dict()
    return menu

def update_menu_item(menu: dict, item_id: str, updates: dict) -> dict:
    if item_id in menu:
        menu[item_id].update(updates)
    return menu

def filter_menu(menu: dict, category: str, vegetarian: bool | None = None) -> list:
    results = [item for item in menu.values() if item['category'] == category]
    if vegetarian is not None:
        results = [item for item in results if item.get('vegetarian') == vegetarian]
    return results
import datetime

class Order:
    def __init__(self, table_number):
        self.table_number = table_number
        self.items = []
        self.status = "open"
        self.timestamp = str(datetime.datetime.now())

def open_order(table_number: int) -> dict:
    new_order = Order(table_number)
    return {"table_number": new_order.table_number, "items": [], "status": "open"}

def add_item_to_order(order: dict, menu_item: dict, quantity: int, note: str = "") -> dict:
    item = {
        "item_id": menu_item['item_id'],
        "name": menu_item['name'],
        "price": menu_item['price'],
        "quantity": quantity,
        "status": "ordered",
        "note": note
    }
    order['items'].append(item)
    return order

def remove_item_from_order(order: dict, item_id: str) -> dict:
    order['items'] = [i for i in order['items'] if i['item_id'] != item_id]
    return order

def update_item_status(order: dict, item_id: str, status: str) -> dict:
    for item in order['items']:
        if item['item_id'] == item_id:
            item['status'] = status
    return order

def calculate_bill(order: dict, tax_rate: float, tip_rate: float) -> dict:
    subtotal = sum(i['price'] * i['quantity'] for i in order['items'] if i['status'] != 'voided')
    tax = subtotal * tax_rate
    tip = subtotal * tip_rate
    return {"subtotal": subtotal, "tax": tax, "tip": tip, "total": subtotal + tax + tip}

def split_bill(order: dict, method: str, parties: int | list) -> list:
    bill = calculate_bill(order, 0.1, 0.1)
    if method == "even":
        share = bill['total'] / parties
        return [{"share": share} for _ in range(parties)]
    return []
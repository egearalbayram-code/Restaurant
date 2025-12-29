import json
import os
import datetime

def load_state(data_dir: str) -> tuple:
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    t_path = os.path.join(data_dir, "tables.json")
    m_path = os.path.join(data_dir, "menu.json")
    o_path = os.path.join(data_dir, "orders.json")
    
    t = []
    if os.path.exists(t_path):
        with open(t_path, 'r') as f: t = json.load(f)
    
    m = {}
    if os.path.exists(m_path):
        with open(m_path, 'r') as f: m = json.load(f)
        
    o = []
    if os.path.exists(o_path):
        with open(o_path, 'r') as f: o = json.load(f)
        
    return t, m, o

def save_state(data_dir: str, tables: list, menu: dict, orders: list) -> None:
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    with open(os.path.join(data_dir, "tables.json"), 'w') as f: json.dump(tables, f, indent=4)
    with open(os.path.join(data_dir, "menu.json"), 'w') as f: json.dump(menu, f, indent=4)
    with open(os.path.join(data_dir, "orders.json"), 'w') as f: json.dump(orders, f, indent=4)

def log_kitchen_ticket(order: dict, directory: str) -> str:
    if not os.path.exists(directory):
        os.makedirs(directory)
    fname = f"ticket_{order['table_number']}_{datetime.datetime.now().strftime('%H%M%S')}.txt"
    with open(os.path.join(directory, fname), 'w') as f:
        f.write(f"TABLE: {order['table_number']}\n")
        for i in order['items']:
            f.write(f"- {i['name']} x{i['quantity']} ({i['status']})\n")
    return fname
import json

def load_state (data_dir: str) -> tuple:

    try:
        with open(f"{data_dir}/tables.json", "r") as f:

            tables = json.load(f)

        with open(f"{data_dir}/menu.json", "r") as f:

            menu = json.load(f)

        with open(f"{data_dir}/orders.json", "r") as f:

            orders = json.load(f)
        
        return menu, tables, orders
    
    except FileNotFoundError:

        return [], {}, []
    

def save_state(data_dir: str, tables:list, menu: dict, orders:list) -> None:

    with open(f"{data_dir}/tables.json", "w") as f:
        json.dump(tables, f, indent=4)

    with open(f"{data_dir}/menu.json", "w") as f :
        json.dump(menu, f, indent=4)

    with open(f"{data_dir}/orders.json", "w") as f:

        json.dump(orders, f, indent=4)

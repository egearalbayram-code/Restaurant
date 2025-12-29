class Table:
    def __init__(self, table_number, capacity, server_name=None, status="Free"):
        self.table_number = table_number
        self.capacity = capacity
        self.server_name = server_name
        self.status = status

    def to_dict(self):
        return self.__dict__

def initialize_tables(path: str) -> list:
    import json
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except:
        return []

def add_table(tables: list, table_data: dict) -> list:
    new_table = Table(**table_data)
    tables.append(new_table.to_dict())
    return tables

def assign_table(tables: list, table_number: int, party_size: int) -> dict | None:
    for table in tables:
        if table['table_number'] == table_number:
            if table['status'] == "Free" and party_size <= table['capacity']:
                table['status'] = "Occupied"
                return table
    return None

def release_table(tables: list, table_number: int) -> bool:
    for table in tables:
        if table['table_number'] == table_number:
            table['status'] = "Free"
            table['server_name'] = None
            return True
    return False

def update_server(tables: list, table_number: int, server_name: str) -> dict:
    for table in tables:
        if table['table_number'] == table_number:
            table['server_name'] = server_name
            return table
    return {}
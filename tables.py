

def add_table(tables: list, table_data: dict) -> list:
  
    tables.append(table_data)
    return tables

def assign_table(tables: list, table_number: int, party_size: int) -> dict | None:
   
    for table in tables:
        
        if table['number'] == table_number and table['status'] == 'free':
            
            if party_size <= table['capacity']:
                table['status'] = 'occupied'
                return table
    return None 

def release_table(tables: list, table_number: int) -> bool:

    for table in tables:
        if table['number'] == table_number:
            table['status'] = 'free'
            return True
    return False
from ..models import base_models as BaseModel

def logic_open_table(table_number):
    success, notification = BaseModel.open_table(table_number)

    if not success:
        return None, notification
    
    target_table = BaseModel.get_table(table_number)
    
    return target_table, notification

def logic_close_table(table_number):
    
    current_table = BaseModel.get_table(table_number)
    
    if current_table is None:
        return False, "The table doesn't exist!"
        
    if current_table.state == True:
        return False, "The table is empty!"
        
    BaseModel.close_table(table_number)

    return True, f"Table {table_number} is cleared!"

def get_table_layout():

    empty_tables = BaseModel.get_free_tables()
    occupied_tables = BaseModel.get_occupied_tables()
    
    return empty_tables, occupied_tables
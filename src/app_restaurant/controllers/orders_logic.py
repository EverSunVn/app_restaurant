from ..models import base_models as BaseModel

def logic_order_dish(table_number, dish_id):
    """Add a dish to the table's bill (Push to Stack)"""
    table = BaseModel.get_table(table_number)
    
    # Check if the table is currently opened (state == False means occupied/opened)
    if not table or table.state == True:
        return False, "Table is not opened yet!"
        
    # Convert dish_id to string to match JSON keys
    dish_id = str(dish_id)
    dish = BaseModel.get_dish(dish_id)
    
    if not dish:
        return False, "Dish does not exist!"
        
    bill = BaseModel.get_bill(table.id)
    
    # Push the dish into the stack (list) and add to total money
    bill.dishes_list.append(dish)
    bill.total_money += dish.cost
    
    return True, f"Added '{dish.name}' to Table {table_number}."

def logic_undo_dish(table_number):
    """Undo the last ordered dish (Pop from Stack)"""
    table = BaseModel.get_table(table_number)
    
    if not table or table.state == True:
        return False, "Table is not opened yet!"
        
    bill = BaseModel.get_bill(table.id)
    
    # Check if the stack is empty
    if not bill.dishes_list:
        return False, "No dishes to undo!"
        
    # Pop the last element from the stack and subtract from total money
    removed_dish = bill.dishes_list.pop()
    bill.total_money -= removed_dish.cost
    
    return True, f"Successfully undid (removed) '{removed_dish.name}'."
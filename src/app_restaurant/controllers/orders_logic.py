from ..models import base_models as BaseModel

def get_menu():
    return list(BaseModel.DISHES_DATA.values())

def process_order(table_number, dishID):

    table = BaseModel.get_table(table_number)
    if table is None or table.state == True:
        return False, "This table is not opened yet!"

    dish = BaseModel.get_dish(dishID)
    if dish is None:
        return False, "This dish doesn't exist!"

    bill = BaseModel.get_bill(table_number)
    bill.dishes_list.append(dish)
    bill.total_money += dish.cost
    
    return True, f"Added {dish.name} to table {table_number}."

def undo_process(table_number):

    table = BaseModel.get_table(table_number)
    if table is None or table.state == True:
        return False, "This table is not opened yet!"
    

    bill = BaseModel.get_bill(table_number)
    
    if not bill.dishes_list:
        return False, "This list is empty, can't undo"

    pop_dish = bill.dishes_list.pop() 
    
    bill.total_money -= pop_dish.cost
    
    return True, f"Succesfully removed dish: {pop_dish.name}"

def get_bill_details(table_number):
    table = BaseModel.get_table(table_number)
    if table is None or table.state == True:
        return None, 0 # Phần này return tiền 
        
    bill = BaseModel.get_bill(table_number)
    return bill.dishes_list, bill.total_money

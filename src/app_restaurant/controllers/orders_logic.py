from ..models import base_models as BaseModel
from ..controllers.kitchen_logic import add_order_to_queue, remove_order_from_queue

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

    remove_order_from_queue(table_number, pop_dish.name)
    
    return True, f"Succesfully removed dish: {pop_dish.name}"

def get_bill_details(table_number):
    table = BaseModel.get_table(table_number)
    if table is None or table.state == True:
        return None, 0 # Phần này return tiền 
        
    bill = BaseModel.get_bill(table_number)
    return bill.dishes_list, bill.total_money

def handle_order(table_number, dish_id):
    # ... các logic kiểm tra bàn, kiểm tra món ...
    
    # Lấy đối tượng món ăn
    dish = BaseModel.get_dish(dish_id)
    bill = BaseModel.get_bill(table_number)
    
    bill.dishes_list.append(dish)
    bill.total_money += dish.cost
    
    add_order_to_queue(table_number, dish)
    
    return True, "Order successful!"
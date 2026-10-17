from ..models import base_models as BaseModel

def logic_get_checkout_info(table_number):
    """Retrieve the current bill information for the checkout UI"""
    table = BaseModel.get_table(table_number)
    
    if not table or table.state == True:
        return False, "Table is empty or does not exist!", [], 0
        
    bill = BaseModel.get_bill(table.id)
    
    # Return success status, message, list of ordered dishes, and total amount
    return True, "Success", bill.dishes_list, bill.total_money

def logic_process_checkout(table_number):
    """Process the payment and clear the table"""
    table = BaseModel.get_table(table_number)
    
    if not table or table.state == True:
        return False, "Table is already empty or does not exist!"
        
    bill = BaseModel.get_bill(table.id)
    final_total = bill.total_money
    
    # Check if they ordered anything
    if final_total == 0 and len(bill.dishes_list) == 0:
        # If the bill is 0, just close the table normally
        BaseModel.close_table(table_number)
        return True, f"Table {table_number} closed with no orders."
    
    # Close the table (This function in base_models.py sets state to True and deletes the bill)
    BaseModel.close_table(table_number)
    
    return True, f"Checkout successful! Total paid: {final_total}."
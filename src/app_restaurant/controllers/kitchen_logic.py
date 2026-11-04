from ..models.base_models import KITCHEN_QUEUE

def add_order_to_queue(table_number, dish):
    # Create a dictionary to store what dish goes to which table
    order_item = {
        "table_number": table_number,
        "dish_name": dish.name
    }
    
    # Append adds to the END of the queue (tail)
    KITCHEN_QUEUE.append(order_item)
    return True, f"Sent {dish.name} (Table {table_number}) to the kitchen."

def get_pending_orders():
    """
    READ: Get the list of all pending orders for the chef's screen.
    """
    return KITCHEN_QUEUE

def complete_next_order():
    """
    DEQUEUE (FIFO): Chef completes the oldest order (the one at index 0).
    """
    # Check if the queue is empty
    if not KITCHEN_QUEUE:
        return False, "No pending orders in the kitchen!"

    # pop(0) removes and returns the FIRST item in the list (First-In, First-Out)
    completed_order = KITCHEN_QUEUE.pop(0)
    
    table_num = completed_order["table_number"]
    dish_name = completed_order["dish_name"]
    
    return True, f"Chef completed: {dish_name} for Table {table_num}!"

def remove_order_from_queue(table_number, dish_name):
    """
    Xóa món ăn vừa bị Undo khỏi hàng đợi của nhà bếp.
    Tìm ngược từ cuối danh sách lên để xóa đúng món vừa thêm sau cùng.
    """

    for i in range(len(KITCHEN_QUEUE) - 1, -1, -1):
        order = KITCHEN_QUEUE[i]
        
        # Nếu tìm thấy đúng bàn và đúng tên món
        if order["table_number"] == table_number and order["dish_name"] == dish_name:
            KITCHEN_QUEUE.pop(i) # Xóa phần tử tại vị trí i
            return True
            
    return False 
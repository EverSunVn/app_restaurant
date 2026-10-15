from models.base_models import get_bill, get_dish

def goi_mon(table_number: int, dish_id: str) -> tuple[bool, str]:
    """
    Thêm món ăn vào đơn hàng của bàn (Thao tác PUSH vào Stack)
    """
    bill = get_bill(table_number)
    dish = get_dish(dish_id)
    
    if not dish:
        return False, "Món ăn không tồn tại trong hệ thống!"
    
    # PUSH món vào Stack (dishes_list)
    bill.dishes_list.append(dish)
    bill.total_money += dish.cost
    return True, f"Đã thêm món '{dish.name}' vào Bàn {table_number}!"


def undo_mon_vua_them(table_number: int) -> tuple[bool, str]:
    """
    Rút món vừa được thêm cuối cùng ra khỏi đơn (Thao tác POP khỏi Stack)
    """
    bill = get_bill(table_number)
    
    # Kiểm tra Stack có trống hay không
    if not bill.dishes_list:
        return False, "Chưa có món nào trong đơn để hoàn tác (Undo)!"
    
    # POP món vừa thêm ở cuối Stack
    removed_dish = bill.dishes_list.pop()
    bill.total_money -= removed_dish.cost
    return True, f"Đã hoàn tác (xóa) món '{removed_dish.name}' khỏi Bàn {table_number}!"

from ..models import base_models as BaseModel

def logic_get_kitchen_orders():
    """Lấy danh sách tất cả các món ăn đang cần chế biến ở tất cả các bàn"""
    kitchen_orders = []
    
    # Duyệt qua tất cả các hóa đơn đang hoạt động trên hệ thống
    for table_num, bill in BaseModel.BILL_DATA.items():
        for index, ordered_dish in enumerate(bill.dishes_list):
            # Nhà bếp chỉ quan tâm món chưa nấu xong ("đã được đặt" hoặc "đang chế biến")
            if ordered_dish.status in ["đã được đặt", "đang chế biến"]:
                kitchen_orders.append({
                    "table_number": table_num,
                    "dish_index": index,
                    "dish_name": ordered_dish.dish.name,
                    "status": ordered_dish.status
                })
    return kitchen_orders

def logic_accept_cooking(table_number, dish_index):
    """Đầu bếp bấm nút tiếp nhận chế biến"""
    return BaseModel.update_dish_status(table_number, dish_index, "đang chế biến")

def logic_finish_cooking(table_number, dish_index):
    """Đầu bếp bấm nút chế biến xong"""
    return BaseModel.update_dish_status(table_number, dish_index, "chế biến xong")

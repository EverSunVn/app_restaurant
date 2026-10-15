from ..models import base_models as BaseModel

def logic_lay_danh_sach_mon():
    """Trả về toàn bộ dictionary món ăn"""
    return BaseModel.DISHES_DATA

def logic_them_mon(dish_id, name, cost):
    """Thêm món mới vào thực đơn"""
    # Ép kiểu dish_id về string nếu file json lưu key là string
    dish_id = str(dish_id) 
    
    if dish_id in BaseModel.DISHES_DATA:
        return False, f"Mã món '{dish_id}' đã tồn tại!"
    
    if cost < 0:
        return False, "Giá tiền không hợp lệ!"

    BaseModel.DISHES_DATA[dish_id] = BaseModel.Dishes(name, cost)
    return True, f"Đã thêm món '{name}' thành công!"

def logic_sua_mon(dish_id, new_name=None, new_cost=None):
    """Sửa thông tin món ăn"""
    dish_id = str(dish_id)
    
    if dish_id not in BaseModel.DISHES_DATA:
        return False, "Món ăn không tồn tại!"
        
    dish = BaseModel.DISHES_DATA[dish_id]
    
    if new_name:
        dish.name = new_name
    if new_cost is not None:
        if new_cost < 0:
            return False, "Giá tiền không hợp lệ!"
        dish.cost = new_cost
        
    return True, "Cập nhật món ăn thành công!"

def logic_xoa_mon(dish_id):
    """Xóa món ăn khỏi thực đơn"""
    dish_id = str(dish_id)
    
    if dish_id in BaseModel.DISHES_DATA:
        dish = BaseModel.DISHES_DATA.pop(dish_id)
        return True, f"Đã xóa món '{dish.name}'!"
        
    return False, "Món ăn không tồn tại!"

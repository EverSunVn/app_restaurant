from models.base_models import get_bill, close_table

def xu_ly_thanh_toan(table_number: int) -> tuple[bool, str, int]:
    """
    Tính tiền, in hóa đơn, làm sạch danh sách món và trả bàn về trạng thái Trống
    """
    bill = get_bill(table_number)
    
    if not bill.dishes_list:
        return False, "Bàn này chưa gọi món nào để thanh toán!", 0

    total_money = bill.total_money
    
    # Đóng bàn: Chuyển state về True (Trống) và xóa bill khỏi BILL_DATA
    close_table(table_number)

    return True, f"Thanh toán thành công cho Bàn {table_number}!", total_money

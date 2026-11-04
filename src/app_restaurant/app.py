<<<<<<< HEAD
import os
import sys
import streamlit as st

# 1. TRỌNG TÂM: Lùi đường dẫn ra ngoài thư mục 'src' thay vì đứng ở 'app_restaurant'
src_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# 2. Bây giờ import mọi thứ phải bắt đầu bằng chữ "app_restaurant."
=======

import os
import sys
import streamlit as st


# ==================================================
# 1. THIẾT LẬP ĐƯỜNG DẪN
# ==================================================

src_path = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if src_path not in sys.path:
    sys.path.insert(0, src_path)


# ==================================================
# 2. CẤU HÌNH STREAMLIT
# ==================================================

st.set_page_config(
    page_title="F&B Management App",
    layout="wide",
    page_icon="🍔"
)


# ==================================================
# 3. KHỞI TẠO KITCHEN QUEUE
# ==================================================

from app_restaurant.models import base_models as BaseModel

if not hasattr(BaseModel, "KITCHEN_QUEUE"):
    BaseModel.KITCHEN_QUEUE = []


# ==================================================
# 4. IMPORT CÁC MODULE
# ==================================================

>>>>>>> Ui/Dat
from app_restaurant.views.tables import render_tables_view
from app_restaurant.views.menu import render_menu_view
from app_restaurant.views.orders import render_orders_view
from app_restaurant.views.checkout import render_checkout_view
<<<<<<< HEAD

# ----- PHẦN UI DƯỚI NÀY GIỮ NGUYÊN -----
st.set_page_config(page_title="F&B Management App", layout="wide", page_icon="🍔")
st.title("🍔 Hệ Thống Quản Lý Nhà Hàng")

tab1, tab2, tab3, tab4 = st.tabs([
    "🪑 Sơ Đồ Bàn", 
    "📜 Thực Đơn", 
    "📝 Gọi Món (Orders)", 
    "💳 Thanh Toán (Checkout)"
])

=======
from app_restaurant.views.kitchen import render_kitchen_view

from app_restaurant.views import orders as orders_view

from app_restaurant.controllers import kitchen_logic
from app_restaurant.controllers import orders_logic


# ==================================================
# 5. KẾT NỐI ORDERS VỚI KITCHEN
# ==================================================

# Luôn lấy hàm gốc trực tiếp từ orders_logic
# Không lấy từ orders_view.process_order vì đây có thể
# là wrapper của lần chạy Streamlit trước.

def process_order_and_send_to_kitchen(table_number, dish_id):

    # Bước 1: Xử lý gọi món bằng logic gốc
    success, message = orders_logic.process_order(
        table_number,
        dish_id
    )

    # Bước 2: Chỉ gửi vào bếp đúng một lần nếu thành công
    if success:

        dish = BaseModel.get_dish(dish_id)

        if dish is not None:
            kitchen_logic.add_order_to_queue(
                table_number,
                dish
            )

    return success, message


# Gắn wrapper vào giao diện Orders
orders_view.process_order = process_order_and_send_to_kitchen


# ==================================================
# 6. TIÊU ĐỀ
# ==================================================

st.title("🍔 HỆ THỐNG QUẢN LÝ NHÀ HÀNG")

st.caption("Restaurant Management System - F&B")


# ==================================================
# 7. TẠO CÁC TAB
# ==================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🪑 Sơ Đồ Bàn",
    "📜 Thực Đơn",
    "📝 Gọi Món (Orders)",
    "💳 Thanh Toán (Checkout)",
    "👨‍🍳 Nhà Bếp (Kitchen)"
])


# ==================================================
# 8. HIỂN THỊ GIAO DIỆN
# ==================================================

>>>>>>> Ui/Dat
with tab1:
    render_tables_view()

with tab2:
    render_menu_view()

with tab3:
    render_orders_view()

with tab4:
    render_checkout_view()
<<<<<<< HEAD
=======

with tab5:
    render_kitchen_view()
>>>>>>> Ui/Dat


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

# Phải khởi tạo trước khi import orders_logic
# vì orders_logic có import kitchen_logic

from app_restaurant.models import base_models as BaseModel

if not hasattr(BaseModel, "KITCHEN_QUEUE"):
    BaseModel.KITCHEN_QUEUE = []


# ==================================================
# 4. IMPORT CÁC GIAO DIỆN
# ==================================================

from app_restaurant.views.tables import render_tables_view
from app_restaurant.views.menu import render_menu_view
from app_restaurant.views.orders import render_orders_view
from app_restaurant.views.checkout import render_checkout_view
from app_restaurant.views.kitchen import render_kitchen_view

from app_restaurant.views import orders as orders_view

from app_restaurant.controllers import kitchen_logic


# ==================================================
# 5. KẾT NỐI ORDERS VỚI KITCHEN
# ==================================================

# Lưu hàm process_order gốc
_original_process_order = orders_view.process_order


def process_order_and_send_to_kitchen(table_number, dish_id):

    # Bước 1: Xử lý gọi món
    success, message = _original_process_order(
        table_number,
        dish_id
    )

    # Bước 2: Nếu gọi món thành công, chuyển vào bếp
    if success:

        dish = BaseModel.get_dish(dish_id)

        if dish is not None:

            kitchen_logic.add_order_to_queue(
                table_number,
                dish
            )

    return success, message


# Thay hàm process_order được sử dụng trong orders.py
# Không chỉnh sửa file orders.py
orders_view.process_order = process_order_and_send_to_kitchen


# ==================================================
# 6. TIÊU ĐỀ ỨNG DỤNG
# ==================================================

st.title("🍔 HỆ THỐNG QUẢN LÝ NHÀ HÀNG")

st.caption(
    "Restaurant Management System - F&B"
)


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
# 8. HIỂN THỊ CÁC GIAO DIỆN
# ==================================================

with tab1:
    render_tables_view()


with tab2:
    render_menu_view()


with tab3:
    render_orders_view()


with tab4:
    render_checkout_view()


with tab5:
    render_kitchen_view()

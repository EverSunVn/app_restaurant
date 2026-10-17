import os
import sys
import streamlit as st

# 1. TRỌNG TÂM: Lùi đường dẫn ra ngoài thư mục 'src' thay vì đứng ở 'app_restaurant'
src_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# 2. Bây giờ import mọi thứ phải bắt đầu bằng chữ "app_restaurant."
from app_restaurant.views.tables import render_tables_view
from app_restaurant.views.menu import render_menu_view
from app_restaurant.views.orders import render_orders_view
from app_restaurant.views.checkout import render_checkout_view

# ----- PHẦN UI DƯỚI NÀY GIỮ NGUYÊN -----
st.set_page_config(page_title="F&B Management App", layout="wide", page_icon="🍔")
st.title("🍔 Hệ Thống Quản Lý Nhà Hàng")

tab1, tab2, tab3, tab4 = st.tabs([
    "🪑 Sơ Đồ Bàn", 
    "📜 Thực Đơn", 
    "📝 Gọi Món (Orders)", 
    "💳 Thanh Toán (Checkout)"
])

with tab1:
    render_tables_view()

with tab2:
    render_menu_view()

with tab3:
    render_orders_view()

with tab4:
    render_checkout_view()
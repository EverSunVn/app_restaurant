import os
import sys
import streamlit as st

# Cấu hình đường dẫn import
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from views.tables import render_tables_view
from views.menu import render_menu_view
from views.orders import render_orders_view
from views.checkout import render_checkout_view

st.set_page_config(page_title="F&B Manager System", layout="wide", page_icon="🍔")
st.title("🍔 Hệ Thống Quản Lý Nhà Hàng (F&B App)")

# Tạo 4 Tab chính theo đúng yêu cầu đề bài
tab1, tab2, tab3, tab4 = st.tabs([
    "🪑 Sơ đồ Bàn", 
    "📜 Thực đơn", 
    "📝 Gọi món (Orders)", 
    "💳 Thanh toán (Checkout)"
])

with tab1:
    render_tables_view()

with tab2:
    render_menu_view()

with tab3:
    render_orders_view()

with tab4:
    render_checkout_view()

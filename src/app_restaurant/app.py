import os
import sys

# =====================================================================
# BỘ KHỞI TẠO ĐƯỜNG DẪN: Sửa lỗi "attempted relative import with no known parent package"
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Ép Python nhận diện thư mục hiện tại như một package cha chính thống
__package__ = os.path.basename(current_dir)
# =====================================================================

import streamlit as st

# Cấu hình Layout hiển thị rộng toàn màn hình
st.set_page_config(layout="wide", page_title="Hệ thống Quản lý Nhà hàng - Project 1", page_icon="🏪")

# Khởi tạo giá trị bàn ăn được chọn lưu trữ xuyên suốt Session State nếu chưa có
if "selected_table" not in st.session_state:
    st.session_state.selected_table = None

# Nhập (Import) các module giao diện thành phần từ thư mục views
from views.tables import render_tables
from views.menu import render_menu_management
from views.orders import render_orders
from views.checkout import render_checkout

# Tiêu đề giao diện chính
st.title("🏪 HỆ THỐNG QUẢN LÝ NHÀ HÀNG - PROJECT 1")
st.caption("Giải pháp vận hành nội bộ phân tầng kiến trúc UI tách biệt hoàn toàn Logic.")

st.markdown("---")

# Dàn layout chia làm 3 cột chính theo yêu cầu đề bài (Sơ đồ Bàn - Đơn hàng & Menu - Thanh toán)
col_left, col_mid, col_right = st.columns([1.2, 1.5, 1.3], gap="large")

# Cột 1: Sơ đồ quản lý trạng thái Bàn ăn
with col_left:
    render_tables()

# Cột 2: Gọi món ăn, xem đơn hàng tạm tính và quản lý danh mục Thực đơn nhà hàng
with col_mid:
    tab_order, tab_menu_config = st.tabs(["🛒 Đơn hàng & Gọi món", "⚙️ Quản lý danh mục Thực đơn"])
    with tab_order:
        render_orders()
    with tab_menu_config:
        render_menu_management()

# Cột 3: Xuất hóa đơn chi tiết, thanh toán in hóa đơn và hoàn trả bàn trống
with col_right:
    render_checkout()

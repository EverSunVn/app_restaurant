<<<<<<< HEAD
import streamlit as st
from app_restaurant.models.base_models import TABLE_DATA
from app_restaurant.controllers.tables_logic import get_table_layout, logic_open_table, logic_close_table

# ... (phần code def render_tables_view() giữ nguyên)
def render_tables_view():
    st.header("🪑 Sơ Đồ Bàn Ăn")

    empty_tables, occupied_tables = get_table_layout()

    col_note1, col_note2, _ = st.columns([1, 1, 3])
    with col_note1:
        st.caption("🟢 **Bàn trống**")
    with col_note2:
        st.caption("🔴 **Đang phục vụ**")

    st.markdown("---")

    cols = st.columns(3)
    for idx, (table_num, table) in enumerate(TABLE_DATA.items()):
        col = cols[idx % 3]
        is_free = table.state # True là bàn trống
        status_color = "🟢" if is_free else "🔴"
        status_text = "Bàn trống" if is_free else "Đang phục vụ"

        with col:
            with st.container(border=True):
                st.subheader(f"{status_color} Bàn số {table.table_number}")
                st.write(f"Trạng thái: **{status_text}**")

                if is_free:
                    if st.button(f"Mở Bàn {table.table_number}", key=f"open_{table_num}", use_container_width=True):
                        _, msg = logic_open_table(table_num)
                        st.success(msg)
                        st.rerun()
                else:
                    if st.button(f"Đóng / Hủy Bàn {table.table_number}", key=f"close_{table_num}", use_container_width=True):
                        _, msg = logic_close_table(table_num)
                        st.info(msg)
                        st.rerun()
=======
import streamlit as st
from app_restaurant.models.base_models import TABLE_DATA
from app_restaurant.controllers.tables_logic import get_table_layout, logic_open_table, logic_close_table

# Cấu hình popup to lên bằng cách gán width="large"
@st.dialog("🎉 Thông báo hệ thống", width="large")
def show_success_dialog(message):
    # Tạo cấu trúc căn giữa, icon tick xanh, tiêu đề và mô tả như ảnh mẫu
    st.markdown(
        f"""
        <div style="text-align: center; padding: 20px 0;">
            <div style="font-size: 70px; color: #4CAF50; margin-bottom: 10px;">✔️</div>
            <h2 style="margin: 0 0 10px 0; color: #333333; font-weight: 600;">Mở bàn thành công!</h2>
            <p style="color: #666666; font-size: 16px; margin-bottom: 25px;">{message}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    # Nút bấm OK xanh dương đồng bộ đại trà ở giữa màn hình
    if st.button("OK", type="primary", use_container_width=True):
        st.rerun()

def render_tables_view():
    st.header("🪑 Sơ Đồ Bàn Ăn")

    empty_tables, occupied_tables = get_table_layout()

    col_note1, col_note2, _ = st.columns(3)
    with col_note1:
        st.caption("🟢 **Bàn trống**")
    with col_note2:
        st.caption("🔴 **Đang phục vụ**")

    st.markdown("---")

    cols = st.columns(3)
    for idx, (table_num, table) in enumerate(TABLE_DATA.items()):
        col = cols[idx % 3]
        is_free = table.state # True là bàn trống
        status_color = "🟢" if is_free else "🔴"
        status_text = "Bàn trống" if is_free else "Đang phục vụ"

        with col:
            with st.container(border=True):
                st.subheader(f"{status_color} Bàn số {table.table_number}")
                st.write(f"Trạng thái: **{status_text}**")

                if is_free:
                    if st.button(f"Mở Bàn {table.table_number}", key=f"open_{table_num}", use_container_width=True):
                        _, msg = logic_open_table(table_num)
                        show_success_dialog(msg)
                else:
                    if st.button(f"Đóng / Hủy Bàn {table.table_number}", key=f"close_{table_num}", use_container_width=True):
                        _, msg = logic_close_table(table_num)
                        st.info(msg)
                        st.rerun()
>>>>>>> Ui/Dat

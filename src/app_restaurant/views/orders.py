import streamlit as st
from app_restaurant.models.base_models import DISHES_DATA
from app_restaurant.controllers.tables_logic import get_table_layout
from app_restaurant.controllers.orders_logic import process_order, undo_process, get_bill_details

# ... (phần code def render_orders_view() giữ nguyên)
def render_orders_view():
    st.header("📝 Gọi Món & Quản Lý Đơn Hàng")

    # Lấy danh sách bàn đang phục vụ (occupied_tables)
    _, occupied_tables = get_table_layout()

    if not occupied_tables:
        st.info("Hiện không có bàn nào đang được mở. Vui lòng sang tab 'Sơ đồ Bàn' để mở bàn trước.")
        return

    # Chọn bàn thao tác
    selected_table = st.selectbox(
        "Chọn bàn cần gọi món:",
        options=occupied_tables,
        format_func=lambda x: f"Bàn số {x}"
    )

    st.markdown("---")
    col_left, col_right = st.columns([1, 1])

    # CỘT TẠO ĐƠN (GỌI MÓN)
    with col_left:
        st.subheader("🛒 Chọn Món Bổ Sung")
        if not DISHES_DATA:
            st.warning("Menu hiện chưa có món nào!")
        else:
            dish_id = st.selectbox(
                "Thực đơn món ăn:",
                options=list(DISHES_DATA.keys()),
                format_func=lambda k: f"{DISHES_DATA[k].name} - {DISHES_DATA[k].cost:,} VNĐ"
            )

            if st.button("➕ Thêm vào đơn hàng", use_container_width=True, type="primary"):
                success, msg = process_order(selected_table, dish_id)
                if success:
                    st.success(msg)
                    st.rerun()
                else:
                    st.error(msg)

    # CỘT HÓA ĐƠN TẠM TÍNH & NÚT UNDO
    with col_right:
        st.subheader(f"🧾 Danh Sách Món - Bàn {selected_table}")
        dishes_list, total_money = get_bill_details(selected_table)

        if dishes_list:
            # Hiển thị danh sách món ăn đã gọi
            items_display = [
                {"STT": idx + 1, "Món ăn": d.name, "Giá": f"{d.cost:,} VNĐ"}
                for idx, d in enumerate(dishes_list)
            ]
            st.table(items_display)
            st.markdown(f"### 💰 **Tổng tạm tính:** `{total_money:,}` VNĐ")

            # Nút Undo (Rút món vừa chọn khỏi Stack)
            if st.button("⏪ Undo (Xóa món vừa thêm gần nhất)", use_container_width=True):
                success, msg = undo_process(selected_table)
                if success:
                    st.warning(msg)
                    st.rerun()
                else:
                    st.error(msg)
        else:
            st.caption("Bàn này chưa gọi món nào.")

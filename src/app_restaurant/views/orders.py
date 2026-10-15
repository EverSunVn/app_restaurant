import streamlit as st
from models.base_models import TABLE_DATA, DISHES_DATA, get_bill
from controllers.orders_logic import goi_mon, undo_mon_vua_them

def render_orders_view():
    """Giao diện Gọi món và Hoàn tác (Undo) bằng Stack"""
    st.header("📝 Quản Lý Đơn Hàng (Gọi Món)")

    # Lọc danh sách các bàn đang phục vụ (state == False)
    occupied_tables = [num for num, table in TABLE_DATA.items() if not table.state]

    if not occupied_tables:
        st.info("Hiện chưa có bàn nào 'Đang phục vụ'. Vui lòng sang tab 'Sơ đồ Bàn' để mở bàn trước.")
        return

    # Tự động chọn bàn vừa bấm bên tab Sơ đồ bàn (nếu có)
    default_index = 0
    if "selected_table_number" in st.session_state and st.session_state["selected_table_number"] in occupied_tables:
        default_index = occupied_tables.index(st.session_state["selected_table_number"])

    selected_table = st.selectbox(
        "Chọn bàn để thực hiện gọi món:", 
        options=occupied_tables, 
        index=default_index,
        format_func=lambda x: f"Bàn số {x}"
    )
    st.session_state["selected_table_number"] = selected_table

    st.markdown("---")
    col_menu, col_bill = st.columns([1, 1])

    # CỘT 1: THỰC ĐƠN GỌI MÓN
    with col_menu:
        st.subheader("🛒 Chọn Món Ăn")
        if not DISHES_DATA:
            st.warning("Thực đơn hiện đang trống!")
        else:
            dish_id = st.selectbox(
                "Danh sách món ăn",
                options=list(DISHES_DATA.keys()),
                format_func=lambda k: f"{DISHES_DATA[k].name} ({DISHES_DATA[k].cost:,} VNĐ)"
            )
            
            if st.button("➕ Thêm vào đơn", use_container_width=True):
                success, msg = goi_mon(selected_table, dish_id)
                if success:
                    st.success(msg)
                    st.rerun()
                else:
                    st.error(msg)

    # CỘT 2: HÓA ĐƠN TẠM TÍNH & NÚT UNDO (STACK)
    with col_bill:
        st.subheader(f"🧾 Hóa Đơn Tạm Tính - Bàn {selected_table}")
        bill = get_bill(selected_table)

        if bill.dishes_list:
            # Hiển thị danh sách món (món mới thêm nằm ở đầu danh sách - trực quan hóa Stack)
            items_display = [
                {"Món": d.name, "Giá": f"{d.cost:,} VNĐ"} 
                for d in reversed(bill.dishes_list)
            ]
            st.table(items_display)
            
            st.markdown(f"### 💰 **Tổng tiền tạm tính:** `{bill.total_money:,}` VNĐ")
            
            # NÚT UNDO (CẤU TRÚC STACK - POP)
            if st.button("⏪ Undo (Hoàn tác món vừa thêm)", type="secondary", use_container_width=True):
                success, msg = undo_mon_vua_them(selected_table)
                if success:
                    st.info(msg)
                    st.rerun()
                else:
                    st.error(msg)
        else:
            st.caption("Bàn này hiện chưa gọi món nào.")

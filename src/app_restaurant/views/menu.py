import streamlit as st
from app_restaurant.controllers.menu_logic import logic_get_all_dishes, logic_add_dish, logic_delete_dish

# ... (phần code def render_menu_view() giữ nguyên)
def render_menu_view():
    st.header("📜 Quản Lý Thực Đơn")

    tab1, tab2 = st.tabs(["📋 Danh Sách Món", "➕ Thêm / Xóa Món"])
    dishes_data = logic_get_all_dishes()

    with tab1:
        table_data = [
            {"Mã món": dish_id, "Tên món": dish.name, "Giá": f"{dish.cost:,} VNĐ"}
            for dish_id, dish in dishes_data.items()
        ]
        if table_data:
            st.dataframe(table_data, use_container_width=True)
        else:
            st.info("Thực đơn đang trống.")

    with tab2:
        col_add, col_del = st.columns(2)
        with col_add:
            st.subheader("Thêm Món Mới")
            with st.form("add_dish_form", clear_on_submit=True):
                d_id = st.text_input("Mã món (VD: 101)")
                d_name = st.text_input("Tên món")
                d_cost = st.number_input("Giá tiền (VNĐ)", min_value=0, step=1000, value=30000)
                if st.form_submit_button("Thêm Món"):
                    ok, msg = logic_add_dish(d_id, d_name, int(d_cost))
                    if ok:
                        st.success(msg)
                        st.rerun()
                    else:
                        st.error(msg)

        with col_del:
            st.subheader("Xóa Món Khỏi Menu")
            if dishes_data:
                del_id = st.selectbox("Chọn món xóa:", options=list(dishes_data.keys()), format_func=lambda x: f"{x} - {dishes_data[x].name}")
                if st.button("Xóa Món", type="primary"):
                    ok, msg = logic_delete_dish(del_id)
                    if ok:
                        st.success(msg)
                        st.rerun()
                    else:
                        st.error(msg)
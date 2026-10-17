import streamlit as st
from controllers import menu_logic

def render_menu_management():
    st.markdown("### 📋 Quản lý Thực đơn (Menu)")
    
    # Lấy toàn bộ danh sách món ăn hiện tại
    dishes = menu_logic.logic_get_all_dishes()
    
    # Hiển thị bảng danh mục món ăn hiện tại
    st.write("**Thực đơn hiện tại của nhà hàng:**")
    menu_data = []
    for dish_id, dish in dishes.items():
        menu_data.append({"Mã món": dish_id, "Tên món": dish.name, "Giá tiền (VNĐ)": f"{dish.cost:,}"})
        
    if menu_data:
        st.dataframe(menu_data, use_container_width=True, hide_index=True)
    else:
        st.info("Thực đơn trống. Vui lòng thêm món ăn mới!")

    # Các Tab phân chia chức năng Thêm / Sửa / Xóa món ăn
    tab_add, tab_edit, tab_delete = st.tabs(["➕ Thêm món", "✏️ Sửa món", "❌ Xóa món"])
    
    with tab_add:
        with st.form("form_add_dish", clear_on_submit=True):
            new_id = st.text_input("Nhập mã món ăn (VD: BunCha)")
            new_name = st.text_input("Nhập tên món ăn")
            new_cost = st.number_input("Nhập giá tiền", min_value=0, step=5000, value=0)
            
            if st.form_submit_button("Xác nhận thêm"):
                if not new_id or not new_name:
                    st.error("Vui lòng không bỏ trống mã món và tên món!")
                else:
                    success, msg = menu_logic.logic_add_dish(new_id, new_name, new_cost)
                    if success:
                        st.success(msg)
                        st.rerun()
                    else:
                        st.error(msg)

    with tab_edit:
        if dishes:
            with st.form("form_update_dish"):
                edit_id = st.selectbox("Chọn mã món cần chỉnh sửa", list(dishes.keys()))
                edit_name = st.text_input("Tên món mới (Để trống nếu giữ nguyên)")
                edit_cost = st.number_input("Giá tiền mới", min_value=0, step=5000, value=int(dishes[edit_id].cost))
                
                if st.form_submit_button("Cập nhật món"):
                    success, msg = menu_logic.logic_update_dish(
                        edit_id, 
                        new_name=edit_name if edit_name else None, 
                        new_cost=edit_cost
                    )
                    if success:
                        st.success(msg)
                        st.rerun()
                    else:
                        st.error(msg)
        else:
            st.caption("Không có món ăn nào để chỉnh sửa.")

    with tab_delete:
        if dishes:
            with st.form("form_delete_dish"):
                del_id = st.selectbox("Chọn món ăn muốn gỡ bỏ", list(dishes.keys()), key="sb_del")
                if st.form_submit_button("Xác nhận xóa món", type="primary"):
                    success, msg = menu_logic.logic_delete_dish(del_id)
                    if success:
                        st.success(msg)
                        st.rerun()
                    else:
                        st.error(msg)
        else:
            st.caption("Không có món ăn nào để xóa.")

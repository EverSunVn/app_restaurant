import streamlit as st
from controllers import tables_logic

def render_tables():
    st.markdown("### 🗺️ Sơ đồ Bàn")
    
    # Lấy danh sách bàn trống và bàn đang có người từ backend logic
    empty_tables, occupied_tables = tables_logic.get_table_layout()
    all_tables = sorted(list(empty_tables) + list(occupied_tables))
    
    if not all_tables:
        st.info("Không tìm thấy dữ liệu bàn ăn.")
        return

    # Hiển thị lưới danh sách bàn ăn (chia làm 3 cột hiển thị)
    cols = st.columns(3)
    for i, t_num in enumerate(all_tables):
        is_empty = t_num in empty_tables
        color_icon = "🟢" if is_empty else "🔴"
        status_text = "Trống" if is_empty else "Phục vụ"
        
        # Nhãn hiển thị trạng thái bàn ăn
        label = f"{color_icon} Bàn {t_num}\n({status_text})"
        
        # Đánh dấu sao nếu bàn đó đang được click chọn hiện tại
        if st.session_state.get("selected_table") == t_num:
            label = f"⭐ {label}"
            
        with cols[i % 3]:
            if st.button(label, key=f"btn_table_{t_num}", use_container_width=True):
                st.session_state.selected_table = t_num
                st.rerun()

    st.markdown("---")
    
    # Khu vực thao tác Mở/Đóng nhanh trạng thái bàn ăn đang chọn
    selected = st.session_state.get("selected_table")
    if selected:
        st.write(f"👉 **Bàn đang tương tác: Bàn {selected}**")
        c1, c2 = st.columns(2)
        
        with c1:
            if selected in empty_tables:
                if st.button("🚀 Mở bàn phục vụ", key="open_table_btn", type="primary", use_container_width=True):
                    table, msg = tables_logic.logic_open_table(selected)
                    if table:
                        st.success(msg)
                    else:
                        st.error(msg)
                    st.rerun()
                    
        with c2:
            if selected in occupied_tables:
                if st.button("🗑️ Đóng / Hủy bàn", key="close_table_btn", type="secondary", use_container_width=True):
                    success, msg = tables_logic.logic_close_table(selected)
                    if success:
                        st.success(msg)
                        if st.session_state.selected_table == selected:
                            st.session_state.selected_table = None
                    else:
                        st.error(msg)
                    st.rerun()

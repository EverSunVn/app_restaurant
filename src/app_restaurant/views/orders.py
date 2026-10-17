import streamlit as st
from controllers import orders_logic
from models import base_models as BaseModel

def render_orders():
    st.markdown("### 🛒 Đơn hàng & Gọi món")
    selected_table = st.session_state.get("selected_table")
    
    if not selected_table:
        st.info("💡 Vui lòng lựa chọn một Bàn ăn ở cột Sơ đồ Bàn để thực hiện gọi món.")
        return

    st.markdown(f"🎯 **Đang thực hiện cho: Bàn {selected_table}**")
    
    # 1. Khu vực hiển thị thực đơn gọi món nhanh
    st.write("**Chọn món để thêm vào bàn:**")
    dishes = BaseModel.DISHES_DATA
    
    if not dishes:
        st.warning("Thực đơn trống! Hãy tạo món ăn trong tab Quản lý thực đơn trước.")
    else:
        for dish_id, dish in dishes.items():
            c_name, c_action = st.columns(2)
            c_name.write(f"▪️ {dish.name} (`{dish.cost:,}` VNĐ)")
            if c_action.button("➕ Thêm", key=f"add_{dish_id}_{selected_table}"):
                success, msg = orders_logic.process_order(selected_table, dish_id)
                if success:
                    st.success(msg)
                    st.rerun()
                else:
                    st.error(msg)

    st.markdown("---")
    
    # 2. Khu vực hiển thị Hóa đơn tạm tính hiện tại & Stack Undo
    st.write("🧾 **Danh sách món đã chọn (Tạm tính):**")
    dishes_list, total_money = orders_logic.get_bill_details(selected_table)
    
    if dishes_list:
        for idx, item in enumerate(dishes_list):
            st.text(f" {idx + 1}. {item.name} - {item.cost:,} VNĐ")
            
        st.markdown(f"💵 **Tổng tiền tạm tính:** `{total_money:,}` VNĐ")
        
        # Nút bấm Hoàn tác (Undo món ăn cuối cùng sử dụng cấu trúc dữ liệu Stack trong backend)
        if st.button("↩️ Hoàn tác (Undo)", key=f"undo_{selected_table}", type="secondary", use_container_width=True):
            success, msg = orders_logic.undo_process(selected_table)
            if success:
                st.success(msg)
                st.rerun()
            else:
                st.error(msg)
    else:
        st.caption("Chưa có món ăn nào được gọi cho bàn này.")

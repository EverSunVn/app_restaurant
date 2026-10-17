import streamlit as st
from controllers import checkout_logic

def render_checkout():
    st.markdown("### 💳 Thanh toán")
    selected_table = st.session_state.get("selected_table")
    
    if not selected_table:
        st.info("💡 Lựa chọn bàn ăn cần tính tiền để xuất hóa đơn.")
        return

    st.markdown(f"🏁 **Tính tiền cho: Bàn {selected_table}**")
    
    # Lấy thông tin hóa đơn thanh toán cuối cùng từ backend checkout_logic
    success, msg, dishes_list, total_money = checkout_logic.logic_get_checkout_info(selected_table)
    
    if not success:
        st.warning(msg)
        return
        
    if dishes_list:
        st.write("📋 **Hóa đơn xuất kho chi tiết:**")
        bill_summary = []
        for item in dishes_list:
            bill_summary.append({"Tên món": item.name, "Giá": f"{item.cost:,} VNĐ"})
        st.table(bill_summary)
        
        st.markdown(f"### 🧾 TỔNG TIỀN: `{total_money:,}` VNĐ")
        
        # Thực hiện thanh toán và xóa trạng thái đơn hàng để đưa bàn về trạng thái Trống
        if st.button("🖨️ Thanh toán & In hóa đơn", key=f"chk_btn_{selected_table}", type="primary", use_container_width=True):
            ok, checkout_msg = checkout_logic.logic_process_checkout(selected_table)
            if ok:
                st.success(checkout_msg)
                st.balloons()
                st.session_state.selected_table = None  # Reset lại lựa chọn bàn ăn
                st.rerun()
            else:
                st.error(checkout_msg)
    else:
        st.info("Bàn trống hoặc chưa có món ăn nào để thực hiện thanh toán.")

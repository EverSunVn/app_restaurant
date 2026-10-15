import streamlit as st
from models.base_models import TABLE_DATA, get_bill
from controllers.checkout_logic import xu_ly_thanh_toan

def render_checkout_view():
    """Giao diện Thanh toán & In hóa đơn"""
    st.header("💳 Thanh Toán & In Hóa Đơn")

    # Lọc danh sách các bàn đang phục vụ
    occupied_tables = [num for num, table in TABLE_DATA.items() if not table.state]

    if not occupied_tables:
        st.info("Hiện không có bàn nào đang hoạt động để thanh toán.")
        return

    selected_table = st.selectbox(
        "Chọn bàn cần thanh toán:", 
        options=occupied_tables, 
        format_func=lambda x: f"Bàn số {x}"
    )
    
    bill = get_bill(selected_table)

    st.markdown("---")
    st.subheader(f"📄 Hóa Đơn Chi Tiết - Bàn số {selected_table}")

    if not bill.dishes_list:
        st.warning("Bàn này chưa gọi món nào!")
        return

    # Hiển thị bảng kê chi tiết các món
    items_display = [
        {"STT": idx + 1, "Tên món": d.name, "Đơn giá": f"{d.cost:,} VNĐ"} 
        for idx, d in enumerate(bill.dishes_list)
    ]
    st.table(items_display)

    st.markdown(f"### 💵 **Tổng số tiền phải thanh toán:** `{bill.total_money:,}` VNĐ")

    st.markdown("---")
    
    # Bước xác nhận an toàn ("Are you sure?") để chống bấm nhầm
    confirm = st.checkbox("Khách hàng đã thanh toán đủ tiền và sẵn sàng dọn bàn")

    if st.button("🧾 Thanh toán & In hóa đơn", type="primary", disabled=not confirm, use_container_width=True):
        success, msg, total = xu_ly_thanh_toan(selected_table)
        if success:
            st.balloons()
            st.success(f"{msg}\nTổng hóa đơn: {total:,} VNĐ. Bàn {selected_table} đã được trả về trạng thái 'Bàn trống'!")
            st.rerun()
        else:
            st.error(msg)

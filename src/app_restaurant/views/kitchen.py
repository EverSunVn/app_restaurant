import streamlit as st
from app_restaurant.controllers.kitchen_logic import get_pending_orders

# Cấu hình popup to lên bằng cách gán width="large"
@st.dialog("👨‍🍳 Thông báo nhà bếp", width="large")
def show_kitchen_dialog(message):
    st.markdown(
        f"""
        <div style="text-align: center; padding: 20px 0;">
            <div style="font-size: 70px; color: #4CAF50; margin-bottom: 10px;">✔️</div>
            <h2 style="margin: 0 0 10px 0; color: #333333; font-weight: 600;">Hoàn thành món ăn!</h2>
            <p style="color: #666666; font-size: 16px; margin-bottom: 25px;">{message}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("OK", type="primary", use_container_width=True):
        st.rerun()

def render_kitchen_view():
    st.header("👨‍🍳 Quản Lý Nhà Bếp")

    queue = get_pending_orders()

    if not queue:
        st.success("Hiện tại không có đơn hàng nào đang chờ.")
        return

    grouped_orders = {}

    for order in queue:
        table_number = order["table_number"]
        dish_name = order["dish_name"]

        if table_number not in grouped_orders:
            grouped_orders[table_number] = []

        grouped_orders[table_number].append(dish_name)

    total_tables = len(grouped_orders)
    total_dishes = len(queue)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Số bàn đang chờ", total_tables)

    with col2:
        st.metric("Tổng số món", total_dishes)

    st.markdown("---")

    table_numbers = list(grouped_orders.keys())
    current_table = table_numbers[0]

    for index, table_number in enumerate(table_numbers):

        dishes = grouped_orders[table_number]
        is_current = index == 0

        with st.container(border=True):

            if is_current:
                st.subheader(f"🔥 ĐANG LÀM - BÀN {table_number}")
            else:
                st.subheader(f"⏳ CHỜ LÀM - BÀN {table_number}")

            st.caption(f"Tổng cộng: {len(dishes)} món")

            for dish_index, dish_name in enumerate(dishes, start=1):
                st.write(f"{dish_index}. {dish_name}")

            if is_current:
                if st.button(
                    f"✅ HOÀN THÀNH BÀN {table_number}",
                    key=f"complete_table_{table_number}",
                    type="primary",
                    use_container_width=True
                ):
                    queue[:] = [
                        order for order in queue
                        if order["table_number"] != table_number
                    ]
                    show_kitchen_dialog(f"Đã hoàn thành tất cả món ăn và chuẩn bị giao cho Bàn {table_number}!")

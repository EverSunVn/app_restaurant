import streamlit as st
from app_restaurant.controllers.kitchen_logic import get_pending_orders


def render_kitchen_view():
    st.header("👨‍🍳 Quản Lý Nhà Bếp")

    queue = get_pending_orders()

    if not queue:
        st.success("Hiện tại không có đơn hàng nào đang chờ.")
        return

    # Gom các món theo bàn, giữ nguyên thứ tự bàn được gọi đầu tiên
    grouped_orders = {}

    for order in queue:
        table_number = order["table_number"]
        dish_name = order["dish_name"]

        if table_number not in grouped_orders:
            grouped_orders[table_number] = []

        grouped_orders[table_number].append(dish_name)

    # Hiển thị tổng số bàn và tổng số món
    total_tables = len(grouped_orders)
    total_dishes = len(queue)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Số bàn đang chờ", total_tables)

    with col2:
        st.metric("Tổng số món", total_dishes)

    st.markdown("---")

    # Lấy bàn đầu tiên làm bàn đang thực hiện
    table_numbers = list(grouped_orders.keys())
    current_table = table_numbers[0]

    # Hiển thị từng bàn
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
                    # Xóa toàn bộ món thuộc bàn vừa hoàn thành
                    queue[:] = [
                        order for order in queue
                        if order["table_number"] != table_number
                    ]

                    st.success(
                        f"Đã hoàn thành tất cả món của Bàn {table_number}!"
                    )
                    st.rerun()
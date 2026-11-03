
import streamlit as st

from app_restaurant.controllers.kitchen_logic import (
    get_pending_orders,
    complete_next_order
)


def render_kitchen_view():
    st.header("👨‍🍳 Quản Lý Nhà Bếp")

    pending_orders = get_pending_orders()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="📋 Đơn hàng đang chờ",
            value=len(pending_orders)
        )

    with col2:
        if pending_orders:
            st.metric(
                label="⏳ Đơn hàng tiếp theo",
                value="Bàn " + str(pending_orders[0]["table_number"])
            )
        else:
            st.metric(
                label="⏳ Đơn hàng tiếp theo",
                value="Không có"
            )

    st.markdown("---")

    st.subheader("🍳 Danh Sách Món Cần Chế Biến")

    if not pending_orders:
        st.info("Hiện tại không có món ăn nào cần chế biến.")
        return
    
    for index, order in enumerate(pending_orders):

        table_number = order["table_number"]
        dish_name = order["dish_name"]

        with st.container(border=True):

            col1, col2, col3 = st.columns([1, 3, 1])

            with col1:
                st.subheader(f"#{index + 1}")

            with col2:
                st.markdown(f"**🍽️ {dish_name}**")
                st.caption(f"📍 Bàn số {table_number}")

                if index == 0:
                    st.success("Đơn hàng tiếp theo cần chế biến")
                else:
                    st.caption("Đang chờ chế biến")

            with col3:
                if index == 0:
                    st.markdown("### 🔥")
                else:
                    st.markdown("### ⏳")

    st.markdown("---")

    st.subheader("✅ Xử Lý Đơn Hàng")

    if st.button(
        "Hoàn Thành Món Tiếp Theo",
        type="primary",
        use_container_width=True
    ):

        success, message = complete_next_order()

        if success:
            st.success(message)
            st.rerun()
        else:
            st.error(message)

    if st.button("🔄 Làm Mới Danh Sách", use_container_width=True):
        st.rerun()

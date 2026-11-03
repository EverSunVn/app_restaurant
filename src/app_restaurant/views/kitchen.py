
import streamlit as st

from app_restaurant.models import base_models as BaseModel

# Đảm bảo hàng đợi tồn tại trước khi import kitchen_logic
if not hasattr(BaseModel, "KITCHEN_QUEUE"):
    BaseModel.KITCHEN_QUEUE = []

from app_restaurant.controllers.kitchen_logic import (
    get_pending_orders,
    complete_next_order
)


def render_kitchen_view():

    # Tiêu đề và số lượng đơn hàng
    col_title, col_count = st.columns([4, 1])

    with col_title:
        st.header("👨‍🍳 QUẢN LÝ NHÀ BẾP")

    with col_count:
        pending_orders = get_pending_orders()

        st.metric(
            label="Tổng đơn hàng",
            value=len(pending_orders)
        )

    st.markdown("---")

    # Chia giao diện thành hai khu vực
    col_doing, col_waiting = st.columns([1, 1])

    # ==================================================
    # ĐANG LÀM
    # ==================================================

    with col_doing:

        st.subheader("🔥 ĐANG LÀM")

        if pending_orders:

            # FIFO: Đơn đầu tiên luôn được ưu tiên chế biến
            current_order = pending_orders[0]

            with st.container(border=True):

                st.markdown(
                    f"### 🍽️ {current_order['dish_name']}"
                )

                st.markdown(
                    f"**📍 Bàn số {current_order['table_number']}**"
                )

                st.caption("Đơn hàng được đặt sớm nhất")

                st.markdown("---")

                if st.button(
                    "✅ XONG",
                    key="complete_current_order",
                    type="primary",
                    use_container_width=True
                ):

                    success, message = complete_next_order()

                    if success:
                        st.success(message)
                        st.rerun()
                    else:
                        st.error(message)

        else:

            st.info("Hiện chưa có món nào đang chế biến.")

    # ==================================================
    # CHỜ LÀM
    # ==================================================

    with col_waiting:

        st.subheader("⏳ CHỜ LÀM")

        # Bỏ qua đơn đầu tiên vì nó đang được chế biến
        waiting_orders = pending_orders[1:]

        if waiting_orders:

            for index, order in enumerate(waiting_orders):

                with st.container(border=True):

                    st.markdown(
                        f"**🍽️ {order['dish_name']}**"
                    )

                    st.markdown(
                        f"📍 Bàn số {order['table_number']}"
                    )

                    st.caption(
                        f"Vị trí chờ: {index + 1}"
                    )

        else:

            st.info("Không có đơn hàng nào đang chờ.")

    # ==================================================
    # LÀM MỚI
    # ==================================================

    st.markdown("---")

    if st.button(
        "🔄 Làm mới danh sách",
        use_container_width=True
    ):
        st.rerun()

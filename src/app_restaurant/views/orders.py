
import streamlit as st

from app_restaurant.models.base_models import DISHES_DATA
from app_restaurant.controllers.tables_logic import get_table_layout
from app_restaurant.controllers.orders_logic import (
    process_order,
    undo_process,
    get_bill_details
)


def render_orders_view():
    st.header("📝 Gọi Món & Quản Lý Đơn Hàng")

    # Lấy danh sách bàn đang phục vụ
    _, occupied_tables = get_table_layout()

    if not occupied_tables:
        st.info(
            "Hiện không có bàn nào đang được mở. "
            "Vui lòng sang tab 'Sơ đồ Bàn' để mở bàn trước."
        )
        return

    # Chọn bàn thao tác
    selected_table = st.selectbox(
        "Chọn bàn cần gọi món:",
        options=occupied_tables,
        format_func=lambda x: f"Bàn số {x}"
    )

    st.markdown("---")

    col_left, col_right = st.columns([1, 1])

    # ==========================================
    # CỘT TRÁI: DANH SÁCH MENU VÀ GỌI MÓN
    # ==========================================
    with col_left:
        st.subheader("🛒 Thực Đơn")

        if not DISHES_DATA:
            st.warning("Menu hiện chưa có món nào!")

        else:
            # Hiển thị toàn bộ món ăn trong menu
            for dish_id, dish in DISHES_DATA.items():

                with st.container(border=True):
                    col_name, col_price, col_button = st.columns(
                        [3, 2, 1]
                    )

                    with col_name:
                        st.write(f"**{dish.name}**")

                    with col_price:
                        st.write(f"{dish.cost:,} VNĐ")

                    with col_button:
                        if st.button(
                            "➕",
                            key=f"add_dish_{selected_table}_{dish_id}",
                            help=f"Thêm {dish.name} vào đơn hàng"
                        ):
                            success, msg = process_order(
                                selected_table,
                                dish_id
                            )

                            if success:
                                st.success(msg)
                                st.rerun()
                            else:
                                st.error(msg)

    # ==========================================
    # CỘT PHẢI: HÓA ĐƠN TẠM TÍNH VÀ UNDO
    # ==========================================
    with col_right:
        st.subheader(f"🧾 Danh Sách Món - Bàn {selected_table}")

        dishes_list, total_money = get_bill_details(selected_table)

        if dishes_list:

            # Hiển thị danh sách món ăn đã gọi
            items_display = [
                {
                    "STT": idx + 1,
                    "Món ăn": dish.name,
                    "Giá": f"{dish.cost:,} VNĐ"
                }
                for idx, dish in enumerate(dishes_list)
            ]

            st.table(items_display)

            # Tổng tiền tạm tính
            st.markdown(
                f"### 💰 **Tổng tạm tính:** `{total_money:,}` VNĐ"
            )

            # Nút Undo: xóa món vừa thêm gần nhất
            if st.button(
                "⏪ Undo (Xóa món vừa thêm gần nhất)",
                use_container_width=True
            ):
                success, msg = undo_process(selected_table)

                if success:
                    st.warning(msg)
                    st.rerun()
                else:
                    st.error(msg)

        else:
            st.caption("Bàn này chưa gọi món nào.")

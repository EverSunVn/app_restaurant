import streamlit as st
from app_restaurant.models.base_models import Table, TABLE_DATA
from app_restaurant.controllers.tables_logic import get_table_layout
from app_restaurant.controllers.checkout_logic import logic_get_checkout_info, logic_process_checkout

# ==============================================================================
# MONKEY PATCH (XỬ LÝ THUẦN UI):
# Tự động gắn thuộc tính 'id' cho Class Table và các object Table trên RAM.
# Giúp checkout_logic.py gọi table.id không bị văng lỗi AttributeError
# mà KHÔNG CẦN CHỈNH SỬA BẤT KỲ FILE LOGIC NÀO CỦA TEAM.
# ==============================================================================
if not hasattr(Table, 'id'):
    Table.id = property(lambda self: getattr(self, 'table_number', getattr(self, '_table_number', None)))

for t in TABLE_DATA.values():
    if not hasattr(t, 'id'):
        setattr(t, 'id', getattr(t, 'table_number', getattr(t, '_table_number', None)))


def render_checkout_view():
    st.header("💳 Thanh Toán & In Hóa Đơn")

    _, occupied_tables = get_table_layout()

    if not occupied_tables:
        st.info("Không có bàn nào đang hoạt động để thanh toán.")
        return

    selected_table = st.selectbox(
        "Chọn bàn cần thanh toán:",
        options=occupied_tables,
        format_func=lambda x: f"Bàn số {x}"
    )

    # Đảm bảo object của bàn được chọn có sẵn thuộc tính id
    target_table = TABLE_DATA.get(selected_table)
    if target_table and not hasattr(target_table, 'id'):
        setattr(target_table, 'id', selected_table)

    # Gọi logic kiểm tra hóa đơn từ controller
    try:
        success, msg, dishes_list, total_money = logic_get_checkout_info(selected_table)
    except Exception as e:
        st.error(f"Lỗi xử lý hóa đơn: {e}")
        return

    st.markdown("---")
    st.subheader(f"📄 Chi Tiết Hóa Đơn - Bàn {selected_table}")

    if not success:
        st.error(msg)
        return

    if dishes_list:
        items_display = [
            {"STT": idx + 1, "Tên món": d.name, "Đơn giá": f"{d.cost:,} VNĐ"}
            for idx, d in enumerate(dishes_list)
        ]
        st.table(items_display)
    else:
        st.caption("Bàn này chưa chọn món ăn nào.")

    st.markdown(f"### 💵 **Tổng tiền cần thanh toán:** `{total_money:,}` VNĐ")
    st.markdown("---")

    confirm = st.checkbox("Đã nhận đủ tiền từ khách hàng")

    if st.button("🧾 Xác Nhận Thanh Toán & Dọn Bàn", type="primary", disabled=not confirm, use_container_width=True):
        try:
            ok, res_msg = logic_process_checkout(selected_table)
            if ok:
                st.balloons()
                st.success(res_msg)
                st.rerun()
            else:
                st.error(res_msg)
        except Exception as e:
            st.error(f"Lỗi thanh toán: {e}")
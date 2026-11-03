import streamlit as st
from app_restaurant.models.base_models import Table, TABLE_DATA
from app_restaurant.controllers.tables_logic import get_table_layout
from app_restaurant.controllers.checkout_logic import logic_get_checkout_info, logic_process_checkout

if not hasattr(Table, 'id'):
    Table.id = property(lambda self: getattr(self, 'table_number', getattr(self, '_table_number', None)))

for t in TABLE_DATA.values():
    if not hasattr(t, 'id'):
        setattr(t, 'id', getattr(t, 'table_number', getattr(t, '_table_number', None)))

# Cấu hình popup to lên bằng cách gán width="large"
@st.dialog("💳 Hóa đơn điện tử", width="large")
def show_checkout_dialog(message):
    st.balloons()
    st.markdown(
        f"""
        <div style="text-align: center; padding: 20px 0;">
            <div style="font-size: 70px; color: #4CAF50; margin-bottom: 10px;">✔️</div>
            <h2 style="margin: 0 0 10px 0; color: #333333; font-weight: 600;">Thanh toán thành công!</h2>
            <p style="color: #666666; font-size: 16px; margin-bottom: 25px;">{message}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("OK", type="primary", use_container_width=True):
        st.rerun()

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

    target_table = TABLE_DATA.get(selected_table)
    if target_table and not hasattr(target_table, 'id'):
        setattr(target_table, 'id', selected_table)

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
                show_checkout_dialog(res_msg)
            else:
                st.error(res_msg)
        except Exception as e:
            st.error(f"Lỗi thanh toán: {e}")

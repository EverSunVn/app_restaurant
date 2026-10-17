# 🍔 Hệ Thống Quản Lý Nhà Hàng (F&B Management App)

> **Một ứng dụng quản lý nhà hàng thu nhỏ được xây dựng trên nền tảng Python, tối ưu giao diện trực quan bằng Streamlit và tổ chức mã nguồn khoa học theo mô hình MVC (Model-View-Controller).**

---
## 👥 Thông Tin Đề Tài & Thành Viên Nhóm (AI DUT)

Dự án này là sản phẩm bài tập dự án thuộc chương 1  **AI DUT**, được thực hiện và vận hành dưới sự dẫn dắt của Mentor cùng tập thể các thành viên:

*   **Người hướng dẫn (Mentor):**
    *   👑 **Thành Danh**
*   **Các thành viên thực hiện dự án (Members):**
    *   🧑‍💻 **Võ Nguyễn Đình Dương** 
    *   🧑‍💻 **Huỳnh Văn Trường** 
    *   🧑‍💻 **Thành Phát**
    *   🧑‍💻 **Đặng Tuấn Đạt**

---
## 🛠️ Vai Trò
### 1. Dương: Quản lý nhóm, phân vai trò cho mọi người, thiết kế kiến trúc hệ thống và dựng bố cục cấu trúc thư mục ban đầu dự án, xây dựng tầng dữ liệu cơ sở và chấp nhận pull request của mọi người
### 2. Trường: Xử lý logic vận hành bàn ăn, đơn hàng, order và checkout
### 3. Phát: Thiết kế kiến trúc hệ thống UI
### 4. Đạt: Xây dựng tài liệu hướng dẫn sử dụng 
---
## 📁 Cấu Trúc Thư Mục Chi Tiết

```text
├── controllers/          # Tầng điều hướng và xử lý logic tính toán
│   ├── checkout_logic.py # Kiểm tra hóa đơn, xử lý dọn bàn và hoàn tất thu tiền
│   ├── menu_logic.py     # Xử lý logic nghiệp vụ thêm, sửa, xóa món ăn
│   ├── orders_logic.py   # Quản lý nạp món vào bill, tính tổng tiền và stack undo
│   └── tables_logic.py   # Thay đổi trạng thái vật lý đóng/mở bàn ăn
├── models/               # Tầng định nghĩa thực thể cấu trúc và dữ liệu hệ thống
│   ├── base_models.py    # Định nghĩa Class OOP (Dishes, Table, Bill) và đọc JSON
│   └── data.json         # Cơ sở dữ liệu gốc lưu trữ thông tin món ăn và bàn
├── views/                # Tầng thiết kế giao diện người dùng (Streamlit UI)
│   ├── tables.py | menu.py | orders.py | checkout.py 
└── app.py                # Điểm khởi chạy (Entrypoint) dự án
---
## 🛠️ Hướng Dẫn Cài Đặt (Installation)

Hãy làm theo các bước sau để thiết lập môi trường và chạy thử nghiệm dự án:

### Bước 1: Tải mã nguồn về máy
Đảm bảo bạn đã có cấu trúc thư mục hoàn chỉnh bao gồm các thư mục (`controllers/`, `models/`, `views/`) và file khởi chạy `app.py`.
File zip: (Bổ sung khi xong dự án)

### Bước 2: Cài đặt thư viện Streamlit
Mở terminal (hoặc Command Prompt / Git Bash) và chạy lệnh cài đặt giao diện:
```bash
pip install streamlit
```

### Bước 3: Khởi động ứng dụng
Di chuyển dòng lệnh của terminal vào đúng thư mục gốc của dự án (nơi chứa file `app.py`) và kích hoạt bằng lệnh:
```bash
streamlit run app.py
```
*Sau khi chạy lệnh, một trang web cục bộ sẽ tự động mở ra trên trình duyệt tại địa chỉ `http://localhost:8501`.*

---




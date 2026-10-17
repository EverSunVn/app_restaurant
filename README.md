# 🍔 Hệ Thống Quản Lý Nhà Hàng (F&B Management App)

> **Một ứng dụng quản lý nhà hàng thu nhỏ được xây dựng trên nền tảng Python, tối ưu giao diện trực quan bằng Streamlit và tổ chức mã nguồn khoa học theo mô hình MVC (Model-View-Controller).**

---

## 👥 Thông Tin Đề Tài & Thành Viên Nhóm (AI DUT)

Dự án này là sản phẩm bài tập dự án thuộc **Chương 1 - AI DUT**, được thực hiện và vận hành dưới sự dẫn dắt của Mentor cùng tập thể các thành viên:

*   **Người hướng dẫn (Mentor):**
    *   👑 **Thành Danh**
*   **Các thành viên thực hiện dự án (Members):**
    *   🧑‍💻 **Võ Nguyễn Đình Dương**
    *   🧑‍💻 **Huỳnh Văn Trường**
    *   🧑‍💻 **Thành Phát**
    *   🧑‍💻 **Đặng Tuấn Đạt**

---

## 🎖️ Vai Trò & Nhiệm Vụ Chi Tiết

### 🛠️ 1. Võ Nguyễn Đình Dương
*   **Vị trí:** Quản lý nhóm (Team Leader) & Core Architect.
*   **Nhiệm vụ:** 
    *   Điều phối dự án, phân chia vai trò và nhiệm vụ cụ thể cho từng thành viên.
    *   Thiết kế kiến trúc hệ thống, dựng bố cục và cấu trúc thư mục ban đầu cho dự án.
    *   Xây dựng nền tảng tầng dữ liệu cơ sở (`models/`).
    *   Kiểm duyệt mã nguồn và chấp nhận các yêu cầu hợp nhất dữ liệu (`Pull Requests`) từ các thành viên.

### 🧠 2. Huỳnh Văn Trường
*   **Vị trí:** Backend Logic Engineer.
*   **Nhiệm vụ:**
    *   Xử lý toàn bộ logic vận hành và chuyển đổi trạng thái của bàn ăn (`tables_logic.py`).
    *   Xây dựng hệ thống tiếp nhận, xử lý đơn hàng và gọi món ăn (`orders_logic.py`).
    *   Lập trình thuật toán kiểm tra hóa đơn và hoàn tất quy trình thanh toán (`checkout_logic.py`).

### 🎨 3. Thành Phát
*   **Vị trí:** UI/UX Designer & Frontend Developer.
*   **Nhiệm vụ:**
    *   Nghiên cứu và thiết kế kiến trúc hệ thống giao diện người dùng (UI).
    *   Trực tiếp lập trình và hoàn thiện các màn hình hiển thị trực quan bằng thư viện Streamlit (`views/`).

### 📝 4. Đặng Tuấn Đạt
*   **Vị trí:** Technical Writer & Quality Assurance.
*   **Nhiệm vụ:**
    *   Khảo sát luồng vận hành của ứng dụng, phát hiện lỗi giao diện và đường dẫn.
    *   Xây dựng hệ thống tài liệu kỹ thuật, tài liệu hướng dẫn sử dụng và triển khai dự án (`README.md`).

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
│   ├── tables.py         # Giao diện sơ đồ bàn ăn
│   ├── menu.py           # Giao diện quản lý thực đơn
│   ├── orders.py         # Giao diện gọi món tại bàn
│   └── checkout.py       # Giao diện hóa đơn và thanh toán
└── app.py                # Điểm khởi chạy (Entrypoint) chính của dự án
```

---

## 🚀 Hướng Dẫn Cài Đặt (Installation)

Hãy làm theo các bước sau để thiết lập môi trường và chạy thử nghiệm dự án trên máy tính của bạn:

### Bước 1: Tải mã nguồn về máy
Đảm bảo bạn đã giải nén và sở hữu cấu trúc thư mục hoàn chỉnh bao gồm các thư mục (`controllers/`, `models/`, `views/`) cùng file khởi chạy `app.py`.
*   *File zip bản dựng:* (Bổ sung khi xong dự án)

### Bước 2: Cài đặt thư viện Streamlit
Mở terminal (hoặc Command Prompt / Git Bash) tại thư mục dự án và chạy lệnh cài đặt thư viện giao diện:
```bash
pip install streamlit
```

### Bước 3: Khởi động ứng dụng
Giữ terminal đứng tại thư mục gốc của dự án (nơi có file `app.py`) và kích hoạt ứng dụng bằng lệnh:
```bash
streamlit run app.py
```
> 💡 *Sau khi lệnh chạy thành công, một trang web cục bộ sẽ tự động hiển thị trên trình duyệt của bạn tại địa chỉ: `http://localhost:8501`.*

---

## 📖 Hướng Dẫn Sử Dụng Trực Quan (User Guide)

Giao diện ứng dụng được chia thành **4 Tab chức năng** chính, mô phỏng chính xác luồng hoạt động thực tế của một nhà hàng chuyên nghiệp:

### 1. 🪑 Quy trình 1: Sơ Đồ Bàn Ăn (`views/tables.py`)
*   **Hệ thống hiển thị màu sắc trực quan:**
    *   🟢 **Bàn trống:** Hiện tại chưa có khách ngồi.
    *   🔴 **Đang phục vụ:** Bàn đang hoạt động và có khách.
*   **Thao tác thực hiện:** Nhân viên click vào nút **"Mở Bàn X"** để kích hoạt bàn ăn từ Trống sang Đang phục vụ. Trạng thái bàn trên giao diện lập tức đổi từ màu xanh 🟢 sang màu đỏ 🔴.

### 2. 📝 Quy trình 2: Gọi Món & Quản Lý Đơn Hàng (`views/orders.py`)
*   **Chọn bàn thao tác:** Lọc và chọn đúng số bàn đang phục vụ (màu đỏ) từ danh sách lựa chọn.
*   **Thêm món ăn:** Chọn món ăn yêu cầu từ thực đơn và nhấn nút **"➕ Thêm vào đơn hàng"**. Danh sách món đã gọi kèm số tiền tạm tính sẽ ngay lập tức hiển thị và tự động cập nhật ở cột bên phải.
*   **Tính năng sửa sai (Undo):** Trường hợp nhân viên bấm nhầm món, có thể nhấn nút **"⏪ Undo (Xóa món vừa thêm gần nhất)"** để bốc món ăn ra khỏi hóa đơn và hoàn lại tiền tự động.

### 3. 💳 Quy trình 3: Thanh Toán & In Hóa Đơn (`views/checkout.py`)
*   **Kiểm tra hóa đơn:** Khi khách gọi tính tiền, nhân viên chuyển qua tab Thanh toán và chọn số bàn. Máy tính sẽ thực hiện các bước kiểm tra an toàn logic (`checkout_logic.py`), nạp danh sách món và kết xuất bảng chi tiết kèm **Tổng tiền cần thanh toán**.
*   **Hoàn tất chu trình:** Tích chọn xác nhận đã nhận đủ tiền từ khách và nhấn nút **"Xác Nhận Thanh Toán & Dọn Bàn"**. Hiệu ứng pháo hoa 🎈 sẽ hiển thị chúc mừng, hóa đơn cũ được giải phóng hoàn toàn khỏi bộ nhớ RAM, và bàn ăn quay trở lại trạng thái Trống 🟢 để sẵn sàng đón lượt khách mới.

### 📜 Quy trình phụ trợ: Quản Lý Thực Đơn (`views/menu.py`)
*   Hỗ trợ quản lý nhà hàng theo dõi toàn bộ danh mục món ăn đang kinh doanh, hoặc chủ động thực hiện **Thêm món mới** (Cung cấp Mã món, Tên món, Giá tiền mới) và **Xóa món** lỗi thời ra khỏi thực đơn nhà hàng một cách linh hoạt.

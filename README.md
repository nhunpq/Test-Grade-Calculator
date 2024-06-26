# Chương trình tính toán và phân tích điểm thi
Mục đích của ứng dụng này để chấm điểm tự động cho các bài thi, giúp giảm thiểu thời gian chấm điểm thi.

### 1. Các tính năng của chương trình:

- Mở các tệp tin văn bản bên ngoài và in thông báo xác nhận sự tồn tại của tệp
- Quét từng dòng của câu trả lời bài thi để tìm dữ liệu hợp lệ và cung cấp báo cáo tương ứng
- Chấm điểm từng bài thi dựa trên tiêu chí đánh giá (rubric) được cung cấp và báo cáo
- Tạo tập tin kết quả

 ### 2. Tiêu chí tính toán điểm thi:
- Chương trình chỉ tính điểm với những câu trả lời có định dạng hợp lệ tương tự như sau: N12345678,B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D
  + Chứa danh sách 26 giá trị được phân tách bằng dấu phẩy.
  + N# cho một học sinh là mục đầu tiên trên dòng. Nó phải chứa ký tự “N” theo sau là 8 ký tự số
    
- Chương trình sử dụng answer_key để tính điểm cho mỗi dòng dữ liệu hợp lệ. Điểm được tính như sau:
  + 4 điểm cho mỗi câu trả lời đúng
  + 0 điểm cho mỗi câu trả lời bị bỏ qua
  + -1 điểm cho mỗi câu trả lời sai
 
 - Answer_key của chương trình hiện tại là "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D".
   Bạn cũng có thể chỉnh sửa nó để phù hợp với thực tế của mình tại phần cuối của mã code như hình bên dưới
   ![Screenshot 2024-06-03 204236](https://github.com/nhunpq/Test-Grade-Calculator/assets/168920556/c3e16bd7-eecb-4ead-9aa7-f292fa72de2e)
  
### 3. Hướng dẫn sử dụng chương trình:
#### - Yêu cầu:

- Jupyter Notebook
- Phiên bản Python 3

#### - Bước 1: Chuẩn bị dữ liệu

- Chuẩn bị tệp tin dữ liệu câu trả lời của sinh viên
- Tất cả các tệp tin đều cần ở định dạng .txt chuẩn để có thể sử dụng chính xác.

#### - Bước 2: Chạy chương trình và xem kết quả
1. Tải mã nguồn từ GitHub Repository. Đảm bảo tệp mã nguồn của bạn nằm trong cùng thư mục với tệp dữ liệu câu trả lời của sinh viên
2. Mở Jupyter Notebook để chạy mã
3. Chỉnh sửa answer_key nếu cần thiết
4. Chạy chương trình và xem kết quả:
- Sau khi chạy xong, chương trình sẽ in báo cáo phân tích trên màn hình. Đây là một mẫu chạy chương trình cho tệp dữ liệu đầu tiên
 ![HINH](https://github.com/nhunpq/Test-Grade-Calculator/assets/168920556/730738b2-0071-4576-903f-fc76fd3dc8f5)

- Ngoài ra bạn sẽ có tệp tin kết quả chứa điểm thi của các học sinh của từng lớp học trong cùng thư mục với tập dữ liệu câu trả lời
  ![Screenshot 2024-06-03 203639](https://github.com/nhunpq/Test-Grade-Calculator/assets/168920556/2d4e7ca8-7b41-4bd5-bb2d-cfe66991dd2e)

- Luôn đảm bảo rằng bạn đã thực hiện đúng các bước trên để chạy chương trình và kiểm tra kết quả chấm điểm của các sinh viên.



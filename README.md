# Dự án tính toán và phân tích điểm thi
Dự án này nhằm mục đích xây dựng một ứng dụng chấm điểm tự động cho các bài thi.

### 1. Ứng dụng có các tác vụ như sau:

- Mở các tập tin văn bản bên ngoài được yêu cầu với exception-handling
- Quét từng dòng của câu trả lời bài thi để tìm dữ liệu hợp lệ và cung cấp báo cáo tương ứng
- Chấm điểm từng bài thi dựa trên tiêu chí đánh giá (rubric) được cung cấp và báo cáo
- Tạo tập tin kết quả được đặt tên thích hợp

 ### 2. Tiêu chí chấm điểm
- Chương trình chỉ tính điểm với những câu trả lời có định dạng hợp lệ tương tự như sau: N12345678,B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D
  + Chứa danh sách 26 giá trị được phân tách bằng dấu phẩy.
  + N# cho một học sinh là mục đầu tiên trên dòng. Nó phải chứa ký tự “N” theo sau là 8 ký tự số
    
- Chương trình sử dụng answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D" này để tính điểm cho mỗi dòng dữ liệu hợp lệ. Điểm có thể được tính như sau:
  + 4 điểm cho mỗi câu trả lời đúng
  + 0 điểm cho mỗi câu trả lời bị bỏ qua
  + -1 điểm cho mỗi câu trả lời sai
  
### 3. Hướng dẫn sử dụng:
#### - Yêu cầu:

- Phiên bản Python 3.9

#### - Bước 1: Chuẩn bị dữ liệu

- Đảm bảo bạn đã chuẩn bị tập tin dữ liệu câu trả lời của học sinh.
- Tất cả các tập tin đều cần ở định dạng .txt chuẩn để có thể sử dụng chính xác.

#### - Bước 2: Chạy chương trình và xem kết quả
- Sau khi chạy xong chương trình sẽ in báo cáo phân tích trên màn hình. Đây là một mẫu chạy chương trình cho tệp dữ liệu đầu tiên
 ![HINH](https://github.com/nhunpq/Test-Grade-Calculator/assets/168920556/730738b2-0071-4576-903f-fc76fd3dc8f5)

- Ngoài ra bạn sẽ có tập tin kết quả chứa điểm thi của các học sinh của từng lớp học trong cùng thư mục với tập dữ liệu câu trả lời.



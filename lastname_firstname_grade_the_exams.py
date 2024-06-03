#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np

def grade_the_exams(answer_key):
    
    # Nhập tên của tệp, truy cập đọc và in thông báo xác nhận sự tồn tại của tệp
    try:
        file_name = input("Enter a class file to grade (i.e. class1 for class1.txt): ") + ".txt"
        data = np.loadtxt(file_name, dtype=str)
        print("Successfully opened", file_name)
        print("\n**** ANALYZING ****")
    except FileNotFoundError:
        print("File cannot be found")
        return
    
    total_lines = 0 # Biến lưu trữ tổng số dòng trong tệp
    invalid_lines = 0 # Biến lưu trữ tổng số dòng không hợp lệ trong tệp
    scores = []  # Danh sách để lưu trữ điểm số
    list_of_skipped_questions = [] # Biến để lưu trữ danh sách mảng boolean cho các câu hỏi bị bỏ qua
    list_of_wronged_questions = [] # Biến để lưu trữ danh sách mảng boolean cho các câu hỏi có câu trả lời sai
    output_content =""# Biến lưu trữ chi tiết thông tin điểm số của sinh viên (Mã SV, điểm số)
    
    # Mở và đọc file phân tích dữ liệu, chấm điểm và báo cáo thống kê
    with open(file_name, 'r') as file:
        # Mở tệp và duyệt qua từng dòng để đếm tổng số dòng
        for line in file:
            total_lines += 1
            # Loại bỏ khoảng trắng ở đầu và cuối của dòng
            line = line.strip() 
    
            # Chia dòng văn bản thành các phần bằng cách phân tách chúng bằng dấy phẩy ','
            data_parts = line.split(',')
            
            # Kiểm tra xem dữ liệu đã tách ra có chứa đúng 26 giá trị hay không và in kết quả
            if len(data_parts) != 26:
                print(f"Invalid line of data: does not contain exactly 26 values:\n {line} \n")
                invalid_lines += 1
                continue
                
            # Kiểm tra ID của sinh viên, phải bắt đầu bằng 'N', theo sau là 8 chữ số và tổng cộng là 9 ký tự và in kết quả
            student_ID = data_parts[0]
            if not student_ID.startswith("N") or not student_ID[1:].isdigit() or len(student_ID) != 9:
                print(f"Invalid line of data: N# is invalid:\n {line} \n")
                invalid_lines += 1
                continue
                
            # Tính điểm và lưu trữ điểm của sinh viên dựa trên câu trả lời của sinh viên so với đáp án được cung cấp
            # +4 điểm cho mỗi câu trả lời đúng, 0 điểm cho mỗi câu trả lời bị bỏ qua,-1 điểm cho mỗi câu trả lời sai
            student_answers = np.array(data_parts[1:])
            score = (
                np.sum(student_answers == list(answer_key.split(','))) * 4 +
                np.sum(student_answers == '') * 0 -
                np.sum(student_answers != list(answer_key.split(','))) * 1
            )
            scores.append(score)
            
            # Xử lý và ghi thông tin về điểm số của sinh viên vào một tệp kết quả
            output_result = file_name.replace(".txt", "_grades.txt")
            output_content+= f"{student_ID}, {score}\n"
            with open(output_result,"w") as file:
                file.write(output_content)
                
            # Tạo mảng boolean cho việc kiểm tra câu hỏi có bị bỏ qua hay không dựa trên câu trả lời của sinh viên
            is_skipped_question_array = np.array(student_answers == '')
            
            # Thêm mảng boolean của câu hỏi bị bỏ qua vào danh sách
            list_of_skipped_questions.append(is_skipped_question_array)
            
            # Sử dụng defaultdict để lưu thông tin về câu hỏi bị bỏ qua
            from collections import defaultdict 
            skipped_questions_counters = defaultdict(int)
            
            # Đếm số lượng sinh viên bỏ qua từng câu hỏi
            for array in list_of_skipped_questions:
                for index, value in enumerate(array):
                    if value:
                        skipped_questions_counters[index + 1] += 1
                        
            # Tìm ra câu hỏi có số lần bị bỏ qua lớn nhất
            max_skipped_count = max(skipped_questions_counters.values())
            max_skipped_questions = [(skip_question, count_skip_question)
                for skip_question, count_skip_question in skipped_questions_counters.items()
                    if count_skip_question == max_skipped_count]
            
            # Tính tỉ lệ bị bỏ qua
            total_skip_students = len(list_of_skipped_questions)
            for skip_question, count_skip_question in max_skipped_questions:
                skip_ratio = count_skip_question / total_skip_students
                
            # Tạo mảng boolean cho việc kiểm tra câu hỏi có trả lời sai hay không dựa trên câu trả lời của sinh viên
            is_wronged_question_array = np.array(student_answers != list(answer_key.split(',')))
            
            # Thêm mảng boolean của câu hỏi trả lời sai vào danh sách
            list_of_wronged_questions.append(is_wronged_question_array)
            
            # Sử dụng defaultdict để lưu thông tin về câu hỏi trả lời sai
            from collections import defaultdict 
            wronged_question_counters = defaultdict(int)
            
            # Đếm số lượng sinh viên trả lời sai từng câu hỏi
            for array in list_of_wronged_questions:
                for index, value in enumerate(array):
                    if value:
                        wronged_question_counters[index + 1] += 1
                        
            # Tìm câu hỏi có số lượng sinh viên trả lời sai nhiều nhất
            max_wronged_count = max(wronged_question_counters.values())
            max_wronged_questions = [(wrong_question, count_wrong_question)
                for wrong_question, count_wrong_question in wronged_question_counters.items()
                    if count_wrong_question == max_wronged_count]
            
            # Tính tỉ lệ trả lời sai
            total_wrong_students = len(list_of_wronged_questions)
            for wrong_question, count_wrong_question in max_wronged_questions:
                wrong_ratio = count_wrong_question / total_wrong_students
            
    # Đếm số lượng điểm cao (lớn hơn 80)
    high_scores_count = np.sum(np.array(scores) > 80)
    # Tính điểm trung bình
    average_score = np.mean(scores)
    # Tìm điểm cao nhất
    max_score = np.max(scores)
    # Tìm điểm thấp nhất
    min_score = np.min(scores)
    # Tính điểm trung vị
    median_score = np.median(scores)
    
    if invalid_lines == 0:
        print("\n No errors found!") # Hiển thị thông báo nếu không có lỗi nào được phát hiện
    print("\n**** REPORT ****")
    print(f"Total valid lines of data: {total_lines - invalid_lines}") # Hiển thị tổng số dòng dữ liệu hợp lệ
    print(f"Total invalid lines of data: {invalid_lines}") # Hiển thị tổng số dòng dữ liệu không hợp lệ
    print(f"Total student of high score: {high_scores_count}") # Hiển thị tổng số lượng sinh viên có điểm cao
    print(f"Mean (average) score: {average_score:.2f}") # Hiển thị điểm trung bình
    print(f"Highest score: {max_score}") # Hiển thị điểm cao nhất
    print(f"Lowest score: {min_score}") # Hiển thị điểm thấp nhất
    print(f"Range of scores: {max_score - min_score}") # Hiển thị phạm vi điểm số cao nhất và thấp nhất
    print(f"Median score: {median_score}") # Hiển thị điểm trung vị
    print("Question that most people skip:", end=" ")
    # Hiển thị câu hỏi bị sinh viên bỏ qua nhiều nhất theo thứ tự
    for idx, data in enumerate(sorted(max_skipped_questions, key=lambda x: x[0])):
        skip_question = data[0]
        count_skip_question = data[1]
        if idx == len(max_skipped_questions) - 1:
            print(f"{skip_question} - {count_skip_question} - {skip_ratio:.2f}", end=" ")
        else:
            print(f"{skip_question} - {count_skip_question} - {skip_ratio:.2f},", end=" ")
            
    # Hiển thị câu hỏi bị sinh viên trả lời sai nhiều nhất theo thứ tự     
    print("\nQuestion that most people answer incorrectly: ",end = "")
    for idx, data in enumerate(sorted(max_wronged_questions, key=lambda x: x[0])):
        wrong_question = data[0]
        count_wrong_question = data[1]
        if idx == len(max_wronged_questions) - 1:
            print(f"{wrong_question} - {count_wrong_question} - {wrong_ratio:.2f}",end=" ")
        else:
            print(f"{wrong_question} - {count_wrong_question} - {wrong_ratio:.2f},",end=" ")
        
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D" #Điều chỉnh đáp án phù hợp

# Gọi hàm analyze_data để phân tích dữ liệu và chấm điểm
grade_the_exams(answer_key)


# In[ ]:





1. Giới thiệu:

Phân loại văn bản là một nhiệm vụ quan trọng trong xử lý ngôn ngữ tự nhiên, nhằm phân loại các tài liệu văn bản vào các lớp hoặc danh mục được xác định trước. Trong bài tập này, em triển khai và so sánh kết quả của ba thuật toán phân loại cho nhiệm vụ phân loại văn bản: Naive Bayes, Multinomial Naive Bayes và SVM. Em sử dụng Python và thư viện scikit-learn, cùng với pandas để xử lý dữ liệu và matplotlib để trực quan hóa.

2. Bộ dữ liệu

Em triển khai và đánh giá kết quả trên bộ dữ liệu được cung cấp trong bài tập. Đây là bộ dữ liệu ghi lại 30k đánh giá bằng tiếng Việt từ các sàn thương mại điện tự. Dữ liệu là một tệp csv gồm 3 cột bao gồm: comment, label và rate. Trong đó, comment thể hiện các đánh giá, label có 3 nhãn neu, pos, neg và rate thể hiện cho thang điểm đánh giá từ 1 đến 5.

3. Phương pháp

3.1. Naive Bayes

Chuẩn bị dữ liệu:

- Tạo một đối tượng bằng CountVectorizer
- Biểu diễn văn bản trong cột 'comment' của thành dạng ma trận Bag-of-Words

Chia dữ liệu thành tập huấn luyện và tập kiểm tra:
- Chia dữ liệu thành tập huấn luyện và tập kiểm tra với tỷ lệ 70-30

Huấn luyện mô hình Naive Bayes

Dự đoán và tính độ chính xác:
- Dự đoán nhãn trên tập kiểm tra
- In ra số điểm được dự đoán sai trên tổng số điểm kiểm tra

Test với dữ liệu mới:
- Tạo một DataFrame chứa các dòng văn bản mới để kiểm tra.
- Biểu diễn các văn bản mới thành dạng ma trận Bag-of-Words.
- Dự đoán nhãn cho dữ liệu kiểm tra mới và in ra kết quả.

3.2. Multinomial Naive Bayes

Đối với Multinomial Naive Bayes, em làm tương tự như đã thực hiện với Naive Bayes và đổi thuật toán từ Naive Bayes thành Multinomial Naive Bayes.

3.3. SVM

Khác với 2 phương pháp vừa nêu trên, với thuật toán SVM, dữ liệu còn được chuyển đổi nhãn sang dạng số:
- Lấy danh sách các nhãn duy nhất từ tập huấn luyện
- Xây dựng ánh xạ giữa nhãn và số
- Chuyển các nhãn trong tập huấn luyện và tập kiểm tra thành dạng số

Xây dựng pipeline với Support Vector Machine (SVM):
- Xác định n-gram, ở đây đang dùng unigram và bigram.
- Tạo một pipeline gồm các bước: chuyển đổi dữ liệu văn bản thành vector đếm từ (CountVectorizer), biểu diễn vector thành vector TF-IDF (TfidfTransformer), và sử dụng mô hình máy vector hỗ trợ (LinearSVC)

Huấn luyện mô hình và dự đoán:
- Huấn luyện mô hình trên tập huấn luyện với nhãn đã được chuyển thành dạng số
- Tạo danh sách các văn bản mới cần dự đoán
- Dự đoán nhãn cho các văn bản mới vừa tạo

In kết quả dự đoán

4. Kết quả
- Mô hình Naive Bayes đạt accuracy: 20.73%
- Mô hình Multinomial Naive Bayes đạt accuracy: 72.76%
- Mô hình SVM đạt accuracy: 77.59%


Đối với 3 câu dữ liệu mới được thêm vào để kiểm tra:
- Mô hình Naive Bayes đưa ra kết quả không mong đợi trên cả ba mẫu thử
- Mô hình Multinomial Naive Bayes đưa ra kết quả mong đợi trên cả ba mẫu thử
- Mô hình SVM đưa ra kết quả mong đợi trên hai mẫu thử, và còn nhầm lẫn ở giữa hai loại nhãn neu và pos 

Note: For permission issue when using requirement.txt to install package, if you can not run the command as Administrator, please use `pip install -r requirements.txt --user`
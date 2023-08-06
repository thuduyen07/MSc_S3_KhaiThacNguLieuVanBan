# Khai thác ngữ liệu văn bản

## 20/07/2023
### Giới thiệu - Tổng quan
Phân loại dữ liệu:
- Có cấu trúc (structured data): thông tin đã chọn lọc và lưu dưới dạng cấu trúc
    - có thể thể hiện dạng rational database
    - sẵn sàng để khai thác
    - có thể dùng các thuật toán data mining
- Không có cấu trúc (unstructured data): thông tin trình bày dạng tự nhiên, không theo chuẩn mực, định dạng không nhất quán
    - không thể thể hiện dạng rational database
    - chưa sẵn sàng để khai thác
    - ví dụ: các comment trên một trang web, các dữ liệu đa phương tiện (image, video, audio, file, emails,spreadsheets..)

Dữ liệu văn bản:
- hình thức trao đổi phổ biến nhất
- đặc điểm: không có cấu trúc trình bày cụ thể
- làm thế nào để khai thác thông tin hữu ích trong lượng dữ liệu khổng lồ này? $\rightarrow$ khai thác văn bản = text-mining/text-analytics

Khai thác văn bản:
- quá trình phát hiện tri thức ẩn trong văn bản
- không phải là khai thác dữ liệu (phát hiện tri thức có cấu trúc)
- đây là bước trước bước khai thác dữ liệu

Ứng dụng của khai thác văn bản
- sentiment analysis / opinion mining
- early warning outbreak / outbreak detection (phát hiện sớm dịch bệnh)
- social listening
    - đo lường sức khoẻ thương hiệu
    - xử lý khủng hoảng truyền thông
    - thăm dò đối thủ cạnh tranh
- fake news detection
- fraud detection
- chatbot & 

Kiến trúc chung của một hệ thống khai thác văn bản:
![](./images/z4533237813795_888c0207993c305b6dd3017feb0305bb.jpg)

Phân loại các bài toán của hệ thống khai thác văn bản
- phân lớp văn bản (text category/document classification)
    - phân loại một văn bản vào một hay một vài loại cho 
- information extraction
    - xác định/rút trích các thành phần quan tâm trong văn bản
    - chuyển từ dạng không có cấu trúc sang dạng có cấu trúc
    - các bài toán đặc trưng (cấp độ):
        - named entity extraction: tên người, địa điểm, tên tổ chức, tên sản phẩm, tên thương hiệu...
        - relation extraction (các sự kiện, tìm các thực thể và quan hệ giữa chúng)
    - ứng dụng: trending analysis, social listening...
- document clustering
    - tự động chia tập hợp các văn bản thành các nhóm
- information retrieval
    - chọn lọc thông tin liên quan trước khi thực hiện các kỹ thuật mining
    - phương pháp cơ bản: so sánh sự tương đồng giữa nội dung tài liệu và câu truy vấn
    - cần 2 mô hình:
        - lưu trữ tài liệu
        - tính độ tương đồng
    - ứng dụng: search engines
- ...
- hoặc là sự kết hợp của một số bài toán này

Các cách tiếp cận cho bài toán khai thác văn bản:
- phương pháp sử dụng luật/heuristics (rule-based methods)
    - dùng if-else, regex, heuristics
    - rút trích tên riêng (tên đi sau chữ "ông/bà")
    - ưu: đơn giản
    - khuyết:
        - tốn công/khó xây dựng bộ luật
- phương pháp học máy: hệ thống tự động học cách giải quyết bài toán
    - học máy có giám sát
    - học máy không giám sát
- phương pháp "prompt engineering: sử dụng mô hình ngôn ngữ lớn (LLM)

Học máy có giám sát, gồm 2 giai đoạn
- huấn luyện mô hình
- sử dụng mô hình để dự đoán dữ liệu mới

Các bước giải quyết bài toán khai thác văn bản:
- chia nhỏ bài toán
- giải quyết các bài toán nhỏ
- có thể kết hơp các phương pháp để giải quyết các bài toán nhỏ
- tổng hợp để có được giải pháp cho bài toán 

Các bước cho các bài toán nhỏ:
- xác định nguồn dữ liệu
- tiền xử lí dữ liệu
- gắn nhãn dữ liệu
- xây dựng mô hình
- kiểm thử / đánh giá
- tinh chỉnh mô hình
- triển khai

### Mục tiêu môn học
![](./images/z4533357476555_1340ba2bb52fdc7e6c60797ed1b821f8.jpg)

![](./images/z4533357523464_fac0afa7638bd8fc7ed0f268a846b3d0.jpg)

![](./images/z4533359452671_e6cd1b41bbfddcae506d8aee1933e4a6.jpg)

![](./images/z4533359454006_2766b7a0e1c037d72ad147b799d05d7c.jpg)

https://2023.aclweb.org/program/best_papers/

https://underline.io/events/284/sessions?eventSessionId=10659

https://2021.emnlp.org/papers

https://aclanthology.org/events/emnlp-2022

![](./images/z4533372105808_2a47af111b19fab0cbaa0e4250386a35.jpg)

![](./images/z4533372110281_3a5c7db83d2df33b65db1c33c32d00b1.jpg)

![](./images/z4533372114484_d18c393bfedb2d5d70ad176ebfa8d5ba.jpg)

![Alt text](./images/image.png)

![Alt text](./images/DanhGiaMonHoc.png)

![Alt text](image.png)

## 030823
## Rút trích thông tin văn bản (Information extraction)

Các bài toán đặc trưng
- nhận diện thực thể định danh: NER
- 
    - event extraction

Mục tiêu
- annotate (gắn nhãn tài liệu)
- tại sao lại cần chuyển từ html sang xml?

Công nghệ 
- lexicon lookups: tìm kiếm một thuật ngữ có trong từ điển hay không

Quy trình xây dựng kho dữ liệu tri thức

cần lưu dữ liệu về knowledge DB và dùng từ đây để chạy các thuật toán học máy -> hi vọng chạy ổn định hơn =))

Một số ứng dụng
- map skills giữa JD và CV =))

Landscape for IE Tasks:
1.
2. 
3. Complexity
- rút trích thông tin dạng closed set (trong hữu hạn )
- regular set (vô hạn có format =))), ví dụ số điện thoại (biết dc có nhiu số :'>)
- complex pattern ()
- ambiguous pattern (không có format cụ thể) => khó, ví dụ tên riêng
4. single field vs record
- 

Các mô hình sử dụng trong IE
- Lexicons: lướt qua văn bản, kiểm tra đối tượng đang xét có trong tập từ điển khum
- classify pre-segmented candidates: xác định term đang xét thuộc lớp nào 
- sliding window: y chang trên mà dùng cửa số trượt =))
- boundary models: chạy hai vòng lặp, một tìm nơi bắt đầu, một tìm nơi kết thúc 
- finite state machines
- context free grammars

regular expressions
- input: các mẫu đã được gán nhãn thủ công
- thường dùng cho số, date, email, tên người có đi kèm chức danh (Dr. Abc)

Sequence labeling: gắn nhãn từng token thuộc về một **loại đặc biệt** thể hiện cho loại đối tượng
- dùng IOB annotation trong đó I-inside, O-outside, B-begin, gán trên từng token
- giới thiệu IOB annotation/CONLL format, [CoNLL-U](https://universaldependencies.org/format.html) 
- có thể đoán ra những token ngay cả khi không có trong từ điển train do đã học được pattern

Relation extraction methods
- manually engineered rules: 
    - rules based on words/entities/parsed text: ví dụ <company> located in <location>
- weakly supervised relation extraction (semi-supervised)
    - giả sử có rule: <company> located in <location>
    - sau khi tìm dc, ta duyệt cả văn bản tìm các từ giữa company và location còn lại -> tạo rule mới và tiếp tục

[CoNLL2003](https://huggingface.co/datasets/conll2003)

Lab03: làm NER cho tiếng việtt


# Theory Final Project:
- Paper: What the DAAM: Interpreting Stable Diffusion Using Cross Attention
- Link paper: https://arxiv.org/pdf/2210.04885.pdf
- Github: https://github.com/castorini/daam

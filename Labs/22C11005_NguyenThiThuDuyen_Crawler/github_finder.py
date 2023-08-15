import sys
import requests
from bs4 import BeautifulSoup

# Tìm các link GitHub chứa tên bài báo
def find_github_links(article_name):
    # Tạo URL tìm kiếm trên Google
    search_url = f"https://www.google.com/search?q={article_name}+github"

    # Lấy nội dung của trang tìm kiếm
    response = requests.get(search_url)

    # Sử dụng BeautifulSoup để phân tích cú pháp HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Tìm các thẻ a chứa "github.com"
    github_links = []
    for link in soup.find_all("a", href=True):
        if "github.com" in link["href"]:
            github_links.append("https://www.google.com" + link["href"]) # Thêm URL của Google vào trước link GitHub

    return github_links

# Kiểm tra các link GitHub có hoạt động hay không
def check_active_links(links):
    active_links = []
    for link in links:
        try:
            response = requests.head(link)
            # Kiểm tra mã trạng thái HTTP, mã 400 trở lên là lỗi
            if response.status_code < 400:  
                active_links.append(link)
        except requests.ConnectionError:
            pass  # Bỏ qua nếu không thể kết nối đến đường dẫn

    return active_links

# Ghi dữ liệu vào tệp Markdown
def write_list_to_md_file(filename, data_list):
    try:
        with open(filename, "w", encoding="utf-8") as md_file:
            for item in data_list:
                md_file.write(f"- {item}\n")
        print(f"Dữ liệu đã được ghi vào tệp {filename} thành công!")
    except Exception as e:
        print(f"Lỗi: {e}")

def main():
    # Kiểm tra tham số đầu vào
    if len(sys.argv) < 2:
        print("Hãy cung cấp tên bài báo cần tìm trên GitHub.")
        return

    # Tìm link GitHub
    article_name = " ".join(sys.argv[1:])
    github_links = find_github_links(article_name)
    active_github_links = check_active_links(github_links)

    # In kết quả
    if active_github_links:
        print("Link GitHub của bài báo:")
        for link in active_github_links:
            print(link)
    else:
        print("Không tìm thấy link GitHub cho bài báo này.")

    # Ghi kết quả vào tệp Markdown
    write_list_to_md_file(article_name + ".md", active_github_links)


# Chạy chương trình
if __name__ == "__main__":
    main()

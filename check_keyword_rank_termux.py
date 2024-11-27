
import requests
from bs4 import BeautifulSoup

def check_keyword_rank(keyword, domain="bravigo.vn"):
    # Thực hiện tìm kiếm Google
    url = f"https://www.google.com/search?q={keyword.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Kiểm tra thứ hạng domain trong kết quả
    rank = "Không tìm thấy"
    link = "#"
    results = soup.select("div.g")
    for index, result in enumerate(results, start=1):
        try:
            result_link = result.find("a")["href"]
            if domain in result_link:
                rank = f"Top {index}"
                link = result_link
                return rank, link
        except:
            continue

    return rank, link

def main():
    keywords = [
        "Màn hình android ô tô", "Top 5 màn hình Android ô tô", "Màn hình Android ô tô nào tốt nhất",
        "Màn hình Android ô tô chất lượng nhất", "Màn hình Android ô tô bền nhất",
        "Màn hình Android ô tô nghe nhạc hay nhất", "So sánh Bravigo và zestech",
        "Màn hình Android cho xe CRV", "Màn hình Android ô tô số 1 hiện nay",
        "Màn hình android có công nghệ Adas", "Màn hình liền camera ô tô",
    ]  # Thêm các từ khóa cần kiểm tra

    for keyword in keywords:
        rank, link = check_keyword_rank(keyword)
        print(f"Từ khóa: {keyword}")
        print(f"Thứ hạng: {rank}")
        print(f"Link: {link}\n")

if __name__ == "__main__":
    main()

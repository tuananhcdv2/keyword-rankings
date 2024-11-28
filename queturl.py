import requests
from bs4 import BeautifulSoup
import re
import os
from tqdm import tqdm

# Hàm quét số điện thoại
def extract_phone_numbers(text):
    phone_pattern = r'\b(?:\d{10}|\d{11})\b'  # Số điện thoại 10-11 chữ số
    return re.findall(phone_pattern, text)

# Hàm quét hình ảnh
def extract_images(soup):
    img_tags = soup.find_all('img')
    img_links = [img['src'] for img in img_tags if 'src' in img.attrs]
    return img_links

# Hàm quét PDF
def extract_pdfs(soup):
    pdf_pattern = r'href=["\'](.*?\.pdf)["\']'
    return re.findall(pdf_pattern, str(soup))

# Hàm quét tài liệu (DOC, DOCX, XLS, XLSX)
def extract_documents(soup):
    doc_pattern = r'href=["\'](.*?\.(?:docx?|xlsx?))["\']'
    return re.findall(doc_pattern, str(soup))

# Hàm quét MP3
def extract_mp3(soup):
    mp3_pattern = r'href=["\'](.*?\.mp3)["\']'
    return re.findall(mp3_pattern, str(soup))

# Hàm quét Video
def extract_videos(soup):
    video_pattern = r'href=["\'](.*?\.(?:mp4|avi|mov|mkv))["\']'
    return re.findall(video_pattern, str(soup))

# Hàm quét thông tin từ trang web
def scrape_website(url, choice):
    try:
        # Lấy nội dung của trang web
        response = requests.get(url)
        response.raise_for_status()  # Kiểm tra lỗi HTTP

        soup = BeautifulSoup(response.text, 'html.parser')

        if choice == '1':  # Quét số điện thoại
            data = extract_phone_numbers(response.text)
        elif choice == '2':  # Quét hình ảnh
            data = extract_images(soup)
        elif choice == '3':  # Quét PDF
            data = extract_pdfs(soup)
        elif choice == '4':  # Quét tài liệu
            data = extract_documents(soup)
        elif choice == '5':  # Quét MP3
            data = extract_mp3(soup)
        elif choice == '6':  # Quét video
            data = extract_videos(soup)
        else:
            raise ValueError("Lựa chọn không hợp lệ")

        return data

    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi truy cập trang web: {e}")
        return []
    except Exception as e:
        print(f"Lỗi xảy ra: {e}")
        return []

# Hàm hiển thị tiến trình và lưu kết quả
def show_progress_and_save(data):
    # Hiển thị tiến trình quét
    for i in tqdm(range(len(data)), desc="Đang quét dữ liệu..."):
        pass

    # Lưu kết quả vào file txt
    with open('result.txt', 'w') as file:
        for item in data:
            file.write(f"{item}\n")

    print("\nQuá trình quét hoàn tất. Kết quả đã được lưu vào 'result.txt'.")

def main():
    # Giao diện lựa chọn loại thông tin cần quét
    print("Chọn loại thông tin cần quét:")
    print("1. Số điện thoại")
    print("2. Hình ảnh")
    print("3. PDF")
    print("4. Tài liệu (DOC, DOCX, XLS, XLSX)")
    print("5. MP3")
    print("6. Video")

    choice = input("Nhập lựa chọn (1-6): ")

    # Nhập URL của trang web cần quét
    url = input("Nhập URL của trang web: ")

    # Quét dữ liệu từ trang web
    print("Đang quét trang web... Vui lòng đợi.")
    data = scrape_website(url, choice)

    if data:
        print(f"\nKết quả quét được ({len(data)} item):")
        for item in data:
            print(item)

        # Lưu kết quả vào file
        show_progress_and_save(data)
    else:
        print("Không tìm thấy dữ liệu hoặc xảy ra lỗi trong quá trình quét.")

if __name__ == "__main__":
    main()

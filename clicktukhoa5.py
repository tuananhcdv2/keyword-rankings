from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from termcolor import colored

def setup_driver():
    # Cấu hình Chrome để mở ở chế độ ẩn danh
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--headless")  # Tùy chọn: chạy ở chế độ headless nếu không cần hiển thị trình duyệt
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def safe_click(driver, element):
    # Thử cuộn vào giữa màn hình và click
    try:
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(3)  # Chờ ngắn để đảm bảo phần tử hiển thị hoàn toàn
        element.click()
    except Exception as e:
        print(f"Lỗi khi click trực tiếp, thử click bằng JavaScript: {e}")
        # Dùng JavaScript để click
        driver.execute_script("arguments[0].click();", element)

def search_and_click(driver, keyword):
    # Mở Google và tìm kiếm từ khóa
    driver.get("https://www.google.com")
    search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)  # Đợi cho kết quả tải xong

    try:
        # Đợi và tìm kết quả đầu tiên
        first_result = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.g a'))
        )
        safe_click(driver, first_result)

        # In thông báo thành công với màu sắc
        message = colored(f"Successfully clicked on the first result for keyword: '{keyword}'", 'magenta')
        print(message)

        # Ở lại trang từ 15-20 giây
        time.sleep(random.randint(15, 20))

    except Exception as e:
        print(f"Lỗi khi tìm và click từ khóa '{keyword}': {e}")

def main():
    driver = setup_driver()
    keywords = [
        "màn hình crv", "màn hình android crv", "so sánh màn hình bravigo và oled",
        "so sánh màn hình bravigo và gotech", "mặt dưỡng màn hình android",
        "có nên thay màn hình zin xe cx5 hay không", "màn hình android ford transit",
        "màn hình android cho crv", "màn hình android ô tô Chevrolet Colorado 2021",
        "màn hình android honda city", "màn hình android cho wuling huangwang",
        "màn hình android ô tô", "top 5 màn hình Android ô tô", "màn hình Android ô tô nào tốt nhất",
        "màn hình Android ô tô chất lượng nhất", "màn hình Android ô tô bền nhất",
        "màn hình Android ô tô nghe nhạc hay nhất", "so sánh Bravigo và zestech",
        "màn hình Android cho xe CRV", "màn hình Android ô tô số 1 hiện nay",
        "màn hình android có công nghệ Adas", "màn hình liền camera ô tô", "màn hình android ô to 7 inch",
        "màn hình crv 2024", "màn hình cx5", "màn hình mazda",
        "màn hình android 7 inch toyota", "màn hình honda city 2024", "màn hình fadil", "màn hình android ô tô chính hãng", "màn hình android ô tô", "màn hình android honda city", "màn hình android cho wuling huangwang",
        "màn hình android cho xe Skoda Kodia",
        "màn hình android nghe nhạc hay nhất",
        "màn hình android cho honda city",
        "màn hình android đáng mua 2024",
        "màn hình zin xpander",
        "màn hình android ô tô 13 inch",
        "màn hình cho xe hyundai creta",
        "màn hình crv",
        "màn hình android crv",
        "so sánh màn hình bravigo và oled",
        "so sánh màn hình bravigo và gotech",
        "màn hình android ford transit",
        "màn hình android cho crv", 
	"màn hình zin xpander",
        "màn hình android ô tô 13 inch",
        "màn hình cho xe hyundai creta",
        "màn hình android cho xe fortuner",
        "màn hình android mercerdes",
    ]  # Danh sách từ khóa để tìm kiếm và click

    try:
        while True:
            for keyword in keywords:
                search_and_click(driver, keyword)
                time.sleep(random.randint(4, 10))  # Đợi ngẫu nhiên giữa các lần click
            # Hiện thông báo sau mỗi vòng lặp và yêu cầu đổi IP VPN
            input(colored("Vui lòng đổi IP VPN rồi nhấn Enter để tiếp tục...", 'yellow'))
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys

def main(headless=False):
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    from selenium.webdriver.chrome.service import Service
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    wait = WebDriverWait(driver, 15)

    try:
        # 1. Mở trang web
        driver.get("https://a.opnews.net/")
        print("Opened page:", driver.title)

        # 2. Cuộn xuống cuối trang
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        # 3. Tìm card "Data Analytics"
        card = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[contains(text(), 'Data Analytics') or contains(., 'Data Analytics')]")
        ))
        driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth', block:'center'});", card)
        time.sleep(1)
        card.click()
        print("Clicked Data Analytics card")
        time.sleep(3)

        # 4. Click nút Home trên top
        home_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[text()='Home' or contains(., 'Home')]")
        ))
        home_btn.click()
        print("Clicked Home button")

        # 5. Chờ rồi đóng trình duyệt
        time.sleep(2)

    finally:
        driver.quit()
        print("Browser closed")

if __name__ == "__main__":
    headless_arg = len(sys.argv) > 1 and sys.argv[1].lower() == "headless"
    main(headless=headless_arg)

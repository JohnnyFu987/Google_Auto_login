import time
import undetected_chromedriver as uc  # 防止被網站檢測的 Chrome 驅動
from selenium.webdriver.common.by import By  # 用於指定定位網頁元素
from selenium.webdriver.support.ui import WebDriverWait  # 用於等待網頁元素出現
from selenium.webdriver.support import expected_conditions as EC  # 指定等待條件

class Main:
    def __init__(self) -> None:
        self.url = 'https://accounts.google.com/ServiceLogin'
        self.driver = uc.Chrome(use_chrome=True)

    def login(self, email, password):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(email + "\n")
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, 'Passwd'))).send_keys(password + "\n")
        input("完成驗證後按 Enter 繼續...")

if __name__ == "__main__":
    email = 'your_email@gmail.com'
    password = 'your_password'

    bot = Main()
    bot.login(email, password)

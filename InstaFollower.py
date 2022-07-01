from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep
SIMILAR_ACC="acc to follow"
USERNAME="Your username"
PASSWORD="Your Password"
class Instafollower:
    def __init__(self):
        self.__driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.__wait =WebDriverWait(self.__driver,15)
    def login(self):
        self.__driver.get("https://www.instagram.com/accounts/login/?hl=bg")
        sleep(1)
        cookie = self.__driver.find_element(By.CSS_SELECTOR, ".HoLwm")
        cookie.click()
        username = self.__driver.find_element(By.NAME,'username')
        username.send_keys(USERNAME)
        password = self.__driver.find_element(By.NAME, 'password')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        input_box = self.__wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.d_djL')))
        input_box.send_keys(SIMILAR_ACC)
        account = self.__wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.qyrsm')))
        account.click()
        followers = self.__wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT,' последователи')))

        followers.click()
    def follow(self):
        sleep(3)
        pop_up_window = self.__wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '._aano')))
        while True:
            try:
                self.__driver.execute_script(
                    'arguments[0].scrollTop = arguments[0].scrollHeight;', pop_up_window)
                #self.__driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',pop_up_window)
                scr1 = self.__driver.find_element(By.CSS_SELECTOR,'div[class="_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9o"]')

                peoples = self.__driver.find_elements(By.CSS_SELECTOR,'._acas')
                for follow_btn in peoples:
                    self.__driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
                    sleep(0.3)
                    follow_btn.click()

            except ElementClickInterceptedException:
                try:
                    print("abc")
                    ok_btn = self.__driver.find_element(By.CSS_SELECTOR, '._a9-v button[class="_a9-- _a9_1"]')
                    ok_btn.click()
                    sleep(2)
                    denied = self.__driver.find_element(By.CSS_SELECTOR,'button[class="_a9-- _a9-_"]')
                    denied.click()
                    sleep(2)

                except:
                    pass

            except:
                pass




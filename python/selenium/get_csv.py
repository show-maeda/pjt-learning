from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from time import sleep
import datetime
import csv

options = Options()
#以下のコメントアウトを解除すると、ヘッドレスモードが有効になります。
# options.add_argument("--headless")

dt_now = datetime.datetime.now()

def login(driver):
    sleep(1)
    # ログイン画面
    email = driver.find_element_by_name("email")
    email.send_keys("shota.maeda@haleruto.com")

    password = driver.find_element_by_name("password")
    password.send_keys("shota.maeda1234")

    sleep(1)
    login_button = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/form/button/span[1]')
    login_button.click()


def set_search_condition(driver, dt_now):
    sleep(1)
    search_button = driver.find_element_by_xpath('//*[@id="root"]/div/main/div[2]/div/button[2]')
    search_button.click()

    sleep(1)
    # １週間前を計算
    td_1week = datetime.timedelta(weeks=1)
    dt_start = dt_now - td_1week
    # 開始日を入れる
    start_date = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div/div/div[3]/div[1]/div/div/div/div/input')
    start_date.send_keys(dt_start.strftime('%Y'))
    start_date.send_keys(dt_start.strftime('%m'))
    start_date.send_keys(dt_start.strftime('%d'))

    end_date = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div/div/div[3]/div[2]/div/div/div/div/input')
    end_date.send_keys(dt_now.strftime('%Y'))
    end_date.send_keys(dt_now.strftime('%m'))
    end_date.send_keys(dt_now.strftime('%d'))

    set_button = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div/div/div[7]/div[2]/div/div/button')
    set_button.click()


def download_csv(driver):
    sleep(1)
    download_button = driver.find_element_by_xpath('//*[@id="root"]/div/main/div[2]/div/button[1]')
    download_button.click()
    sleep(1)
    Alert(driver).accept()


if __name__ == "__main__":
    driver = webdriver.Chrome(
        executable_path="./chromedriver",
        options=options)
    driver.get("https://web.agri-board.com/login")
    login(driver)
    set_search_condition(driver, dt_now)
    download_csv(driver)
    sleep(5)
    driver.close()
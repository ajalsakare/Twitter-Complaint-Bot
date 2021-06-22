import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Program Files/chromedriver_win32/chromedriver.exe"
SPEEDTEST_URL = "https://www.speedtest.net/"
TWITTER_LOGIN_URL = "https://twitter.com/"
USERNAME = os.environ.get('TWITTER_USERNAME')
PASSWORD = os.environ.get('TWITTER_PASSWORD')

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(SPEEDTEST_URL)

go = driver.find_element_by_class_name("start-text")
go.click()
time.sleep(50)

download_speed = driver.find_element_by_class_name("download-speed")
DOWNLOAD_SPEED = download_speed.text
print(f"Download Speed: {download_speed.text}")

upload_speed = driver.find_element_by_class_name("upload-speed")
UPLOAD_SPEED = upload_speed.text
print(f"Upload Speed: {upload_speed.text}")
MSG = f"Hello @Airtel_Presence, I'm having internet speed problems from past couple of weeks. My down/up speeds are {DOWNLOAD_SPEED}/{UPLOAD_SPEED},please look into this! "

driver.quit()
driver2 = webdriver.Chrome(executable_path=chrome_driver_path)
driver2.get(TWITTER_LOGIN_URL)
time.sleep(3)

login = driver2.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div')
login.click()
time.sleep(5)

username = driver2.find_element_by_name("session[username_or_email]")
username.send_keys(USERNAME)

password = driver2.find_element_by_name("session[password]")
password.send_keys(PASSWORD)

login2 = driver2.find_elements_by_tag_name("span")
for l in login2:
    if l.text == "Log in":
        l.click()
        break
time.sleep(5)

tweet_msg = driver2.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div['
                                          '2]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                          '1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div['
                                          '2]/div/div/div/div')
tweet_msg.send_keys(MSG)
tweet = driver2.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div['
                                      '2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div['
                                      '3]/div/span/span')
tweet.click()

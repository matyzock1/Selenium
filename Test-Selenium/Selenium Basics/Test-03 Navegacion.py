from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

delay = 3

ser = Service("C:\Drivers\chromedriver.exe")

op = webdriver.ChromeOptions()
op.add_argument("--disable-notifications")

driver = webdriver.Chrome(service=ser, options=op)

driver.maximize_window()

driver.get("https://demoqa.com/text-box")
time.sleep(delay)

driver.get("https://github.com/matyzock1/tesis")
time.sleep(delay)

driver.get("https://soundcloud.com/kiddforget")
time.sleep(delay)

driver.execute_script("window.history.go(-1)")
time.sleep(delay)

driver.execute_script("window.history.go(-1)")
time.sleep(delay)

driver.execute_script("window.history.go(+2)")
time.sleep(delay)


driver.close()
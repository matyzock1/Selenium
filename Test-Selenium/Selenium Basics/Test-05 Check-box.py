from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("http://total-qa.com/checkbox-example/")
driver.maximize_window()

t = 5

#Esperamos que un elemento aparezca para realizar su accion!

btn_uno = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@type,'checkbox')])[1]")))
btn_uno.click()

btn_dos = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@type,'checkbox')])[2]")))
btn_dos.click()

btn_dos = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@type,'checkbox')])[3]")))
btn_dos.click()

time.sleep(t)


driver.close()

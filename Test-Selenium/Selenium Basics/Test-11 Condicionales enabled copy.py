from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

t = 2

ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()

#Le damos tiempo al navegador para localizar los elementos
driver.implicitly_wait(5)


titulo = driver.find_element(By.XPATH, "//button[contains(@id,'submit')]")

if titulo.is_enabled() == True:
    print("El elemento se encuentra en la página")
    time.sleep(t)
else:
    print("El elemento no se encuentra en la página")
    
time.sleep(t)
driver.close()
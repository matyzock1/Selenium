from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(1)


#Identificamos el primer valor del formulario
nombre = driver.find_element(By.XPATH, "//input[@id='userName']")

#Enviamos los valores al formulario una vez localizado el primer valor
nombre.send_keys("Matías" + Keys.TAB + 'matyzock@gmail.com'+ Keys.TAB + 'Calle 113' + Keys.TAB + 'Callecita 1134' + Keys.TAB + Keys.ENTER)

driver.execute_script("window.scrollBy(0, 500)")
time.sleep(2)

driver.execute_script("window.scrollBy(0, -500)")
time.sleep(2)
driver.find_element(By.XPATH, "(//span[contains(@class,'text')])[2]").click()
time.sleep(2)

driver.close()

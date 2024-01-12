from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(1)

nombre = driver.find_element(By.ID, "userName")
nombre.send_keys("Matías")
time.sleep(1)

email = driver.find_element(By.ID, "userEmail")
email.send_keys("matyzock@gmail.com")
time.sleep(1)

direccion = driver.find_element(By.ID, "currentAddress")
direccion.send_keys("Calle 113")
time.sleep(1)

direccion1 = driver.find_element(By.ID, "permanentAddress")
direccion1.send_keys("Callecita 1134")
time.sleep(1)

#Ejecutamos una función de javaScript para que baje la página.
driver.execute_script("window.scrollBy(0, 500)")

boton = driver.find_element(By.ID, "submit")
boton.click()
time.sleep(1)



driver.close()

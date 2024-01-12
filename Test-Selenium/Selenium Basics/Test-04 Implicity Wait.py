from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()

#Le da tiempo al navegador para localizar los objetos.
driver.implicitly_wait(10)

t = .1
time.sleep(t)

nombre = driver.find_element(By.CSS_SELECTOR, "#userName")
nombre.send_keys("Matías")
time.sleep(t)

email = driver.find_element(By.CSS_SELECTOR, "#userEmail")
email.send_keys("matyzock@gmail.com")
time.sleep(t)

direccion = driver.find_element(By.CSS_SELECTOR, "#currentAddress")
direccion.send_keys("Calle 113")
time.sleep(t)

direccion1 = driver.find_element(By.CSS_SELECTOR, "#permanentAddress")
direccion1.send_keys("Callecita 1134")
time.sleep(t)

#Ejecutamos una función de javaScript para que baje la página.
driver.execute_script("window.scrollBy(0, 500)")

boton = driver.find_element(By.CSS_SELECTOR, "#submit")
boton.click()
time.sleep(t)

driver.close()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

t = 1   

ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()

#Le damos tiempo al navegador para localizar los elementos
driver.implicitly_wait(5)

btn = driver.find_element(By.XPATH, "//button[contains(@class,'btn btn-default')]")
time.sleep(t)

ir = driver.execute_script("arguments[0].scrollIntoView();", btn)
btn.click()
time.sleep(t)


#NOMBRE
error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//small[@class='help-block'][contains(.,'Please supply your first name')]")))
error = driver.find_element(By.XPATH, "//small[@class='help-block'][contains(.,'Please supply your first name')]")
time.sleep(t)

if (error.text == "Please supply your first name"):
    ir = driver.execute_script("arguments[0].scrollIntoView();", error)
    time.sleep(t)
    campo = driver.find_element(By.XPATH, "//input[contains(@name,'first_name')]").send_keys("Matías")
    time.sleep(t)
    print("Nombre correcto")
    
else:
    print("Falta el nombre")
    

#APELLIDO
error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//small[@class='help-block'][contains(.,'Please supply your last name')]")))
error = driver.find_element(By.XPATH, "//small[@class='help-block'][contains(.,'Please supply your last name')]")
time.sleep(t)

if (error.text == "Please supply your last name"):
    ir = driver.execute_script("arguments[0].scrollIntoView();", error)
    time.sleep(t)
    campo = driver.find_element(By.XPATH, "//input[contains(@name,'last_name')]").send_keys("Aravena")
    time.sleep(t)
    print("Apellido correcto")
    
else:
    print("Falta el Apellido")
    
# if error.is_displayed() == True:
#     ir = driver.execute_script("arguments[0].scrollIntoView();", error)
#     time.sleep(t)
#     campo = driver.find_element(By.XPATH, "//input[contains(@name,'first_name')]").send_keys("Matías" + Keys.TAB + "Aravena")
#     time.sleep(t)
    
#     print(botonSend.is_enabled())
# else:
#     print("El elemento no se encuentra en la página")


if btn.is_enabled():
    print("El botón está habilitado")
    time.sleep(t)
else:
    print("El botón no está habilitado")

driver.quit()
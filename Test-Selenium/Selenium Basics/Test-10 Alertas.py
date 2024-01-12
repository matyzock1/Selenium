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

driver.get("https://demo.seleniumeasy.com/bootstrap-modal-demo.html")
driver.maximize_window()

#Le damos tiempo al navegador para localizar los elementos
driver.implicitly_wait(5)


#Localizamos el boton launch modal y le damos click
driver.find_element(By.XPATH, "//a[contains(text(),'Launch modal')]").click()
time.sleep(t)


#Realizamos un try-except para que valide que el elemento es visible
try:

    #La documentacion de selenium dice que para interactuar con las alertas se debe usar el driver.switch_to.alert
    
    #Aceptar la alerta
    # driver.switch_to.alert.accept()

    #Cancelar la alerta
    # driver.switch_to.alert.dismiss()
    
    buscar = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "(//a[@href='#'][contains(.,'Save changes')])[1]")))
    buscar = driver.find_element(By.XPATH, "(//a[@href='#'][contains(.,'Save changes')])[1]").click()
    time.sleep(t)
#Validamos que el elemento no existe, si es así se ejecuta el except
except TimeoutException as ex:
    print('El elemento no se encuentra en la página')
    
#Localizamos el boton launch modal y le damos click
driver.find_element(By.XPATH, "//a[contains(text(),'Launch modal')]").click()
time.sleep(t)

#Realizamos un try-except para que valide que el elemento es visible
try:
    buscar = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "(//a[@href='#'][contains(.,'Close')])[1]")))
    buscar = driver.find_element(By.XPATH, "(//a[@href='#'][contains(.,'Close')])[1]").click()
    time.sleep(t)

except TimeoutException as ex:
    print('El elemento no se encuentra en la página')


driver.close()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

t = 1

ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://testpages.herokuapp.com/styled/file-upload-test.html")
driver.maximize_window()

#Le damos tiempo al navegador para localizar los elementos
driver.implicitly_wait(5)

#Realizamos un try-except para que valide que el elemento es visible
try:
    #Validamos que el elemento existe, si es así podemos tomarlo
    SubirArchivo = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'fileinput')]")))

    #Seleccionamos el boton de subir archivo
    SubirArchivo = driver.find_element(By.XPATH, "//input[contains(@id,'fileinput')]")
    time.sleep(t)
    
    #Subimos el archivo con "send_keys"
    #No olvidar que las rutas en python es "//" y no "\" como en windows
    SubirArchivo.send_keys("C://Users//Matias Aravena F//Desktop//SELENIUM//Images//pajaro.jpg")
    time.sleep(t)

    #Validamos que el checkbox sea clickeable y lo clickeamos
    checkox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='itsanimage'][contains(.,'Image')]"))).click()
    time.sleep(t)

    #Validamos que el boton submit sea clickeable y lo clickeamos
    submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@type,'submit')]"))).click()
    time.sleep(t)

    print('Elemento enviado correctamente')
    driver.close()
    
#Validamos que el elemento no existe, si es así se ejecuta el except
except TimeoutException as ex:
    print('El elemento no se encuentra en la página')
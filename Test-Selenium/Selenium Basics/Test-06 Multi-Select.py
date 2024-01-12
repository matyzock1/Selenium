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

driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
driver.maximize_window()

#Le damos tiempo al navegador para localizar los elementos
driver.implicitly_wait(t)


#Bajamos 500 pixeles la página
driver.execute_script("window.scrollBy(0, 500);")

time.sleep(t)

#Realizamos un try-except para que valide que el elemento es visible
try:
    #Seleccionamos el elemento envolviendolo en un Select para poder seleccionar las opciones
    opcionSelect = Select(WebDriverWait(driver, t).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='multi-select']"))))

    #Seleccionamos a traves del index del elemento en lista
    opcionSelect.select_by_index(2)
    time.sleep(t)
    opcionSelect.select_by_index(3)
    time.sleep(t)
    opcionSelect.select_by_index(4)
    time.sleep(t)
    driver.close()

except TimeoutException as ex:
    print('El elemento no se encuentra en la página')
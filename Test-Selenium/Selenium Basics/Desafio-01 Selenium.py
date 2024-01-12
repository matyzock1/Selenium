from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


ser = Service("C:\Drivers\chromedriver.exe")


op = webdriver.ChromeOptions()

prefs = {
    'autofill.profile_enabled': False
}

op.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://demo.seleniumeasy.com/input-form-demo.html")

driver.maximize_window()
driver.implicitly_wait(5)

t = 1

try:
    form = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@name,'first_name')]")))

    form = driver.find_element(By.XPATH, "//input[contains(@name,'first_name')]").send_keys("Matias" + Keys.TAB + "Aravena"
    + Keys.TAB + "matyzock@gmail.com" + Keys.TAB + "9250515959" + Keys.TAB + "Pedro Fontova 7120" + Keys.TAB + "Santiago")

    time.sleep(t)

    #Esperamos a que sea clickeable el elemento
    seleccion = Select(driver.find_element(By.XPATH, "//select[contains(@name,'state')]"))
    seleccion.select_by_index(15)

    time.sleep(t)

    driver.find_element(By.XPATH, "//input[contains(@name,'zip')]").send_keys("1234" + Keys.TAB + "www.matyzock.com")
    
    time.sleep(t)

    driver.find_element(By.XPATH, "//input[contains(@value,'yes')]").click()

    driver.find_element(By.XPATH, "//textarea[contains(@class,'form-control')]").send_keys("Hola, este es un texto de prueba")

    time.sleep(t)

    driver.find_element(By.XPATH, "//button[contains(@class,'btn btn-default')]").click()

    time.sleep(t)
    print("El formulario se ha enviado correctamente")
    driver.close()

except TimeoutException as ex:
    print('El elemento no se encuentra en la página')

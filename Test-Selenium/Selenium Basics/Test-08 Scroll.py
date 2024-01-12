from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

t = 3

ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://pixabay.com/es/")
driver.maximize_window()

#Le damos tiempo al navegador para localizar los elementos
driver.implicitly_wait(5)


#Realizamos un try-except para que valide que el elemento es visible
try:
    #Validamos que el elemento existe, si es así podemos tomarlo
    Buscar = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(@class,'icon--L+lBh pinterest--QFbJv')])[2]")))

    #Nos posicionamos en el elemento
    Buscar = driver.find_element(By.XPATH, "(//span[contains(@class,'icon--L+lBh pinterest--QFbJv')])[2]")

    #Hacemos scroll hasta el elemento
    ir = driver.execute_script("arguments[0].scrollIntoView();", Buscar)
    time.sleep(t)
#Validamos que el elemento no existe, si es así se ejecuta el except
except TimeoutException as ex:
    print('El elemento no se encuentra en la página')
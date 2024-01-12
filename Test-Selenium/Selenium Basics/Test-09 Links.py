from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


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
    #obtenemos todos los links de la página
    # links = driver.find_elements(By.TAG_NAME, "a")

    # for x in links:
    #     print(x.text)

    #Buscamos el elemento por su LINK-TEXT y lo clickeamos
    driver.find_element(By.LINK_TEXT,"Input Forms").click()
    time.sleep(t)

    driver.find_element(By.LINK_TEXT,"Simple Form Demo").click()
    time.sleep(t)

    # print("La cantidad de links en la página es: ", len(links))

except TimeoutException as ex:
    print('El elemento no se encuentra en la página')

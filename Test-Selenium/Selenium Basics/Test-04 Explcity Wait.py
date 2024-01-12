from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://www.latercera.com")
driver.maximize_window()

#Esperamos que un elemento aparezca para realizar su accion!

elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='onesignal-slidedown-cancel-button']")))
elemento.click()

t = 5

click = driver.find_element(By.XPATH, "//a[@href='/politica/noticia/mesa-de-seguridad-toha-no-logra-sellar-pacto-con-partidos-y-apuesta-por-sumar-a-otras-fuerzas-politicas-de-aqui-a-marzo/72VSI3XIWVAG7BWRSF5V4NUJRM/'][contains(.,'Mesa de seguridad: Tohá no logra sellar pacto con partidos y apuesta por sumar a otras fuerzas políticas de aquí a marzo')]")
driver.execute_script("arguments[0].click();", click)

time.sleep(t)
driver.close()

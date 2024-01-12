from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ser = Service("C:\Drivers\chromedriver.exe")

op = webdriver.ChromeOptions()
#Desactivamos las notificaciones del navegador
op.add_argument("--disable-notifications")
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://idatesting.itdchile.cl")
driver.implicitly_wait(10)

driver.maximize_window()

delay = 1

#Iniciamos sesión en ITD
def iniciarSesion(tiempo):
    usuario = driver.find_element(By.XPATH, "//input[contains(@id,'j_username')]")
    usuario.send_keys('maravena')

    password = driver.find_element(By.XPATH, "//input[contains(@id,'j_password')]")
    password.send_keys('JKs3hNkt!')

    login = driver.find_element(By.XPATH, "//button[@class='fxt-btn-fill fondo-color'][contains(.,'Login')]")
    login.click()

    time.sleep(tiempo)
    

#Seleccionar la opción Mailing
def seleccionarMailing(tiempo):
    mailing = driver.find_element(By.XPATH, "//a[contains(@title,'Mailing')]")
    driver.execute_script("arguments[0].click();", mailing)

    time.sleep(tiempo)

    nuevoMasivo = driver.find_element(By.XPATH, "//span[contains(.,'Nuevo Mail Masivo')]")
    driver.execute_script("arguments[0].click();", nuevoMasivo)
    time.sleep(tiempo)

    crearMensaje = driver.find_element(By.XPATH, "//input[contains(@value,'Crear Mensaje')]")
    driver.execute_script("arguments[0].click();", crearMensaje)
    time.sleep(tiempo)

    driver.find_element(By.XPATH, "//div[contains(@id,'messageWs')]").send_keys("Asunto de prueba" + Keys.TAB + 'Bajada de Prueba' + Keys.TAB + 'Cuerpo de Prueba')
    time.sleep(tiempo)


iniciarSesion(delay)
seleccionarMailing(delay)

driver.close()
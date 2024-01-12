import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from Funciones.function import Funciones_globlales


class Pagina_Login():
    
    def __init__(self, driver):
        self.driver = driver
    
    #Recibimos los parametros del archivo test.py
    def Login_Master(self ,url, text, clave, tiempo):
        driver = self.driver
        f = Funciones_globlales(driver)

        #Llamamos a las funciones del archivo function.py y les pasamos los parametros
        f.navegar(url, tiempo)
        f.texto_mixto("id", "user-name", text, tiempo)
        f.texto_mixto("id", "password", clave, tiempo)
        # f.text_id("user-name", name, tiempo)
        # f.text_id("password", clave, tiempo)
        f.boton("xpath","//input[contains(@id,'login-button')]", tiempo)
        f.error("//h3[contains(@data-test,'error')]", tiempo)
    
    def login_2(self, url, text, tiempo):
        driver = self.driver
        f = Funciones_globlales(driver)

        f.navegar(url, tiempo)
        f.texto_mixto('id', 'userName', text, tiempo)
        f.texto_mixto('id', 'userEmail', text, tiempo)
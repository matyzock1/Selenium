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


class Upload_File():
    
    def __init__(self, driver):
        self.driver = driver
    
    #Recibimos los parametros del archivo test.py
    def upload_master(self ,url, file, tiempo):
        driver = self.driver
        f = Funciones_globlales(driver)

        #Llamamos a las funciones del archivo function.py y les pasamos los parametros
        f.navegar(url, tiempo)
        f.uploadFile("//input[contains(@id,'fileinput')]", file, tiempo)
        f.checkbox("//input[contains(@id,'itsanimage')]", tiempo)
        f.boton("//input[contains(@type,'submit')]", tiempo)
    
    def checkbox_radio(self, url, tiempo):
        driver = self.driver
        f = Funciones_globlales(driver)
        f.navegar(url, tiempo)
        f.checkbox_radio("//input[contains(@id,'isAgeSelected')]", tiempo)

    def multiple_select(self, url, tiempo):
        driver = self.driver
        f = Funciones_globlales(driver)
        f.navegar(url, tiempo)

        #For para seleccionar los checkbox de la pagina iterando el valor de su posicion
        for n in range(2,6):
            f.multiple_select(tiempo, "(//input[@type='checkbox'])["+str(n)+"]")
            
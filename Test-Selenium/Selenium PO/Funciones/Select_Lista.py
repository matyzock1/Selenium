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


class Select_Item():
    
    def __init__(self, driver):
        self.driver = driver
    
    #Recibimos los parametros del archivo test.py
    def select_item(self ,url, tipo, texto, tiempo):
        driver = self.driver
        f = Funciones_globlales(driver)

        #Llamamos a las funciones del archivo function.py y les pasamos los parametros
        f.navegar(url, tiempo)
        f.select_type("//select[contains(@id,'select-demo')]", tipo, texto, tiempo)
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
from Funciones.Page_Login import Pagina_Login
from Funciones.Select_Lista import Select_Item
from Funciones.Upload_Page import Upload_File
from Funciones.function import Funciones_globlales

tiempo = .5

#Corremos los casos de uso del login, donde las funciones vienen del archivo Page_Login.py
class PlantillaTest(unittest.TestCase):

    def setUp(self):
        ser = Service(r"C://Drivers//chromedriver.exe")
        op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ser, options=op)

    def test_uno(self):
        driver = self.driver
        
        #Instanciamos la clase Pagina_Login
        pg = Pagina_Login(driver)
        #Llamamos a la funcion Login_Master y le pasamos los parametros
        pg.Login_Master("https://www.saucedemo.com","standard_user","secret_sauce" ,tiempo)
    
    def test_dos(self):
        driver = self.driver

        pg = Pagina_Login(driver)
        pg.Login_Master("https://www.saucedemo.com","problem_user", "secret_sauce", tiempo)


    def test_tres(self):
        driver = self.driver

        pg = Pagina_Login(driver)
        pg.Login_Master("https://www.saucedemo.com","standard_user","" ,tiempo)


    def test_cuatro(self):
        driver = self.driver

        pg = Pagina_Login(driver)
        pg.Login_Master("https://www.saucedemo.com","","" ,tiempo)

    def test_cinco(self):
        driver = self.driver

        pg = Pagina_Login(driver)
        pg.Login_Master("https://www.saucedemo.com","sadasdsad","asdasdsad" ,tiempo)

    def test_select(self):
        driver = self.driver
        
        pg = Select_Item(driver)
        pg.select_item("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html", "index", "4", tiempo)

    def test_upload(self):
        driver = self.driver

        pg = Upload_File(driver)
        pg.upload_master("https://testpages.herokuapp.com/styled/file-upload-test.html", "C://Users//Matias Aravena F//Pictures//asd.png", tiempo)


    def test_checkbox(self):
        driver = self.driver

        pg = Upload_File(driver)
        pg.checkbox_radio("https://demo.seleniumeasy.com/basic-checkbox-demo.html", tiempo)

    def test_multiple(self):
        driver = self.driver

        pg = Upload_File(driver)
        pg.multiple_select("https://demo.seleniumeasy.com/basic-checkbox-demo.html", tiempo)
    
    def test_formulario(self):
        driver = self.driver
        pg = Pagina_Login(driver)

        pg.login_2("https://demoqa.com/text-box", "Matias Aravena", tiempo)
        pg.login_2("https://demoqa.com/text-box", "matyzock@gmail.com", tiempo)


    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    # unittest.main(warnings='ignore')
    print("test")

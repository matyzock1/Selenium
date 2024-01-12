import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

#Creamos las funciones globales que vamos a utilizar en los casos de uso
class Funciones_globlales():
    
    def __init__(self, driver):
        self.driver = driver
    
    def navegar(self, url, tiempo):
        driver = self.driver
        driver.get(url)
        print('Se abrió la página: ', url)
        driver.maximize_window()
        t = time.sleep(tiempo)
        return t

    def boton(self, tipo, selector, tiempo):
        driver = self.driver
        if tipo == 'xpath':
            try:
                boton = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, selector)))
                boton = driver.execute_script("arguments[0].scrollIntoView();", boton)
                boton = driver.find_element(By.XPATH, selector)
                print('Se hizo click en el elemento: ', selector)
                boton.click()
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print('El elemento no se encuentra en la página', selector)
        elif tipo == 'id':
            try:
                boton = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, selector)))
                boton = driver.execute_script("arguments[0].scrollIntoView();", boton)
                boton = driver.find_element(By.ID, selector)
                print('Se hizo click en el elemento: ', selector)
                boton.click()
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print('El elemento no se encuentra en la página', selector)
        else:
            print('El tipo de selección no es correcto.')


    def texto_mixto(self, tipo, selector, text, tiempo):
        driver = self.driver
        if tipo == 'xpath':
            try:
                t = time.sleep(tiempo)
                texto = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, selector)))
                texto = driver.execute_script("arguments[0].scrollIntoView();", texto)
                texto = driver.find_element(By.XPATH, selector)   
                texto.clear()
                texto.send_keys(text)
                print('Se ingreso en el elemento: ', selector, 'el texto: ', text)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print('El elemento no se encuentra en la página', selector)

        elif tipo == 'id':
                try:
                    t = time.sleep(tiempo)
                    texto = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, selector)))
                    texto = driver.execute_script("arguments[0].scrollIntoView();", texto)
                    texto = driver.find_element(By.ID, selector)
                    texto.clear()
                    texto.send_keys(text)
                    print('Se ingreso en el elemento: ', selector, 'el texto: ', text)
                    return t
                except TimeoutException as ex:
                    print(ex.msg)
                    print('El elemento no se encuentra en la página', selector)
        else:
            print('El tipo de selección no es correcto.')

    def error(self, xpath, tiempo):
        driver = self.driver
        try:
            t = time.sleep(tiempo)
            error = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
            error = driver.execute_script("arguments[0].scrollIntoView();", error)
            error = driver.find_element(By.XPATH, xpath)

            if error.text == 'Epic sadface: Username and password do not match any user in this service':
                    print('Error encontrado: El usuario y contraseña no coinciden')
            elif error.text == 'Epic sadface: Password is required':
                    print('Error encontrado: La contraseña es requerida')
            elif error.text == 'Epic sadface: Username is required':
                    print('Error encontrado: El usuario es requerido')
            else:
                    print('Logeado correctamente.')
            return t
            
        except TimeoutException as ex:
                print(ex.msg)
                print('No se encontró un mensaje de error.')
    
    # def text_id(self, xpath, text, tiempo):
    #     driver = self.driver
    #     try:
    #         t = time.sleep(tiempo)
    #         texto = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, xpath)))
    #         texto = driver.execute_script("arguments[0].scrollIntoView();", texto)
    #         texto = driver.find_element(By.ID, xpath)
    #         texto.clear()
    #         texto.send_keys(text)
    #         print('Se ingresó el texto: ', text, 'en el elemento: ', xpath)
    #         return t
    #     except TimeoutException as ex:
    #         print(ex.msg)
    #         print('El elemento no se encuentra en la página', xpath)

    # def text_xpath(self, xpath, text, tiempo):
    #     driver = self.driver
    #     try:
    #         t = time.sleep(tiempo)
    #         texto = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
    #         texto = driver.execute_script("arguments[0].scrollIntoView();", texto)
    #         texto = driver.find_element(By.XPATH, xpath)   
    #         texto.clear()
    #         texto.send_keys(text)
    #         print('Se ingresó el texto: ', text, 'en el elemento: ', xpath)
    #         return t
    #     except TimeoutException as ex:
    #         print(ex.msg)
    #         print('El elemento no se encuentra en la página', xpath)

    def select_type(self, xpath, tipo, text, tiempo):
        driver = self.driver
        try:
            t = time.sleep(tiempo)
            select = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
            select = driver.execute_script("arguments[0].scrollIntoView();", select)
            select = driver.find_element(By.XPATH, xpath)
            select = Select(select)
            if tipo == "value":
                select.select_by_value(text)
            elif tipo == "index":
                select.select_by_index(text)
            elif tipo == "text":
                select.select_by_visible_text(text)
            else:
                print('El tipo de selección no es correcto.')
            t = time.sleep(tiempo)
            print('Se seleccionó el elemento: ', xpath, 'con el texto: ', text)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print('El elemento no se encuentra en la página', xpath)

    def uploadFile(self, xpath, file, tiempo):
        driver = self.driver
        driver.implicitly_wait(5)
        try:
            upload = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
            upload = driver.execute_script("arguments[0].scrollIntoView();", upload)
            upload = driver.find_element(By.XPATH, xpath)
            delay = time.sleep(tiempo)
            upload.send_keys(file)
            print('Se subió el archivo: ', file, 'en el elemento: ', xpath)
            tiempo = time.sleep(tiempo)
            return delay
        except TimeoutException as ex:
            print(ex.msg)
            print('El elemento no se encuentra en la página', xpath)
            return delay

    def checkbox(self, xpath, tiempo):
        driver = self.driver
        try:
            checkbox = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
            checkbox = driver.execute_script("arguments[0].scrollIntoView();", checkbox)
            checkbox = driver.find_element(By.XPATH, xpath)
            checkbox.click()
            t = time.sleep(tiempo)
            print('Se hizo click en el elemento: ', xpath)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print('El elemento no se encuentra en la página', xpath)


    def checkbox_radio(self, xpath, tiempo):
        driver = self.driver
        try:
            checkbox = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
            checkbox = driver.execute_script("arguments[0].scrollIntoView();", checkbox)
            checkbox = driver.find_element(By.XPATH, xpath)
            checkbox.click()
            t = time.sleep(tiempo)
            print('Se hizo click en el elemento: ', xpath)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print('El elemento no se encuentra en la página', xpath)

    def multiple_select(self, tiempo, *args):
        driver = self.driver
        try:
            for num in args:
                checkbox = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, num)))
                checkbox = driver.execute_script("arguments[0].scrollIntoView();", checkbox)
                checkbox = driver.find_elements(By.XPATH, num)
                #Para seleccionar todos los checkbox se hace un for
                for chk in checkbox:
                    chk.click()
                    print('Se hizo click en el elemento: ', num)
                t = time.sleep(tiempo)
                return t
        except TimeoutException as ex:
            for num in args:
                print(ex.msg)
                print('El elemento no se encuentra en la página', num)  
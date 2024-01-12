from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C://Drivers//chromedriver.exe")
        self.driver.maximize_window()

    def test_nada(self):
        driver = self.driver
        driver.get("https://demoqa.com/text-box")
        
        print("Iniciando test")
        
        nombre = driver.find_element(By.XPATH, "//input[contains(@id,'userName')]")
        email = driver.find_element(By.XPATH, "//input[contains(@id,'userEmail')]")
        desc = driver.find_element(By.XPATH, "//textarea[contains(@id,'currentAddress')]")
        address = driver.find_element(By.XPATH, "//textarea[contains(@id,'permanentAddress')]")
        boton = driver.find_element(By.XPATH, "//button[contains(@id,'submit')]")
        
        nombre.send_keys("FEINT LA MEA CORNETA")
        time.sleep(1)
        email.send_keys("feint@gmail.com")
        time.sleep(1)
        desc.send_keys("FEINT LA MEA CORNETA EN LA RAJA")
        time.sleep(1)
        address.send_keys("pico en la cuea 1398")
        time.sleep(1)
        boton.click()
        
        
        # Wait for error message
        error = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
        )
        
        error_text = error.text
        if "Epic sadface: Username is required" in error_text:
            print("Falta agregar el nombre de usuario y la contraseña")
        else:
            print("No falta agregar nada")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
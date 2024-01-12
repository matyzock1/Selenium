from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import unittest



class PlantillaTest(unittest.TestCase):

    def setUp(self):
        ser = Service(r"C:\Users\S0C\Downloads\chrome-win64\chrome-win64\chrome.exe")
        op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ser, options=op)
        self.driver.maximize_window()

    def test_uno(self):
        driver = self.driver
        driver.get("https://www.google.com/")
        time.sleep(2)

    def tearDown(self):
        driver = self.driver
        driver.close()


if __name__ == '__main__':
    unittest.main()

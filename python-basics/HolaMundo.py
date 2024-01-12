from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("https://idatesting.itdchile.cl/login.jsp")

print('Bienvenido a', driver.title)

driver.close()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

t = 3

ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")
driver.maximize_window()
driver.implicitly_wait(10)


#Bajamos 500 pixeles la página
# driver.execute_script("window.scrollBy(0, 500);")

try:
    opcionSelect = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='post-2646']/div[2]/div/div/div/p/select")))
    
    # Creamos un objeto de la clase Select y le pasamos el elemento seleccionado
    ds = Select(opcionSelect)

    # Seleccionamos la opcion por el texto
    ds.select_by_visible_text("Argentina")
    time.sleep(t)

    # Seleccionamos la opcion por el index
    ds.select_by_index(2)

    time.sleep(t)
    # Seleccionamos por el value (inspeccionar elemento)
    ds.select_by_value("CAN")

    time.sleep(t)
    driver.close()

except:
    driver.quit()



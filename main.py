from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "https://cdp2020.chapeaudepaille.fr/backend_dev.php"
driver_Chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver_Chrome.get("https://cdp2020.chapeaudepaille.fr/backend_dev.php")
driver_Chrome.maximize_window()
driver_Chrome.get(url)
driver_Chrome.find_element(By.ID, "details-button").click()
driver_Chrome.find_element(By.ID, "proceed-link").click()


driver_Chrome.implicitly_wait(15)
driver_Chrome.find_element(By.ID, "signin_username").send_keys("super-admin-1")
driver_Chrome.find_element(By.ID, "signin_password").send_keys("CDPtest@1")
driver_Chrome.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/form[1]/div[3]/input[1]").click()

menu = driver_Chrome.find_element(By.XPATH, "//a[contains(@class,'sf-with-ul')][normalize-space()='Pages']")
action = ActionChains(driver_Chrome)
action.move_to_element(menu).perform()
driver_Chrome.implicitly_wait(10)
menu = driver_Chrome.find_element(By.XPATH, "(//a[contains(@class,'expand sf-with-ul subClosed')][normalize-space("
                                            ")='Produits'])[1]")
action = ActionChains(driver_Chrome)
action.move_to_element(menu).perform()
driver_Chrome.implicitly_wait(10)
driver_Chrome.find_element(By.XPATH, "//li[contains(@class,'sfHover')]//a[contains(@title,'Liste des "
                                     "Produits')][contains(text(),'Liste')]").click()
driver_Chrome.implicitly_wait(15)
driver_Chrome.find_element(By.XPATH, "//a[normalize-space()='Ajouter un produit']").click()
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from Pages import BASE_PAGE

from Pages.BASE_PAGE import datalist
Visite = datalist['Visite'][0]

def Dropdown(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        Button = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[1]')
        Dropdown = Actions.move_to_element(Button)
        Dropdown.click().perform()
    except NoSuchElementException:
        print("Dropdown : No Such Element")

def Dropdown_element1(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        Dropdownelement1 = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[1]/ul/li[1]')
        Button = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[1]')
        Dropdown = Actions.move_to_element(Button)
        Dropdown.click().perform()
        Dropdownelement1.click()
        time.sleep(3)
    except NoSuchElementException:
        print("Dropdown_element1 : No Such Element")

def Dropdown_element2(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        Dropdownelement2 = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[1]/ul/li[2]')
        Button = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[1]')
        Dropdown = Actions.move_to_element(Button)
        Dropdown.click().perform()
        Dropdownelement2.click()
        time.sleep(3)
    except NoSuchElementException:
        print("Dropdown_element2 : No Such Element")

def Dropdown_element3(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        Dropdownelement3 = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[1]/ul/li[3]')
        Button = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[1]')
        Dropdown = Actions.move_to_element(Button)
        Dropdown.click().perform()
        Dropdownelement3.click()
        time.sleep(3)
    except NoSuchElementException:
        print("Dropdown_element3 : No Such Element")

def Dropdown_element4(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        Dropdownelement4 = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[1]/ul/li[4]')
        Button = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[1]')
        Dropdown = Actions.move_to_element(Button)
        Dropdown.click().perform()
        Dropdownelement4.click()
        time.sleep(3)
    except NoSuchElementException:
        print("Dropdown_element4 : No Such Element")

def Dropdown_element5(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        Dropdownelement5 = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[1]/ul/li[5]')
        Button = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[1]')
        Dropdown = Actions.move_to_element(Button)
        Dropdown.click().perform()
        Dropdownelement5.click()
    except NoSuchElementException:
        print("Dropdown_element5 : No Such Element")

def Images(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        Img = Driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div[4]/div/ul[1]/li[1]/a/div/span')
        Img.click()
        closeButton = Driver.find_element(By.CSS_SELECTOR, 'a[class="pp_close"]')
        closeButton.click()

    except NoSuchElementException:
        print("Images : No Such Element")
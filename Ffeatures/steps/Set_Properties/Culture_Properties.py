import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Pages import BASE_PAGE


def Dropdown(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        Dropdown = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[3]')
        VisiteDropdown = Actions.move_to_element(Dropdown)
        VisiteDropdown.click().perform()
    except NoSuchElementException:
        print("Dropdown : No Such Element")

def Dropdown_element1(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        Dropdown1 = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[3]/ul/li[1]')
        Dropdown = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[3]')
        VisiteDropdown = Actions.move_to_element(Dropdown)
        VisiteDropdown.click().perform()
        time.sleep(3)
        Dropdown1.click()
        time.sleep(5)
    except NoSuchElementException:
        print("Dropdown_element1 : No Such Element")

def Dropdown_element2(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        Dropdown2 = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[3]/ul/li[2]')
        Dropdown = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[3]')
        VisiteDropdown = Actions.move_to_element(Dropdown)
        VisiteDropdown.click().perform()
        time.sleep(3)
        Dropdown2.click()
        time.sleep(5)
    except NoSuchElementException:
        print("Dropdown_element2 : No Such Element")

def Dropdown_element3(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        Dropdown3 = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[3]/ul/li[3]')
        Dropdown = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[3]')
        VisiteDropdown = Actions.move_to_element(Dropdown)
        VisiteDropdown.click().perform()
        time.sleep(3)
        Dropdown3.click()
        time.sleep(5)
    except NoSuchElementException:
        print("Dropdown_element3 : No Such Element")

def Dropdown_element4(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        Dropdown4 = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[3]/ul/li[4]')
        Dropdown = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[3]')
        VisiteDropdown = Actions.move_to_element(Dropdown)
        VisiteDropdown.click().perform()
        time.sleep(3)
        Dropdown4.click()
        time.sleep(5)
    except NoSuchElementException:
        print("Dropdown_element4 : No Such Element")

def Dropdown_element5(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        Dropdown5 = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[3]/ul/li[5]')
        Dropdown = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[3]')
        VisiteDropdown = Actions.move_to_element(Dropdown)
        VisiteDropdown.click().perform()
        time.sleep(3)
        Dropdown5.click()
        time.sleep(5)
        BASE_PAGE.Button_close(context)
    except NoSuchElementException:
        print("Dropdown_element5 : No Such Element")
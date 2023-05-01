from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import *
from selenium.webdriver import ActionChains
from  Pages import BASE_PAGE


def Dropdown(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        Button = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[2]')
        Button.click()
    except NoSuchElementException:
        print("No Such Element")

def Dropdown_element1(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        element1 = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[2]/ul/li[1]')
        element = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[2]')
        Dropdown = Actions.move_to_element(element)
        Dropdown.perform()
        BASE_PAGE.Button_close(context)
        element1.click()
    except NoSuchElementException:
        print("No Such Element")

def Dropdown_element2(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        element2 = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[2]/ul/li[2]')
        element = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[2]')
        Dropdown = Actions.move_to_element(element)
        Dropdown.perform()
        BASE_PAGE.Button_close(context)
        element2.click()
    except NoSuchElementException:
        print("No Such Element")

def Dropdown_element3(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        element3 = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[2]/ul/li[3]')
        element = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[2]')
        Dropdown = Actions.move_to_element(element)
        Dropdown.perform()
        BASE_PAGE.Button_close(context)
        element3.click()
    except NoSuchElementException:
        print("No Such Element")

def Recette(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        Recette = Driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div/a/div/div[2]/div')
        Recette.click()
        Driver.back()
    except NoSuchElementException:
        print("No Such Element")

def fruit(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        fruit = Driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/section[1]/div/div/div/a/img')
        fruit.click()
        Driver.back()
    except NoSuchElementException:
        print("No Such Element")

def legume(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        legume = Driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/section[2]/div/div/div/a/img')
        legume.click()
        Driver.back()
    except NoSuchElementException:
        print("No Such Element")

def fleur(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        fleur = Driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/section[3]/div/div/div/a/img')
        fleur.click()
        Driver.back()
    except NoSuchElementException:
        print("No Such Element")

def Suivant(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        Suivant = Driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div[1]/ul/div/li[2]/a/div[1]')
        Suivant.click()
    except NoSuchElementException:
        print("No Such Element")

def Precedant(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        Precedant = Driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div[1]/ul/div/li[1]/a/div[1]')
        Precedant.click()
    except NoSuchElementException:
        print("No Such Element")

def Tout(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        Tout = Driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div[1]/ul/li/a/div[1]')
        Tout.click()
    except NoSuchElementException:
        print("No Such Element")
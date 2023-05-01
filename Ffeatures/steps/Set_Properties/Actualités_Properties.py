from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import os
from selenium import webdriver

from Pages import BASE_PAGE
from Pages.BASE_PAGE import datalist
Actualités = datalist['Actualités'][0]


def StartPage(context):
    os.environ['PATH'] += "C:\SeleniumDriver"
    context.driver = webdriver.Chrome()
    Driver = context.driver
    Driver.maximize_window()
    Driver.get("https://pithienville.cdp2020.chapeaudepaille.fr/actualites-de-la-cueillette-pithienville-27")
    Driver.implicitly_wait(5)

def Events(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        Tout_button = Driver.find_element(By.XPATH, '//*[@id="content-widget"]/div/div[1]')
        Tout_button.click()
        event_button = Driver.find_element(By.XPATH, '//*[@id="categ-select"]/option[2]')
        event_button.click()
    except NoSuchElementException:
        print("No Such Element")

def Recherche(context, recherche):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        search = Driver.find_element(By.XPATH, '//*[@id="content-widget"]/div/div[2]/form/div/input')
        search.send_keys(recherche)
        search_button = Driver.find_element(By.XPATH, '//*[@id="content-widget"]/div/div[2]/form/div/button')
        search_button.click()
    except NoSuchElementException:
        print("No Such Element")

def Actualité(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        Actualité_button = Driver.find_element(By.XPATH, '//*[@id="content-blog"]/div[1]/div/a/div/div[2]/h2')
        Actualité_button.click()
    except NoSuchElementException:
        print("No Such Element")

def OtherActualité(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        Actualité_button = Driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div[2]/div/div[3]/a/div[2]/h3')
        Actualité_button.click()
    except NoSuchElementException:
        print("No Such Element")
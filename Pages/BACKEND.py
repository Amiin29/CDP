import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, \
    ElementClickInterceptedException
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options


def LandHomePage(context):
    os.environ['PATH'] += "C:\SeleniumDriver"
    context.driver = webdriver.Chrome()
    Driver = context.driver
    Driver.maximize_window()
    Driver.get("https://cdp2020.chapeaudepaille.fr/backend.php/")
    Driver.implicitly_wait(3)

def LandProductsPage(context):
    os.environ['PATH'] += "C:\SeleniumDriver"
    context.driver = webdriver.Chrome()
    Driver = context.driver
    Driver.maximize_window()
    Driver.get("https://cdp2020.chapeaudepaille.fr/backend.php/produits/liste-des-produits.html")
    Driver.implicitly_wait(3)

def LandVarietiesPage(context):
    os.environ['PATH'] += "C:\SeleniumDriver"
    context.driver = webdriver.Chrome()
    Driver = context.driver
    Driver.maximize_window()
    Driver.get("https://cdp2020.chapeaudepaille.fr/backend.php/varieties.html")
    Driver.implicitly_wait(3)

def LandRecettesPage(context):
    os.environ['PATH'] += "C:\SeleniumDriver"
    context.driver = webdriver.Chrome()
    Driver = context.driver
    Driver.maximize_window()
    Driver.get("https://cdp2020.chapeaudepaille.fr/backend.php/recettes/liste-des-recettes.html")
    Driver.implicitly_wait(3)
def CalendrierRecoltePage(context):
    os.environ['PATH'] += "C:\SeleniumDriver"
    context.driver = webdriver.Chrome()
    Driver = context.driver
    Driver.maximize_window()
    Driver.get("https://pithienville.cdp2020.chapeaudepaille.fr/calendrier-fruits-legumes-fleurs-recoltes-cueillette-pithienville-27.html")
    Driver.implicitly_wait(3)
def Security(context):
    Driver = context.driver
    try:
        btn1 = Driver.find_element(By.ID, "details-button").click()
        btn2 = Driver.find_element(By.ID, "proceed-link").click()
    except NoSuchElementException:
        print("No Such Element")

def Login(context):
    Driver = context.driver
    try:
        Identifiant = Driver.find_element(By.ID, "signin_username")
        Identifiant.send_keys("super-admin-1")
        Mdp = Driver.find_element(By.ID, "signin_password")
        Mdp.send_keys("CDPtest@1")
        LoginBtn = Driver.find_element(By.XPATH, '/html/body/div/div/div[2]/form/div[3]/input')
        LoginBtn.click()
    except NoSuchElementException:
        print("No Such Element")

def Pithienville(context):
    Driver = context.driver
    try:
        CDP = Driver.find_element(By.ID, "select2-switch-cueillette-container")
        CDP.click()
        Recherche = Driver.find_element(By.XPATH,'/html/body/span/span/span[1]/input')
        Recherche.send_keys("Pithienville")
        Recherche.send_keys(Keys.ENTER)
    except NoSuchElementException:
        print("Pithienville = No Such Element")


def Close(context):
    Driver = context.driver
    Driver.quit()
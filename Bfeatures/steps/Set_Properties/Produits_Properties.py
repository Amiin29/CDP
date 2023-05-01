import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
def Ajout(context):
    Driver = context.driver
    try:
        AjoutBtn = Driver.find_element(By.CSS_SELECTOR, 'a[href="/backend.php/produits/ajouter-produit.html"]')
        AjoutBtn.click()
        time.sleep(10)
    except NoSuchElementException:
        print("AjoutButton : No Such Element")
def Titre(context,Titre):
    Driver = context.driver
    try:
        TitreBtn = Driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[4]/div/form/fieldset/div/div[2]/div[1]/div[1]/div[1]/div/input')
        TitreBtn.clear()
        TitreBtn.send_keys(Titre)
    except NoSuchElementException:
        print("Titre : No Such Element")

def Categories(context,categorie):
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        Categories = Driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/span[1]/span[1]')
        Slideshow = Actions.move_to_element(Categories)
        Slideshow.perform()
        Categorie = Driver.find_element(By.XPATH, '/html/body/span/span/span[1]/input')
        Categorie.send_keys(categorie)
        Categorie.send_keys(Keys.ENTER)
    except NoSuchElementException:
        print("Categories : No Such Element")

def Historique(context,historique):
    Driver = context.driver
    try:
        HisBtn = Driver.find_element(By.ID,"editor-container-1")
        HisBtn.send_keys(historique)
    except NoSuchElementException:
        print("Historique : No Such Element")

def Prop(context,prop):
    Driver = context.driver
    try:
        PropBtn = Driver.find_element(By.ID,"editor-container-2")
        PropBtn.send_keys(prop)
    except NoSuchElementException:
        print("Prop : No Such Element")

def Astuces(context,astuces):
    Driver = context.driver
    try:
        AstucesBtn = Driver.find_element(By.XPATH, '//*[@id="editor-container-3"]/div[1]')
        AstucesBtn.send_keys(astuces)
    except NoSuchElementException:
        print("Astuces : No Such Element")

def DescImages(context,desc):
    Driver = context.driver
    try:
        DescBtn = Driver.find_element(By.ID,"product_product_image_alt")
        DescBtn.send_keys(desc)
    except NoSuchElementException:
        print("Description Image : No Such Element")

def Sauvegarder(context):
    Driver = context.driver
    try:
        btn = Driver.find_element(By.XPATH, '//*[@id="usualValidate"]/fieldset/div/div[2]/div[2]/input')
        btn.click()
    except NoSuchElementException:
        print("Sauvegarder : No Such Element")

def Suppression(context):
    Driver = context.driver
    try:
        btn = Driver.find_element(By.XPATH, '//*[@id="deleteItem"]/b')
        btn.click()
    except NoSuchElementException:
        print("Suppression : No Such Element")

def Modification(context):
    Driver = context.driver
    try:
        btn = Driver.find_element(By.XPATH,'//*[@id="products-table"]/tbody/tr[1]/td[5]/ul/li[1]/a[1]/b')
        btn.click()
    except NoSuchElementException:
        print("Modification : No Such Element")

def Recherche(context,recherche):
    Driver = context.driver
    try:
        btn = Driver.find_element(By.XPATH, '//*[@id="products-table_filter"]/label/input')
        btn.clear()
        btn.send_keys(recherche)
    except NoSuchElementException:
        print("Recherche : No Such Element")

def AlerteOui(context):
    Driver = context.driver
    try:
        btn = Driver.find_element(By.ID,"confirmDelete")
        btn.click()
    except NoSuchElementException:
        print("Alerte Oui : No Such Element")

import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

def Ajout(context):
    Driver = context.driver
    try:
        AjoutBtn = Driver.find_element(By.CSS_SELECTOR, 'a[href="/backend.php/ajouter-variete.html"]')
        AjoutBtn.click()
        time.sleep(10)
    except NoSuchElementException:
        print("AjoutButton : No Such Element")

def Produits(context,produit):
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        Produits = Driver.find_element(By.ID, "select2-product_variety_product_id-container")
        Slideshow = Actions.move_to_element(Produits)
        Slideshow.perform()
        Produit = Driver.find_element(By.XPATH, '/html/body/span/span/span[1]/input')
        Produit.send_keys(produit)
        Produit.send_keys(Keys.ENTER)
    except NoSuchElementException:
        print("Produits : No Such Element")

def Titre(context,titre):
    Driver = context.driver
    try:
        TitreBtn = Driver.find_element(By.ID, "product_variety_product_variety_title")
        TitreBtn.send_keys(titre)
    except NoSuchElementException:
        print("Titre : No Such Element")

def Contenu(context,contenu):
    Driver = context.driver
    try:
        Btn = Driver.find_element(By.XPATH,'//*[@id="editor-container-1"]/div[1]')
        Btn.send_keys(contenu)
    except NoSuchElementException:
        print("Contenu : No Such Element")

def Sauvegarder(context):
    Driver = context.driver
    try:
        btn = Driver.find_element(By.XPATH, '//*[@id="usualValidate"]/fieldset/div/div[5]/input')
        btn.click()
    except NoSuchElementException:
        print("Sauvegarder : No Such Element")

def Modification(context):
    Driver = context.driver
    try:
        btn = Driver.find_element(By.XPATH,'//*[@id="variety-table"]/tbody/tr[1]/td[4]/ul/li[1]/a[1]/b')
        btn.click()
    except NoSuchElementException:
        print("Modification : No Such Element")

def Recherche(context,recherche):
    Driver = context.driver
    try:
        btn = Driver.find_element(By.XPATH, '//*[@id="variety-table_filter"]/label/input')
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

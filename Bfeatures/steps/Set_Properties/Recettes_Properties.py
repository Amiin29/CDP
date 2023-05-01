import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

def ActiverModule(context):
    Driver = context.driver
    try:
        Btn = Driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div[1]/div/div/div/div/div/div[1]/div/div")
        Btn.click()
        time.sleep(3)
    except NoSuchElementException:
        print("ActiverModule : No Such Element")

def ActiverRecette(context):
    Driver = context.driver
    try:
        Btn = Driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[4]/div/div[2]/div/div/div/div/div/div[1]/div/div')
        Btn.click()
        time.sleep(3)
    except NoSuchElementException:
        print("ActiverRecette : No Such Element")
def Ajout(context):
    Driver = context.driver
    try:
        Btn = Driver.find_element(By.ID, "add")
        Btn.click()
        time.sleep(3)
    except NoSuchElementException:
        print("AjoutButton : No Such Element")
def Suppression(context):
    Driver = context.driver
    try:
        Btn = Driver.find_element(By.XPATH, '//*[@id="deleteItem"]/strong')
        Btn.click()
        time.sleep(2)
    except NoSuchElementException:
        print("Suppression : No Such Element")
def Modification(context):
    Driver = context.driver
    try:
        Btn = Driver.find_element(By.XPATH, '//*[@id="edit"]/strong')
        Btn.click()
        time.sleep(2)
    except NoSuchElementException:
        print("Modification : No Such Element")
def Publier(context):
    Driver = context.driver
    try:
        Btn = Driver.find_element(By.XPATH, '//*[@id="1644"]/td[7]/div/div[2]/div[1]')
        Btn.click()
        time.sleep(2)
    except NoSuchElementException:
        print("Publier : No Such Element")
def Publiées(context):
    Driver = context.driver
    try:
        Btn = Driver.find_element(By.ID,"published")
        Btn.click()
        time.sleep(2)
    except NoSuchElementException:
        print("Publiées : No Such Element")
def NPubliées(context):
    Driver = context.driver
    try:
        Btn = Driver.find_element(By.ID,"notpublished")
        Btn.click()
        time.sleep(2)
    except NoSuchElementException:
        print("NPubliées : No Such Element")

def VoirTous(context):
    Driver = context.driver
    try:
        Btn = Driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div[2]/a')
        Btn.click()
        time.sleep(2)
    except NoSuchElementException:
        print("VoirTous : No Such Element")

def Recherche(context,nom):
    Driver = context.driver
    try:
        Btn = Driver.find_element(By.XPATH, '//*[@id="recette-table_filter"]/label/input')
        Btn.click()
        Btn.clear()
        Btn.send_keys(nom)
        time.sleep(2)
    except NoSuchElementException:
        print("Recherche : No Such Element")
        
def Titre(context,titre):
    Driver = context.driver
    try:
        Btn = Driver.find_element(By.ID, "recette_seo_recette_title")
        Btn.click()
        Btn.clear()
        Btn.send_keys(titre)
        time.sleep(2)
    except NoSuchElementException:
        print("Titre : No Such Element")
def Resume(context,resume):
    Driver = context.driver
    try:
        Btn = Driver.find_element(By.ID, "editor-container-1")
        Btn.click()
        Btn.clear()
        Btn.send_keys(resume)
        time.sleep(2)
    except NoSuchElementException:
        print("Resume : No Such Element")
def Ingredient(context,ingredient):
    Driver = context.driver
    try:
        Btn = Driver.find_element(By.ID, "editor-container-2")
        Btn.click()
        Btn.clear()
        Btn.send_keys(ingredient)
        time.sleep(2)
    except NoSuchElementException:
        print("Ingredient : No Such Element")
def Description(context,desc):
    Driver = context.driver
    try:
        Btn = Driver.find_element(By.ID, "recette_seo_recette_image_alt")
        Btn.click()
        Btn.clear()
        Btn.send_keys(desc)
        time.sleep(2)
    except NoSuchElementException:
        print("Description : No Such Element")
def Etapes(context,ing):
    Driver = context.driver
    try:
        Btn = Driver.find_element(By.ID, "editor-container-3")
        Btn.click()
        Btn.clear()
        Btn.send_keys(ing)
        time.sleep(2)
    except NoSuchElementException:
        print("Etapes : No Such Element")
def Sauvegarder(context):
    Driver = context.driver
    try:
        Btn = Driver.find_element(By.ID, "actuality_submit")
        Btn.click()
        time.sleep(2)
    except NoSuchElementException:
        print("Sauvegarder : No Such Element")


#Front

def RechercheFront(context,nom):
    Driver = context.driver
    try:
        champ = Driver.find_element(By.XPATH, '//*[@id="content-blog"]/div[1]/form/div/input')
        champ.click()
        champ.send_keys(nom)
        Btn = Driver.find_element(By.XPATH,'//*[@id="content-blog"]/div[1]/form/div/button')
        Btn.click()
        time.sleep(2)
    except NoSuchElementException:
        print("Recherche : No Such Element")

def NosRecettes(context):
    Driver = context.driver
    try:
        Btn = Driver.find_element(By.XPATH, '//*[@id="jMenu"]/li[4]')
        Btn.click()
        time.sleep(2)
    except NoSuchElementException:
        print("NosRecettes : No Such Element")

def RecettePage(context):
    Driver = context.driver
    try:
        Btn = Driver.find_element(By.XPATH, '//*[@id="content-blog"]/div[2]/div/a/div')
        Btn.click()
        time.sleep(2)
    except NoSuchElementException:
        print("RecettePage : No Such Element")

def LandAddRecette(context):
    Driver = context.driver
    Driver.maximize_window()
    Driver.get("https://cdp2020.chapeaudepaille.fr/backend.php/produits/liste-des-produits.html")
    Driver.implicitly_wait(3)
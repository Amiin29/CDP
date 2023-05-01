from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from Pages import BASE_PAGE


def NewsletterIcon(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        NewsletterIcon = Driver.find_element(By.XPATH, '//*[@id="mymodal"]/em')
        NewsletterIcon.click()
        time.sleep(3)
    except NoSuchElementException:
        print("NewsletterIcon : No Such Element")

def SaisirEmail(context,email):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        EmailChamp = Driver.find_element(By.XPATH ,'//*[@id="email"]')
        EmailChamp.clear()
        EmailChamp.send_keys(email)
        time.sleep(3)
    except NoSuchElementException:
        print("SaisirEmail : No Such Element")

def CocherCase(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        try:
            OkButoon = Driver.find_element(By.CSS_SELECTOR,'a[class="acceptCookie"]').click()
        except NoSuchElementException:
            print("okButton : No Such Element")
        except ElementNotInteractableException:
            print("okButton : element not interactable")
        checkbox = Driver.find_element(By.XPATH, '//*[@id="optin"]')
        element = Actions.move_to_element(checkbox)
        element.perform()
        checkbox.click()
        status = Driver.find_element(By.XPATH, '//*[@id="optin"]').is_selected() #False/True
        print(status)
        time.sleep(3)
    except NoSuchElementException:
        print("CocherCase : No Such Element")

def SaisirNom(context,nom):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        NomChamp = Driver.find_element(By.XPATH ,'//*[@id="lastname"]')
        NomChamp.clear()
        NomChamp.send_keys(nom)
        time.sleep(3)
    except NoSuchElementException:
        print("SaisirNom : No Such Element")

def SaisirPrenom(context,prenom):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        PrenomChamp = Driver.find_element(By.XPATH ,'//*[@id="firstname"]')
        PrenomChamp.clear()
        PrenomChamp.send_keys(prenom)
        time.sleep(3)
    except NoSuchElementException:
        print("SaisirPrenom : No Such Element")

def SaisirTelephone(context,telephone):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        TelephoneChamp = Driver.find_element(By.XPATH ,'//*[@id="phone"]')
        TelephoneChamp.clear()
        TelephoneChamp.send_keys(telephone)
        time.sleep(3)
    except NoSuchElementException:
        print("SaisirTelephone : No Such Element")


def SaisirAdresse(context,adresse):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        AdresseChamp = Driver.find_element(By.XPATH ,'//*[@id="adress"]')
        AdresseChamp.clear()
        AdresseChamp.send_keys(adresse)
        time.sleep(3)
    except NoSuchElementException:
        print("SaisirAdresse : No Such Element")

def SaisirCodePostal(context,codepostal):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        CodePostalChamp = Driver.find_element(By.XPATH ,'//*[@id="cp"]')
        CodePostalChamp.clear()
        CodePostalChamp.send_keys(codepostal)
        time.sleep(3)
    except NoSuchElementException:
        print("SaisirCodePostal : No Such Element")

def SaisirVille(context,ville):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        VilleChamp = Driver.find_element(By.XPATH ,'//*[@id="city"]')
        VilleChamp.clear()
        VilleChamp.send_keys(ville)
        time.sleep(3)
    except NoSuchElementException:
        print("SaisirVille : No Such Element")

def AbonnerButton(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        try:
            BASE_PAGE.Button_close(context)
        except NoSuchElementException:
            print("Button_close : No Such Element")
        except ElementNotInteractableException:
            print("Button_close : element not interactable")
        try:
            OkButoon = Driver.find_element(By.CSS_SELECTOR,'a[class="acceptCookie"]').click()
        except NoSuchElementException:
            print("okButton : No Such Element")
        except ElementNotInteractableException:
            print("okButton : element not interactable")

        AbonnerButton = Driver.find_element(By.XPATH ,'//*[@id="newsletter-form"]/div/button')
        element = Actions.move_to_element(AbonnerButton)
        element.perform()
        AbonnerButton.click()
        time.sleep(3)
    except NoSuchElementException:
        print("AbonnerButton : No Such Element")

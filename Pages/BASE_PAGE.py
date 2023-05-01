import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, \
    ElementClickInterceptedException
import time
from selenium.webdriver import ActionChains

import json
jsonpath = r'C:\Users\Administrator\PycharmProjects\ChapeauDePaille\Locators.json'



def LandHomePage(context):
    os.environ['PATH'] += "C:\SeleniumDriver"
    context.driver = webdriver.Chrome()
    Driver = context.driver
    Driver.maximize_window()
    Driver.get("https://pithienville.cdp2020.chapeaudepaille.fr/")
    Driver.implicitly_wait(3)

def ReturnHomePage(context):
    Driver = context.driver
    try:
        logo_Button = Driver.find_element(By.CSS_SELECTOR, 'img[class="logo-img"]')
        logo_Button.click()
        time.sleep(5)
    except NoSuchElementException:
        print("logo : No Such Element")
    except ElementClickInterceptedException:
        print("logo : element not interactable")

def landRecettePage(context):
    os.environ['PATH'] += "C:\SeleniumDriver"
    context.driver = webdriver.Chrome()
    Driver = context.driver
    Driver.maximize_window()
    Driver.get("https://pithienville.cdp2020.chapeaudepaille.fr/recettes")
    Driver.implicitly_wait(3)

def Button_close(context): #taarach alihh wakteh yatlaalek
    Driver = context.driver
    try:
        time.sleep(5)
        Button_close = Driver.find_element(By.XPATH, '//*[@id="btn-close-newsletter-modal-auto-open"]')
        Button_close.click()
    except NoSuchElementException:
        print("button close : No Such Element")
    except ElementNotInteractableException:
        print("button close : element not interactable")

def PlusTardButton(context):
    Button_close(context)
    Driver = context.driver
    try:
        PlusTardButton = Driver.find_element(By.XPATH, '//*[@id="refuse-notif-button"]/div/span')
        PlusTardButton.click()
    except NoSuchElementException:
        print("PlusTardButton : No Such Element")
    except ElementNotInteractableException:
        print("PlusTardButton : element not interactable")


def ButtonsVerification(context):
    Button_close(context)
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        Cuiellete_button = Driver.find_element(By.XPATH, '//ul[@class="centered text-s-1 jMenu"]/li[1]')
        CuilleteDropdown = Actions.move_to_element(Cuiellete_button)
        CuilleteDropdown.click().perform()
        time.sleep(2)

        Recolte_button = Driver.find_element(By.XPATH, '//ul[@class="centered text-s-1 jMenu"]/li[2]')
        RecolteDropdown = Actions.move_to_element(Recolte_button)
        Button_close(context)
        RecolteDropdown.click().perform()
        Driver.back()
        time.sleep(2)

        Culture_button = Driver.find_element(By.XPATH, '//ul[@class="centered text-s-1 jMenu"]/li[3]')
        CultureDropdown = Actions.move_to_element(Culture_button)
        Button_close(context)
        CultureDropdown.click().perform()
        time.sleep(2)

        Visite_button = Driver.find_element(By.XPATH, '//ul[@class="centered text-s-1 jMenu"]/li[4]')
        VisiteDropdown = Actions.move_to_element(Visite_button)
        Button_close(context)
        VisiteDropdown.click().perform()
        time.sleep(2)

        Ecole_button = Driver.find_element(By.XPATH, '//ul[@class="centered text-s-1 jMenu"]/li[5]')
        EcoleDropdown = Actions.move_to_element(Ecole_button)
        Button_close(context)
        EcoleDropdown.click().perform()
        time.sleep(2)

        Panier_button = Driver.find_element(By.XPATH, '//ul[@class="centered text-s-1 jMenu"]/li[6]')
        Button_close(context)
        Panier_button.click()
        Driver.switch_to.window(Driver.window_handles[0])
        time.sleep(2)

        magazin_button = Driver.find_element(By.XPATH, '//ul[@class="centered text-s-1 jMenu"]/li[7]')
        Button_close(context)
        magazin_button.click()
        Driver.back()
        time.sleep(2)

        '''recrute_button = Driver.find_element(By.CSS_SELECTOR, 'em[class="fas fa-tshirt"]').click()
        Driver.back()'''

    except NoSuchElementException:
        print("buttons : No Such Element")


def TopButtonsVerification(context):
    Button_close(context)
    Driver = context.driver
    try:
        PlusTardButton = Driver.find_element(By.XPATH, '//*[@id="refuse-notif-button"]/div/span')
        PlusTardButton.click()
    except NoSuchElementException:
        print("PlusTardButton : No Such Element")
    except ElementNotInteractableException:
        print("PlusTardButton : element not interactable")
    try:
        fb_button = Driver.find_element(By.XPATH, '//*[@id="social_media"]/a/em').click()
        Driver.switch_to.window(Driver.window_handles[0])
        time.sleep(2)

        Button_close(context)
        horaire_button = Driver.find_element(By.CSS_SELECTOR, 'em[class="fas fa-map-marked-alt"]').click()
        Driver.back()
        time.sleep(2)

        Button_close(context)
        newsletter_button = Driver.find_element(By.CSS_SELECTOR, 'em[class="fas fa-envelope"]').click()
        time.sleep(1)

        Button_close(context)
        close_btn = Driver.find_element(By.CSS_SELECTOR, 'a[class="btn-close "]').click()
        time.sleep(2)

        Button_close(context)
        calendrier_button = Driver.find_element(By.CSS_SELECTOR, 'em[class="fas fa-calendar-alt"]').click()
        Driver.back()
        time.sleep(2)
    except NoSuchElementException:
            print("Top buttons : No Such Element")


def CloseBrowser(context):
    Driver = context.driver
    Driver.quit()

def LandRecoltePage(context):
    os.environ['PATH'] += "C:\SeleniumDriver"
    context.driver = webdriver.Chrome()
    Driver = context.driver
    Driver.maximize_window()
    Driver.get("https://pithienville.cdp2020.chapeaudepaille.fr/fruits-legumes-fleurs-cueillette-pithienville-27/haricots-verts-et-haricots-grains.html")
    Driver.implicitly_wait(3)

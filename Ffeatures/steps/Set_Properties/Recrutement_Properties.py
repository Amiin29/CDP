from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time
from Pages import BASE_PAGE
from Pages.BASE_PAGE import datalist
Recrutement = datalist['Recrutement'][0]

def OffersButton(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        PlusTardButton = Driver.find_element(By.XPATH, '//*[@id="refuse-notif-button"]/div/span')
        PlusTardButton.click()
    except NoSuchElementException:
        print("PlusTardButton : No Such Element")
    except ElementNotInteractableException:
        print("PlusTardButton : element not interactable")
    try:
        OffersButton = Driver.find_element(By.CSS_SELECTOR, 'div[class="btn-recrutement green-btn"]')
        OffersButton.click()
        time.sleep(5)
    except NoSuchElementException:
        print("S1 :No Such Element")

def OfferButton(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        OfferButton = Driver.find_element(By.CSS_SELECTOR, 'div[class="large-3 medium-3 small-4 columns voir-plus"]')
        OfferButton.click()
        time.sleep(5)
    except NoSuchElementException:
        print("S2 :No Such Element")

def PostuleButton(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        PostuleButton = Driver.find_element(By.CSS_SELECTOR, 'div[class="large-12 medium-12 small-12 columns postuler"]')
        PostuleButton.click()
        time.sleep(5)
    except NoSuchElementException:
        print("S3 :No Such Element")

    
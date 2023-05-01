import time
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from Pages import BASE_PAGE

def SuivezIcon(context):
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
        SuivezIcon = Driver.find_element(By.XPATH, '//*[@id="social_media"]/a/em')
        SuivezIcon.click()
        time.sleep(5)
        Driver.switch_to.window(Driver.window_handles[0])
        time.sleep(5)
    except NoSuchElementException:
        print("SuivezIcon : No Such Element")

def FbIcon(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        FbIcon = Driver.find_element(By.XPATH, '//*[@id="footer"]/div[6]/div[1]/a/em')
        FbIcon.click()
        time.sleep(5)
        Driver.switch_to.window(Driver.window_handles[0])
        time.sleep(5)
    except NoSuchElementException:
        print("FbIcon : No Such Element")

def YtIcon(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        YtIcon = Driver.find_element(By.XPATH, '//*[@id="footer"]/div[6]/div[2]/a/em')
        YtIcon.click()
        time.sleep(5)
        Driver.switch_to.window(Driver.window_handles[0])
        time.sleep(5)
    except NoSuchElementException:
        print("YtIcon : No Such Element")
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from Pages import BASE_PAGE

def Ecole_Button(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        Ecole_Button = Driver.find_element(By.XPATH ,'//ul[@class=\"centered text-s-1 jMenu\"]/li[5]')
        EcoleDropdown = Actions.move_to_element(Ecole_Button)
        EcoleDropdown.click().perform()
        time.sleep(5)
    except NoSuchElementException:
        print("No Such Element")


def Offre_Button(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        Offre_Button = Driver.find_element(By.XPATH,'//ul[@class="centered text-s-1 jMenu"]/li[5]/ul[@class="submenu"]/li[1]')
        Ecole_Button = Driver.find_element(By.XPATH ,'//ul[@class=\"centered text-s-1 jMenu\"]/li[5]')
        EcoleDropdown = Actions.move_to_element(Ecole_Button)
        EcoleDropdown.click().perform()
        Offre_Button.click()
        time.sleep(5)
    except NoSuchElementException:
        print("No Such Element")


def Reservations_Button(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        Res_Button = Driver.find_element(By.XPATH,'//ul[@class="centered text-s-1 jMenu"]/li[5]/ul[@class="submenu"]/li[2]')
        Ecole_Button = Driver.find_element(By.XPATH ,'//ul[@class=\"centered text-s-1 jMenu\"]/li[5]')
        EcoleDropdown = Actions.move_to_element(Ecole_Button)
        EcoleDropdown.click().perform()
        Res_Button.click()
    except NoSuchElementException:
        print("No Such Element")
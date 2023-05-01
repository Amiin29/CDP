import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Pages import BASE_PAGE
from Pages.BASE_PAGE import datalist
Visite = datalist['Visite'][0]


def VisiteDropdown(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        Visite_Dropdown = Driver.find_element(By.XPATH, str(Visite['VisiteDropdown']))
        Visite_Dropdown.click()
    except NoSuchElementException:
        print("Visite_Dropdown : No Such Element")
def AccesHoraireElement(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        Acces_Horaire_Button = Driver.find_element(By.XPATH, str(Visite['AccesHoraireElement']))
        Visite_Dropdown = Driver.find_element(By.XPATH, str(Visite['VisiteDropdown']))
        VisiteDropdown = Actions.move_to_element(Visite_Dropdown)
        VisiteDropdown.click().perform()
        Acces_Horaire_Button.click()
        time.sleep(5)
    except NoSuchElementException:
        print("AccesHoraireElement : No Such Element")


def IteneraireButton(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        Iteneraire_Button = Driver.find_element(By.CSS_SELECTOR, str(Visite['IteneraireButton']))
        Iteneraire_Button.click()
        time.sleep(5)
        Driver.switch_to.window(Driver.window_handles[0])
    except NoSuchElementException:
        print("Iteneraire_Button : No Such Element")

def VisitePreparationElement(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        Visite_Preparation_Button = Driver.find_element(By.XPATH, str(Visite['VisitePreparationElement']) )
        Visite_Dropdown = Driver.find_element(By.XPATH, str(Visite['VisiteDropdown']))
        VisiteDropdown = Actions.move_to_element(Visite_Dropdown)
        VisiteDropdown.click().perform()
        Visite_Preparation_Button.click()
        time.sleep(5)
    except NoSuchElementException:
        print("Visite_Preparation_Element : No Such Element")
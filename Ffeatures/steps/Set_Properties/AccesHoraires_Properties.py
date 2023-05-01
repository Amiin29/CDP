import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Pages import BASE_PAGE

from Pages.BASE_PAGE import datalist
AccesHoraires = datalist['AccesHoraires'][0]


def AccHorIcon(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        AccHorButton = Driver.find_element(By.CSS_SELECTOR, str(AccesHoraires['AccHorIcon']))
        AccHorButton.click()
        time.sleep(3)
    except NoSuchElementException:
        print("AccHorIcon : No Such Element")


def ItButton(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        ItButton = Driver.find_element(By.CSS_SELECTOR, str(AccesHoraires['ItButton']))
        ItButton.click()
        time.sleep(3)
        Driver.switch_to.window(Driver.window_handles[0])
        time.sleep(3)
    except NoSuchElementException:
        print("ItButton : No Such Element")
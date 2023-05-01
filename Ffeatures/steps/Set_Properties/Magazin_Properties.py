import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Pages import BASE_PAGE


from Pages.BASE_PAGE import datalist
Magazin = datalist['Magazin'][0]

def Magazin_Button(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        Magazin_Button = Driver.find_element(By.ID, str(Magazin['MagazinButton']))
        Magazin_Button.click()
        time.sleep(5)
    except NoSuchElementException:
        print("Magazin_Button : No Such Element")
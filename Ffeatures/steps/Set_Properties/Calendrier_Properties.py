from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Pages import BASE_PAGE


def CalendarIcon(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        CalendarIcon = Driver.find_element(By.CSS_SELECTOR, 'a[class="calendar-products-page-link"]')
        CalendarIcon.click()
    except NoSuchElementException:
        print("CalendarIcon : No Such Element")

def YearButton(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        YearButton = Driver.find_element(By.ID, 'allmonth')
        YearButton.click()
    except NoSuchElementException:
        print("YearButton : No Such Element")

def ThisMomentButton(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        FlowerMomentButton = Driver.find_element(By.ID, 'thistime')
        FlowerMomentButton.click()
    except NoSuchElementException:
        print("ThisMomentButton : No Such Element")

def FruitButton(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        FruitButton = Driver.find_element(By.CSS_SELECTOR, 'dd[ref="frt"]')
        FruitButton.click()
    except NoSuchElementException:
        print("FruitButton : No Such Element")

def LegumeButton(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        LegumeYearButton = Driver.find_element(By.CSS_SELECTOR, 'dd[ref="lgm"]')
        LegumeYearButton.click()
    except NoSuchElementException:
        print("LegumeButton : No Such Element")

def FlowerButton(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        FlowerButton = Driver.find_element(By.CSS_SELECTOR, 'dd[ref="flowr"]')
        FlowerButton.click()
    except NoSuchElementException:
        print("FlowerButton : No Such Element")

def Recolte(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        Recolte = Driver.find_element(By.CSS_SELECTOR, 'a[title="Plantes aromatiques"]')
        Recolte.click()
    except NoSuchElementException:
        print("Recolte : No Such Element")

def AllButton(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        All = Driver.find_element(By.XPATH, '//*[@id="calendarFilterProduct"]/dd[1]/a')
        All.click()
    except NoSuchElementException:
        print("AllButton : No Such Element")
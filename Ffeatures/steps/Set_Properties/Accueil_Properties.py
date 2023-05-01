from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Pages import BASE_PAGE

from Pages.BASE_PAGE import datalist
Accueil = datalist['Accueil'][0]



def Thistime(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        Thistime = Driver.find_element(By.XPATH, str(Accueil['Thistime']))
        Thistime.click()
        Driver.back()
    except NoSuchElementException:
        print("Thistime : No Such Element")

def VoirPlus(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        VoirPlus = Driver.find_element(By.CSS_SELECTOR, str(Accueil['VoirPlus']))
        VoirPlus.click()
        Driver.back()
    except NoSuchElementException:
        print("VoirPlus : No Such Element")

def Disponible(context):
    Driver = context.driver
    try:
        fruit = Driver.find_element(By.CSS_SELECTOR, str(Accueil['fruit']))
        fruit.click()
        Driver.back()
        legume = Driver.find_element(By.CSS_SELECTOR, str(Accueil['legume']))
        legume.click()
        Driver.back()
        fleur = Driver.find_element(By.CSS_SELECTOR,str(Accueil['fleur']))
        fleur.click()
        Driver.back()
    except NoSuchElementException:
        print("Disponible : No Such Element")

def FirstElement_Slideshow(context):
    Driver = context.driver
    try:
        FirstElement = Driver.find_element(By.XPATH, '//*[@id="slider1_container"]/ol/li[1]').click()
    except NoSuchElementException:
        print("FirstElement_Slideshow : No Such Element")

def SecondElement_Slideshow(context):
    Driver = context.driver
    try:
        SecondElement = Driver.find_element(By.XPATH, '//*[@id="slider1_container"]/ol/li[2]').click()
    except NoSuchElementException:
        print("No Such Element")

def ThirdElement_Slideshow(context):
    Driver = context.driver
    try:
        Thirdelement = Driver.find_element(By.XPATH, '//*[@id="slider1_container"]/ol/li[3]').click()
    except NoSuchElementException:
        print("SecondElement_Slideshow : No Such Element")

def FourthElement_Slideshow(context):
    Driver = context.driver
    try:
        FourthElement = Driver.find_element(By.XPATH, '//*[@id="slider1_container"]/ol/li[4]').click()
    except NoSuchElementException:
        print("FourthElement_Slideshow : No Such Element")

def Decouvrir1(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        Decouvrir = Driver.find_element(By.XPATH, '//*[@id="inner-corousel"]/div[1]/div/div/div/div/div[3]/a')
        Decouvrir.click()
        Driver.back()
    except NoSuchElementException:
        print("Decouvrir1 : No Such Element")

def Decouvrir3(context):
    Driver = context.driver
    try:
        Decouvrir = Driver.find_element(By.CSS_SELECTOR, 'a[title="C’est le printemps !"]')
        Decouvrir.click()
        Driver.back()
    except NoSuchElementException:
        print("Decouvrir3 : No Such Element")


def Decouvrir4(context):
    Driver = context.driver
    try:
        Decouvrir = Driver.find_element(By.XPATH, '//*[@id="inner-corousel"]/div[4]/div/div/div/div/div[3]/a')
        Decouvrir.click()
        Driver.back()
    except NoSuchElementException:
        print("Decouvrir4 : No Such Element")

def Bloc1(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        Bloc1 = Driver.find_element(By.XPATH, '//*[@id="cartridge"]/div[1]/div/a/h2')
        element = Actions.move_to_element(Bloc1)
        element.perform()
        Bloc1.click()
        Driver.back()
    except NoSuchElementException:
        print("Bloc1 : No Such Element")
def Bloc2(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        Bloc2 = Driver.find_element(By.XPATH,  '//*[@id="cartridge"]/div[2]/div/a/h2')
        element = Actions.move_to_element(Bloc2)
        element.perform()
        Bloc2.click()
        Driver.back()
    except NoSuchElementException:
        print("Bloc2 : No Such Element")

def Bloc3(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        Bloc3 = Driver.find_element(By.XPATH, '//*[@id="u_0_2_ta"]')
        element = Actions.move_to_element(Bloc3)
        element.perform()
        Bloc3.click()
        Driver.switch_to.window(Driver.window_handles[0])
    except NoSuchElementException:
        print("Bloc3 : No Such Element")


def Bloc4(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    Actions = ActionChains(Driver)
    try:
        Bloc4 = Driver.find_element(By.XPATH, '//*[@id="cartridge"]/div[4]/div/a/h2')
        element = Actions.move_to_element(Bloc4)
        element.perform()
        Bloc4.click()
        Driver.back()
    except NoSuchElementException:
        print("Bloc4 : No Such Element")

def Actualités(context):
    Driver = context.driver
    try:
        Actualites = Driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[2]/a')
        Actualites.click()
        Driver.back()
    except NoSuchElementException:
        print("Actualités : No Such Element")

def Actualité(context):
    Driver = context.driver
    try:
        Actualite1 = Driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[1]/div[1]/a')
        Actualite1.click()
        Driver.back()
        Actualite2 = Driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[1]/div[2]/a')
        BASE_PAGE.Button_close(context)
        Actualite2.click()
        Driver.back()
    except NoSuchElementException:
        print("Actualité : No Such Element")

def Preparation(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        AccueilConseil = Driver.find_element(By.XPATH, '//*[@id="inyours"]/div[1]/div[1]')
        AccueilConseil.click()
        Circuit = Driver.find_element(By.XPATH, '//*[@id"="inyours"]/div[1]/div[2]')
        Circuit.click()
        Prix = Driver.find_element(By.XPATH, '//*[@id="inyours"]/div[1]/div[3]')
        Prix.click()
        Animaux = Driver.find_element(By.XPATH, '//*[@id="inyours"]/div[1]/div[4]')
        Animaux.click()
    except NoSuchElementException:
        print("Preparation : No Such Element")

def AccueilConseil(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        AccueilConseil = Driver.find_element(By.XPATH, '//*[@id="inyours"]/div[1]/div[1]')
        AccueilConseil.click()
        Driver.back()
    except NoSuchElementException:
        print("AccueilConseil : No Such Element")

def Circuit(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        Circuit = Driver.find_element(By.XPATH, '//*[@id="inyours"]/div[1]/div[2]')
        Circuit.click()
        Driver.back()
    except NoSuchElementException:
        print("Circuit : No Such Element")

def Prix(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        Prix = Driver.find_element(By.XPATH, '//*[@id="inyours"]/div[1]/div[3]')
        Prix.click()
        Driver.back()
    except NoSuchElementException:
        print("Prix : No Such Element")

def Animaux(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        Animaux = Driver.find_element(By.XPATH, '//*[@id="inyours"]/div[1]/div[4]')
        Animaux.click()
        Driver.back()
    except NoSuchElementException:
        print("Animaux : No Such Element")

def Location(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        Location = Driver.find_element(By.XPATH, '//*[@id="footer"]/div[1]/div/div[1]/div[2]/div[1]/div/span/a/span[1]')
        Location.click()
        Driver.switch_to.window(Driver.window_handles[0])
    except NoSuchElementException:
        print("Location : No Such Element")

def Phone(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        Phone = Driver.find_element(By.XPATH, '//*[@id="footer"]/div[1]/div/div[1]/div[2]/div[3]/p/a/span[1]')
        Phone.click()
    except NoSuchElementException:
        print("Phone : No Such Element")

def Email(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        Email = Driver.find_element(By.XPATH, '//*[@id="footer"]/div[1]/div/div[1]/div[2]/div[2]/p/span/a/span[1]')
        Email.click()
    except NoSuchElementException:
        print("Email : No Such Element")

def Fb(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        Fb = Driver.find_element(By.XPATH, '//*[@id="footer"]/div[1]/div/div[1]/div[2]/div[4]/a/p/em')
        Fb.click()
        Driver.switch_to.window(Driver.window_handles[0])
    except NoSuchElementException:
        print("Fb : No Such Element")

def Contact(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        Location = Driver.find_element(By.XPATH, '//*[@id="footer"]/div[1]/div/div[1]/div[2]/div[1]/div/span/a/span[1]')
        Location.Locationclick()
        Phone = Driver.find_element(By.XPATH, '//*[@id="footer"]/div[1]/div/div[1]/div[2]/div[3]/p/a/span[1]')
        Phone.click()
        Email = Driver.find_element(By.XPATH, '//*[@id="footer"]"/div[1]/div/div[1]/div[2]/div[2]/p/span/a/span[1]')
        Email.click()
        Fb = Driver.find_element(By.XPATH, '//*[@id="footer"]/div[1]/div/div[1]/div[2]/div[4]/a/p/em')
        Fb.click()
    except NoSuchElementException:
        print("Contact : No Such Element")

def Newsletter(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        Newsletter = Driver.find_element(By.XPATH, '//*[@id="email-newsletter-subscription-footer-1"]')
        Newsletter.send_keys("yesmine.arous4@gmail.com")
        Abonner = Driver.find_element(By.XPATH, '//*[@id="newsletter-form-footer-1"]/div/button')
        Abonner.click()
    except NoSuchElementException:
        print("Newsletter : No Such Element")

def Others(context):
    BASE_PAGE.Button_close(context)
    Driver = context.driver
    try:
        url = Driver.find_element(By.XPATH, '//*[@id="footer"]/div[2]/div[1]/a')
        url.click()
        legal = Driver.find_element(By.XPATH, '//*[@id="footer"]/div[2]/div[2]/a')
        legal.click()
    except NoSuchElementException:
        print("Others : No Such Element")

def MangerBouger(context):
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
        url = Driver.find_element(By.XPATH, '//*[@id="footer"]/div[2]/div[1]/a')
        urlclick = Actions.move_to_element(url)
        urlclick.click().perform()
        url.click()
        Driver.back()
    except NoSuchElementException:
        print("MangerBouger : No Such Element")

def MentionsLegales(context):
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
        Mlegal = Driver.find_element(By.XPATH, '//*[@id="footer"]/div[2]/div[2]/a')
        element = Actions.move_to_element(Mlegal)
        element.perform()
        Mlegal.click()
    except NoSuchElementException:
        print("MentionsLegales : No Such Element")
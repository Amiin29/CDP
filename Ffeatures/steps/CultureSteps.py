from selenium import webdriver
from behave import *
from Ffeatures.steps.Set_Properties import Culture_Properties
from Pages import BASE_PAGE

class Culture(webdriver.Chrome):
    @when(u'Cliquer sur le dropdown "Nos pratiques de culture"')
    def NosPratiquesDeCulture(context):
        Culture_Properties.Dropdown(context)

    @when(u'Cliquer sur le bouton "Agri respect"')
    def AgriRespect(context):
        Culture_Properties.Dropdown_element1(context)
        BASE_PAGE.TopButtonsVerification(context)
        BASE_PAGE.ButtonsVerification(context)

    @when(u'Cliquer sur le bouton "le désherbage, un binage vaut deux arrosages"')
    def Désherbage(context):
        Culture_Properties.Dropdown_element2(context)
        BASE_PAGE.Button_close(context)
        BASE_PAGE.TopButtonsVerification(context)
        BASE_PAGE.ButtonsVerification(context)
    @when(u'Cliquer sur le bouton "Cultiver sous abri"')
    def CultiverSousAbri(context):
        Culture_Properties.Dropdown_element3(context)
        BASE_PAGE.Button_close(context)
        BASE_PAGE.TopButtonsVerification(context)
        BASE_PAGE.ButtonsVerification(context)

    @when(u'Cliquer sur le bouton "Il y a mieux que les pestivides en agriculture !"')
    def Agriculture(context):
        Culture_Properties.Dropdown_element4(context)
        BASE_PAGE.Button_close(context)
        BASE_PAGE.TopButtonsVerification(context)
        BASE_PAGE.ButtonsVerification(context)

    @when(u'Cliquer sur le bouton "Notre lutte contre le gaspillage"')
    def Gaspillage(context):
        Culture_Properties.Dropdown_element5(context)
        BASE_PAGE.Button_close(context)
        BASE_PAGE.TopButtonsVerification(context)
        BASE_PAGE.ButtonsVerification(context)

    @then(u'La page contenant la pratique de culture "Notre lutte contre le gaspillage" est affichée')
    def End(context):
        BASE_PAGE.CloseBrowser(context)


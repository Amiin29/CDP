from selenium import webdriver
from behave import *
from Pages import BASE_PAGE
from Ffeatures.steps.Set_Properties import Magazin_Properties

class Magazin(webdriver.Chrome):
    @when(u'Cliquer sur le bouton "Le magazin"')
    def MagazinBouton(context):
        Magazin_Properties.Magazin_Button(context)
        BASE_PAGE.TopButtonsVerification(context)
        BASE_PAGE.ButtonsVerification(context)

    @then(u'Une page contenant les détails du magazin est affichée')
    def End(context):
        BASE_PAGE.CloseBrowser(context)


from selenium import webdriver
from behave import *
from Pages import BASE_PAGE
from Ffeatures.steps.Set_Properties import Ecole_Properties

from Pages.BASE_PAGE import datalist
Ecole = datalist['Ecole'][0]

class Ecole(webdriver.Chrome):
    @given(u'La page accueil est ouverte')
    def Start(context):
        BASE_PAGE.LandHomePage(context)

        

    @when(u'Cliquer sur le Dropdown "Ecole"')
    def EcoleDrpodown(context):
        Ecole_Properties.Ecole_Button(context)

    @when(u'Cliquer sur le bouton "Notre offre"')
    def Offre(context):
        Ecole_Properties.Offre_Button(context)
        BASE_PAGE.TopButtonsVerification(context)
        BASE_PAGE.ButtonsVerification(context)
        BASE_PAGE.ReturnHomePage(context)

    @when(u'Cliquer sur le bouton "Réservations"')
    def Reservations(context):
        Ecole_Properties.Ecole_Button(context)
        Ecole_Properties.Reservations_Button(context)
        BASE_PAGE.TopButtonsVerification(context)
        BASE_PAGE.ButtonsVerification(context)

    @then(u'La page contenant les réservations est affichée')
    def End(context):
        BASE_PAGE.CloseBrowser(context)



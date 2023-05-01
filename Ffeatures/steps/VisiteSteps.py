from selenium import webdriver
from behave import *
from Pages import BASE_PAGE
from Ffeatures.steps.Set_Properties import Visite_Properties

from Pages.BASE_PAGE import datalist
Visite = datalist['Visite'][0]



class Visite(webdriver.Chrome):

    @given(u'que La page d\'accueil est ouverte')
    def Start(context):
        BASE_PAGE.LandHomePage(context)

    @when(u'Cliquer sur le Dropdown "Votre visite"')
    def VotreVisite(context):
        Visite_Properties.VisiteDropdown(context)

    @when(u'Cliquer sur "AccésHoraires"')
    def AccesHoraires(context):
        Visite_Properties.AccesHoraireElement(context)
        BASE_PAGE.TopButtonsVerification(context)
        BASE_PAGE.ButtonsVerification(context)


    @when(u'Cliquer sur "Itinéraire"')
    def Itineraire(context):
        Visite_Properties.IteneraireButton(context)
        BASE_PAGE.ReturnHomePage(context)


    @when(u'Cliquer sur "Préparer votre visite"')
    def PreparerVotreVisite(context):
        Visite_Properties.VisitePreparationElement(context)
        BASE_PAGE.TopButtonsVerification(context)
        BASE_PAGE.ButtonsVerification(context)

    @then(u'La page contenant les détails sur la préparation d\'une visite est affichée')
    def End(context):
        BASE_PAGE.CloseBrowser(context)


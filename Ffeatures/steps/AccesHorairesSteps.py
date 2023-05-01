from selenium import webdriver
from behave import *
from Pages import BASE_PAGE
from Ffeatures.steps.Set_Properties import AccesHoraires_Properties
class AccesHoraires(webdriver.Chrome):

    @given(u'La page d\'accueil est ouverte')
    def Start(context):
        BASE_PAGE.LandHomePage(context)

    @when(u'Cliquer sur l\'icone "Accès&Horaires"')
    def AccHor(context):
        AccesHoraires_Properties.AccHorIcon(context)

    @when(u'Cliquer sur le bouton Itinéraire')
    def Itineraire(context):
        AccesHoraires_Properties.ItButton(context)

    @then(u'La page contenant les horaires et la localisation est affichée')
    def End(context):
        BASE_PAGE.CloseBrowser(context)
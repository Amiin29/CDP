from selenium import webdriver
from behave import *
from Pages import BASE_PAGE
from Ffeatures.steps.Set_Properties import Recrutement_Properties



class Recrutement(webdriver.Chrome):
    @given(u'que La page  d\'accueil est ouverte')
    def Start(context):
        BASE_PAGE.LandHomePage(context)

    @when(u'Cliquer sur le bouton "Voir les offres"')
    def Offres(context):
        Recrutement_Properties.OffersButton(context)
        BASE_PAGE.TopButtonsVerification(context)
        BASE_PAGE.ButtonsVerification(context)
    @when(u'Cliquer sur le bouton "Voir offre"')
    def Offre(context):
        Recrutement_Properties.OfferButton(context)
        BASE_PAGE.TopButtonsVerification(context)
        BASE_PAGE.ButtonsVerification(context)
    @when(u'Cliquer ur le button "Postuler"')
    def Postule(context):
        Recrutement_Properties.PostuleButton(context)

    @then(u'La page contenant les détails de l\'offre est affichée')
    def End(context):
        BASE_PAGE.CloseBrowser(context)

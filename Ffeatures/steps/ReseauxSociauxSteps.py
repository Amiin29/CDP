from selenium import webdriver
from behave import *
from Ffeatures.steps.Set_Properties import ReseauxSociaux_Properties
from Pages import BASE_PAGE

class ReseauSociaux(webdriver.Chrome):
    @when(u'Cliquer sur l\'icone "Suivez-nous"')
    def IconeSuivezNous(context):
        ReseauxSociaux_Properties.SuivezIcon(context)
    @then(u'Une page d\'un réseau social s\'ouvre')
    def End1(context):
        BASE_PAGE.CloseBrowser(context)

    @when(u'Cliquer sur l\'icone de Facebook')
    def IconeFacebook(context):
        ReseauxSociaux_Properties.FbIcon(context)

    @then(u'Une page Facebook s\'affiche')
    def End2(context):
        BASE_PAGE.CloseBrowser(context)

    @when(u'Cliquer sur l\'icone de Youtube')
    def IconeYoutube(context):
        ReseauxSociaux_Properties.YtIcon(context)

    @then(u'Une page de la chaine Youtube s\'affiche')
    def End3(context):
        BASE_PAGE.CloseBrowser(context)


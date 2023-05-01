from behave import *
from selenium import webdriver
from Pages import BASE_PAGE
from Ffeatures.steps.Set_Properties import Actualités_Properties
class Actualités(webdriver.Chrome):
    @given(u'La page de tous les actualités est ouverte')
    def Start(context):
        Actualités_Properties.StartPage(context)
    @when(u'Afficher seulement les évènements')
    def Evenements(context):
        Actualités_Properties.Events(context)

    @when(u'Faire la recherche')
    def Recherche(context):
        Actualités_Properties.Recherche(context,"345")
        Actualités_Properties.Recherche(context,"BH")
        Actualités_Properties.Recherche(context," ")
        Actualités_Properties.Recherche(context,"pomme")
        Actualités_Properties.Recherche(context,"Brouette")
    @when(u'Choisir une actualité')
    def Actualité(context):
        Actualités_Properties.Actualité(context)

    @when(u'Afficher autre actualité')
    def AutreActualité(context):
        Actualités_Properties.OtherActualité(context)

    @then(u'Une page contenant la description d\'une actualité est affichée')
    def End(context):
        BASE_PAGE.CloseBrowser(context)


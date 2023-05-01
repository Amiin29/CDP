import time

from selenium import webdriver
from behave import *
from Pages import  BASE_PAGE
from Set_Properties import Recoltes_Properties
class Recoltes(webdriver.Chrome):
    @when(u'Cliquer sur le bouton "Les récoltes" dans la bar de navigation')
    def Recotes(context):
        Recoltes_Properties.Dropdown(context)
    @when(u'Revenir à la page d\'accueil')
    def Accueil(context):
        time.sleep(3)
        BASE_PAGE.ReturnHomePage(context)

    @when(u'Cliquer sur le bouton "En ce moment"')
    def EnCeMoment(context):
        Recoltes_Properties.Dropdown_element1(context)


    @when(u'Cliquer sur le nom de la recette du moment')
    def Recette(context):
        Recoltes_Properties.Recette(context)

    @when(u'Cliquer sur Framboises')
    def Fruit(context):
        Recoltes_Properties.fruit(context)

    @when(u'Cliquer sur Betteraves rouges')
    def Legume(context):
        Recoltes_Properties.legume(context)

    @when(u'Cliquer sur Fleurs à sécher : les immortelles et les statices')
    def Fleur(context):
        Recoltes_Properties.fleur(context)


    @when(u'Cliquer sur le bouton "Calendrier"')
    def Calendrier(context):
        Recoltes_Properties.Dropdown_element2(context)
        BASE_PAGE.ReturnHomePage(context)

    @when(u'Cliquer sur le bouton "Des fruits, des légumes, des fleurs"')
    def RecolteDesc(context):
        Recoltes_Properties.Dropdown_element3(context)

    @when(u'Cliquer sur "Suivant"')
    def Suivant(context):
        Driver = context.driver
        Recoltes_Properties.Suivant(context)
        Recoltes_Properties.Suivant(context)
        Recoltes_Properties.Suivant(context)
        Recoltes_Properties.Suivant(context)
        Recoltes_Properties.Suivant(context)
        Recoltes_Properties.Suivant(context)
        Recoltes_Properties.Suivant(context)
        Recoltes_Properties.Suivant(context)
        Recoltes_Properties.Suivant(context)
        Recoltes_Properties.Suivant(context)
        Recoltes_Properties.Suivant(context)

    @then(u'Une page contenant une description d\'une récoltee est affichée')

    @given(u'La page contenant une description d\'une récolte est ouverte')
    def Start(context):
        BASE_PAGE.LandRecoltePage(context)
    @when(u'Cliquer sur "Précédent"')
    def Precedant(context):
        Recoltes_Properties.Precedant(context)

    @when(u'Cliquer sur "Tout"')
    def Tout(context):
        Recoltes_Properties.Tout(context)

    @then(u'Une page contenant une description d\'une récolte est affichée')
    def End(context):
        BASE_PAGE.CloseBrowser(context)



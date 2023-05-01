from selenium import webdriver
from behave import *
from Pages import BASE_PAGE
from Ffeatures.steps.Set_Properties import Apropos_Properties
class Apropos(webdriver.Chrome):
    @when(u'Cliquer sur le Dropdown "La cuiellette"')
    def Start(context):
        Apropos_Properties.Dropdown(context)
    @when(u'Cliquer "Qui sommes-nous ?"')
    def QuiSommesNous(context):
        Apropos_Properties.Dropdown_element1(context)
        BASE_PAGE.TopButtonsVerification(context)
        BASE_PAGE.ButtonsVerification(context)
    @when(u'Cliquer sur "Cueillez la fraicheur"')
    def CuillezFraicheur(context):
        Apropos_Properties.Dropdown_element2(context)
        BASE_PAGE.TopButtonsVerification(context)
        BASE_PAGE.ButtonsVerification(context)

    @when(u'Cliquer sur "Notre charte"')
    def NotreCharte(context):
        Apropos_Properties.Dropdown_element3(context)
        BASE_PAGE.TopButtonsVerification(context)
        BASE_PAGE.ButtonsVerification(context)

    @when(u'Afficher les images')
    def Images(context):
        Apropos_Properties.Images(context)
        BASE_PAGE.ReturnHomePage(context)

    @when(u'Cliquer sur "Chapeau de Paille"')
    def ChapeauDePaille(context):
        Apropos_Properties.Dropdown_element4(context)
        BASE_PAGE.TopButtonsVerification(context)
        BASE_PAGE.ButtonsVerification(context)

    @when(u'Cliquer sur "Actualités"')
    def Actualités(context):
        Apropos_Properties.Dropdown_element5(context)
        BASE_PAGE.TopButtonsVerification(context)
        BASE_PAGE.ButtonsVerification(context)


    @then(u'Une page contenant tous les actualités est affichée')
    def End(context):
        BASE_PAGE.CloseBrowser(context)


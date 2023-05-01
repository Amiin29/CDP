import time

from behave import *
from selenium import webdriver
from Pages import BASE_PAGE
from Ffeatures.steps.Set_Properties import Accueil_Properties

class Accueil(webdriver.Chrome):

    @when('Vérifier les 4 boutons de la première barre de navigation')
    def QuatreBoutons(context):
        BASE_PAGE.TopButtonsVerification(context)

    @when('Vérifier les boutons et les dropdowns de la deuxième barre de navigation')
    def BarreNavigations(context):
        BASE_PAGE.ButtonsVerification(context)

    @when('Cliquer sur "En ce moment dans la cuillette"')
    def CeMoment(context):
        Accueil_Properties.Thistime(context)

    @when('Cliquer sur "Voir plus"')
    def VoirPlus(context):
        Accueil_Properties.VoirPlus(context)

    @when('Afficher ce qui est disponible dans la cueillette en ce moment')
    def DispoCeMoment(context):
        Accueil_Properties.Disponible(context)

    @when('Naviguer entre les éléments du slideshow')
    def Slideshows(context):
        Accueil_Properties.FirstElement_Slideshow(context)
        Accueil_Properties.SecondElement_Slideshow(context)
        Accueil_Properties.ThirdElement_Slideshow(context)
        Accueil_Properties.FourthElement_Slideshow(context)

    @when('Afficher le premier élément du slideshow')
    def PrSlideshow(context):
        Accueil_Properties.Decouvrir1(context)

    @when('Afficher le deuxième élément du slideshow')
    def DxSlideshow(context):
        Accueil_Properties.SecondElement_Slideshow(context)

    @when('Afficher le troisième élément du slideshow')
    def TrSlideshow(context):
        Accueil_Properties.ThirdElement_Slideshow(context)
        Accueil_Properties.Decouvrir3(context)

    @when('Afficher le quatrième élément du slideshow')
    def QtSlideshow(context):
        Accueil_Properties.FourthElement_Slideshow(context)
        Accueil_Properties.Decouvrir4(context)

    @when('Afficher le premier bloc " Qui sommes-nous  "')
    def PrBloc(context):
        Accueil_Properties.Bloc1(context)

    @when('Afficher le deuxième bloc " Calendrier & Récoltes "')
    def DxBloc(context):
        Accueil_Properties.Bloc2(context)

    @when('Afficher le troisième bloc')
    def TrBloc(context):
        Accueil_Properties.Bloc3(context)
    @when('Afficher le quatrième bloc')
    def QtBloc(context):
        Accueil_Properties.Bloc4(context)

    @when('Afficher Tous les actualités')
    def TousActualités(context):
        Accueil_Properties.Actualités(context)

    @when('Afficher une actualité')
    def Actualité(context):
        Accueil_Properties.Actualité(context)
        BASE_PAGE.ReturnHomePage(context)

    @when('Afficher "Accueil et conseil"')
    def AccueilConseil(context):
        Accueil_Properties.AccueilConseil(context)
        BASE_PAGE.ReturnHomePage(context)

    @when('Afficher "Animaux de la ferme"')
    def AnimauxFerme(context):
        Accueil_Properties.Animaux(context)
        BASE_PAGE.ReturnHomePage(context)

    @when('Afficher "Circuit rapide"')
    def CircuitRapide(context):
        Accueil_Properties.Circuit(context)
        BASE_PAGE.ReturnHomePage(context)

    @when('Afficher "Prix dégressifs"')
    def PrixDegressifs(context):
        Accueil_Properties.Prix(context)
        BASE_PAGE.ReturnHomePage(context)

    @when('Afficher la localisation')
    def Localisation(context):
        Accueil_Properties.Location(context)


    @when('Cliquer sur le numéro de téléphone')
    def Telephone(context):
        print("Une alerte s'affiche")

    @when('Cliquer sur l\'icone Facebook')
    def Facebook(context):
        Accueil_Properties.Fb(context)

    @when('Cliquer sur l\'adresse email')
    def Email(context):
        Accueil_Properties.Email(context)

    @when('Afficher les partenaires')
    def Partenaires(context):
        print("Des photos, y'a rien à afficher !")
    @when('S\'abonner à la newsletter avec un email déjà existé')
    def Newsletter(context):
        Accueil_Properties.Newsletter(context)
    @when('Ouvrir le site web "MangerBouger"')
    def MangerBouger(context):
        Accueil_Properties.MangerBouger(context)
    @when('Afficher les mentions légales')
    def MentionsLegales(context):
        Accueil_Properties.MentionsLegales(context)
    @then('La page des " Mentions légales " est affichée')
    def End(context):
        BASE_PAGE.CloseBrowser(context)


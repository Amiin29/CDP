from behave import *
from selenium import webdriver
import time
from Pages import BASE_PAGE
from Set_Properties import Newsletter_Properties

class Newsletter(webdriver.Chrome):
    @when(u'Cliquer sur le button de Newsletter')
    def NewsletterButton(context):
        Newsletter_Properties.NewsletterIcon(context)

    @when(u'Cocher la case pour accepter et recevoir les newsletter')
    def CocherCase(context):
        Newsletter_Properties.CocherCase(context)

    @when(u'Cliquer sur le button "Je m\'abonne"')
    def Abonner(context):
        Newsletter_Properties.AbonnerButton(context)

    @when(u'Saisir un email non valide')
    def EmailNonValide(context):
        Newsletter_Properties.SaisirEmail(context,email="yesmine.arous4@gamil.com")
        Newsletter_Properties.CocherCase(context)

    @then(u'Un message s\'affiche en indiquant que l\'inscription est échouée et que je dois vérifier le champ de l\'email')

    @when(u'Cocher la case pour accepter et recevoir les newsletter et s\'abonner')
    def CocherCase(context):
        Newsletter_Properties.CocherCase(context)
        Newsletter_Properties.AbonnerButton(context)
    @when(u'Saisir un email valide')
    def EmailNonValide(context):
        Newsletter_Properties.SaisirEmail(context, email="yesmine.arous4@gmail.com")
        Newsletter_Properties.CocherCase(context)
    @when(u'Saisir des chiffres dans le Prénom')
    def PrenomNonValide(context):
        Newsletter_Properties.SaisirPrenom(context, prenom="4354")
        Newsletter_Properties.CocherCase(context)
    @when(u'Saisir des chiffres dans le Nom')
    def NomNonValide(context):
        Newsletter_Properties.SaisirNom(context, nom="4354")
        Newsletter_Properties.CocherCase(context)


    @when(u'Saisir des chiffres dans Ville')
    def VilleNonValide(context):
        Newsletter_Properties.SaisirVille(context,ville="5667")
        Newsletter_Properties.CocherCase(context)
    @when(u'Saisir un numéro de Telephone non valide')
    def NumTelNonValide(context):
        Newsletter_Properties.SaisirTelephone(context, "34567786")
        Newsletter_Properties.CocherCase(context)
    @when(u'Saisir un Nom valide')
    def NomValide(context):
        Newsletter_Properties.SaisirNom(context,nom="Arous")
    @when(u'Saisir un Prenom valide')
    def PrenomValide(context):
        Newsletter_Properties.SaisirPrenom(context, prenom="Yesmine")

    @when(u'Saisir un numéro de téléphone valide')
    def NumTelValide(context):
        Newsletter_Properties.SaisirTelephone(context,telephone="0232343759")
    @when(u'Saisir un Email déjà utilisé et valide')
    def Email(context):
        Newsletter_Properties.SaisirEmail(context, email="yesmine.arous4@gmail.com")
    @when(u'Saisir une Adresse valide')
    def AdresseValide(context):
        Newsletter_Properties.SaisirAdresse(context, adresse="Route de Pithienville")
    @when(u'Saisir un code postal valide')
    def CodePostalValide(context):
        Newsletter_Properties.SaisirCodePostal(context, codepostal="27180")
    @when(u'Saisir une Ville valide')
    def VileValide(context):
        Newsletter_Properties.SaisirVille(context, "Pithienville")
        Newsletter_Properties.CocherCase(context)
    @when(u'Décocher la case pour accepter et recevoir les newsletter')
    def Decocher(context):
        Newsletter_Properties.CocherCase(context)
    @then(u'Un message s\'affiche en indiquant que l\'inscription est échouée et je dois cocher la case pour accepter et recevoir les newsletter')
    def End(context):
        BASE_PAGE.CloseBrowser(context)


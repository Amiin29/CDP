from selenium import webdriver
from behave import *
from Pages import BASE_PAGE,BACKEND
from Bfeatures.steps.Set_Properties import Recettes_Properties
class Recettes(webdriver.Chrome):
    @given(u'La page de la liste des recettes dans le backend est ouverte')
    def StartPage(context):
        BACKEND.LandRecettesPage(context)
        BACKEND.Security(context)
        BACKEND.Login(context)
        BACKEND.Pithienville(context)
    @when(u'Cliquer sur le bouton switch de "Activer le module recette dans le menu "')
    def Module(context):
        Recettes_Properties.ActiverModule(context)

    @then(u'Le module est activé')
    def End(context):
        BASE_PAGE.CloseBrowser(context)

    @given(u'La page d\'accueil est ouverte')
    def Start(context):
        BASE_PAGE.LandHomePage(context)
    @when(u'Cliquer sur le bouton " Nos recettes "')
    def step_impl(context):
        Recettes_Properties.NosRecettes(context)

    @then(u'La page de la liste des recettes est affichée')
    def End(context):
        BASE_PAGE.CloseBrowser(context)

    @given(u'La page de la liste des recette dans le backend est ouverte')
    def Start(context):
        BACKEND.LandRecettesPage(context)
        BACKEND.Security(context)
        BACKEND.Login(context)
        BACKEND.Pithienville(context)
    @when(u'Cliquer sur le bouton switch de "Activer les recettes sur la page d\'accueil "')
    def ActiverRecette(context):
        Recettes_Properties.ActiverRecette(context)

    @then(u'la recette est activée')
    def End(context):
        BASE_PAGE.CloseBrowser(context)
    @when(u'Cliquer sur le bouton " Voir tous "')
    def VoirTous(context):
        Recettes_Properties.VoirTous(context)
    @given(u'La page de la liste de toutes les recettes dans le backend est ouverte')
    def Start(context):
        BACKEND.LandRecettesPage(context)
        BACKEND.Security(context)
        BACKEND.Login(context)
        BACKEND.Pithienville(context)


    @when(u'Cliquer sur le bouton "Non Publiées"')
    def NPublished(context):
        Recettes_Properties.NPubliées(context)

    @when(u'Ouvrir la page d\'accueil de site web')
    def HomePage(context):
        BASE_PAGE.LandHomePage(context)

    @when(u'Cliquer sur le bouton "Nos recettes " dans le menu')
    def NosRecettes(context):
        Recettes_Properties.NosRecettes(context)
    @then(u'La meme liste des recettes affichée dans le backend est affichée')
    def End(context):
        BASE_PAGE.CloseBrowser(context)

    @when(u'Cliquer sur le bouton "Publiées"')
    def Published(context):
        Recettes_Properties.Publiées(context)

    @given(u'La page de la liste des recette dans le backend est ouvertee')
    def Add(context):
        Recettes_Properties.LandAddRecette(context)
        BACKEND.Security(context)
        BACKEND.Login(context)
        BACKEND.Pithienville(context)

    @when(u'Cliquer sur le bouton "Ajouter une recette')
    @when(u'Saisir le titre')
    def Titre(context):
        Recettes_Properties.Titre(context,"test")
    @when(u'Saisir le résumé')
    def Resume(context):
        Recettes_Properties.Resume(context,"testttttt")
    @when(u'Saisir la liste des Ingrédients')
    def Ingredients(context):
        Recettes_Properties.Ingredient(context,"testtt")
    @when(u'Saisir la Liste des étapes')
    def Etapes(context):
        Recettes_Properties.Etapes(context,"testtttt")
    @then(u'La liste des recettes avec la nouvelle recette est affichée')
    def End(context):
        BASE_PAGE.CloseBrowser(context)

    @then(u'Un message d\'erreur indiquant que le champ de résumé est obligatoire')
    def End(context):
        BASE_PAGE.CloseBrowser(context)

    @given(u'La page de la liste des recettes publiées dans le backend est ouverte')
    def Start(context):
        BACKEND.LandRecettesPage(context)
        BACKEND.Security(context)
        BACKEND.Login(context)
        BACKEND.Pithienville(context)
    @when(u'Rechercher une recette')
    def Recherche(context):
        Recettes_Properties.Recherche(context,"test")
    @when(u'Effacer quelque caractères')
    def Effacer(context):
        Recettes_Properties.Resume(context,"tes")

    @when(u'Rechercher la recette')
    def Recherche(context):
        Recettes_Properties.Recherche(context,"test")
    @then(u'Pas de résultat')
    def End(context):
        BASE_PAGE.CloseBrowser(context)


    @given(u'La page de la liste des recettes non publiées dans le backend est ouverte')
    def Start(context):
        BACKEND.LandRecettesPage(context)
        BACKEND.Security(context)
        BACKEND.Login(context)
        BACKEND.Pithienville(context)
    @when(u'Cliquer sur le switch')
    def Switch(context):
        Recettes_Properties.Publier(context)
    @when(u'Cliquer sur le bouton "Nos recettes" dans le menu')
    def NosRecettes(context):
        Recettes_Properties.NosRecettes(context)
    @when(u'Rechercher la recette publiée')
    def Recherche(context):
        Recettes_Properties.RechercheFront(context,"test")
    @then(u'Seulement la recette est affichée dans la liste')
    def End(context):
        BASE_PAGE.CloseBrowser(context)

    @given(u'La page d\'accueil de site web est ouverte')
    def HomePage(context):
        BASE_PAGE.LandHomePage(context)

    @when(u'Rechercher la recette publiée dans le site')
    def Rechercher(context):
        Recettes_Properties.RechercheFront(context,"test")

    @when(u'Afficher la recette')
    def Recette(context):
        Recettes_Properties.RecettePage(context)
    @then(u'La page de la recette avec les modifications dans le résumé est affichée')
    def End(context):
        BASE_PAGE.CloseBrowser(context)

    @when(u'Saisir le nom de la recette dans le champ de recherche')
    def Nom(context):
        Recettes_Properties.Recherche(context,"test")
    @when(u'Rechercher la recettes')
    @then(u'Aucune recette est affichée')
    def End(context):
        BASE_PAGE.CloseBrowser(context)

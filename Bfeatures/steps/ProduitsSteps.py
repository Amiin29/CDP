from selenium import webdriver
from behave import *
from Pages import BACKEND
from Bfeatures.steps.Set_Properties import Produits_Properties
class Prouduits(webdriver.Chrome):
    @given(u'La page de la liste des produits est ouverte')
    def PageProduits(context):
        BACKEND.LandProductsPage(context)
        BACKEND.Security(context)
        BACKEND.Login(context)
        BACKEND.Pithienville(context)

    @when(u'Cliquer sur "Ajouter un produit"')
    def Ajout(context):
        Produits_Properties.Ajout(context)
    @when(u'Saisir le titre de produit')
    def Titre(context):
        Produits_Properties.Titre(context, Titre="test")

    @when(u'Choisir une catégorie')
    def Catégorie(context):
        Produits_Properties.Categories(context,"fruit")

    @when(u'Saisir la description d\'image')
    def DescriptionImage(context):
        Produits_Properties.DescImages(context,desc="Description test")

    @when(u'Saisir l\'historique')
    def Historique(context):
        Produits_Properties.Historique(context,"testtttttt")

    @when(u'Saisir les propriétés')
    def Proprietes(context):
        Produits_Properties.Prop(context,"testst")

    @when(u'Cliquer sur Sauvegarder')
    def Sauvegarde(context):
        Produits_Properties.Sauvegarder(context)

    @then(u'Un message d\'erreur s\'affiche indiquant que le champ "Astuces/Conservation/Dégustation" est obligatoire')
    def End(context):
        BACKEND.Close(context)

    @when(u'Saisir les astuces')
    def Astuces(context):
        Produits_Properties.Astuces(context,"tttttt")

    @then(u'Le produit est ajouté à la liste des produits')
    def EndS2(context):
        BACKEND.Close(context)

    @when(u'Saisir le nom d\'un produit dans le recherche')
    def Recherche(context):
        Produits_Properties.Recherche(context,"test")

    @then(u'Seulement le produit souhaité est affiché est les autres produits sont masqués')
    def EndS3(context):
        BACKEND.Close(context)

    @when(u'Rechercher le produit à modifier')
    def Rechercher(context):
        Produits_Properties.Recherche(context,"test")

    @when(u'Cliquer sur le bouton de modification')
    def Modification(context):
        Produits_Properties.Modification(context)

    @when(u'Supprimer quelque caractères de nom')
    def NouveauTitre(context):
        Produits_Properties.Titre(context,"te")

    @when(u'Ouvrir la page de tous les récoltes dans le siteweb de la cueillette de Pithienville')
    def CalendrierPage(context):
        BACKEND.CalendrierRecoltePage(context)
    @when(u'Cliquer sur le nom de produit modifié')
    def NomProduit(context):
        print("")
    @then(u'Une page contenant une descrption de produit s\'affiche avec un nom modifié')
    def EndS4(context):
        BACKEND.Close(context)

    @when(u'Rechercher le produit à surpprimer')
    def Recherche(context):
        Produits_Properties.Recherche(context)
    @when(u'Cliquer sur le bouton de suppression')
    def Suppression(context):
        Produits_Properties.Suppression(context)
    @when(u'Confirmer la suppression')
    def Confirmer(context):
        Produits_Properties.AlerteOui(context)

    @then(u'Le produit est supprimé de la liste des produits')
    def EndS5(context):
        BACKEND.Close(context)


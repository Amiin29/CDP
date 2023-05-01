from behave import *
from selenium import webdriver
from Ffeatures.steps.Set_Properties import Calendrier_Properties
from Pages import BASE_PAGE
class Calendrier(webdriver.Chrome):
    @when(u'Cliquer sur le button "Calendrier dse récoltes"')
    def CalendrierDesRecoltes(context):
        Calendrier_Properties.CalendarIcon(context)

    @when(u'Cliquer sur le button "Année entière"')
    def AnneeEntiere(context):
        Calendrier_Properties.YearButton(context)

    @when(u'Cliquer sur "Fruit"')
    def Fruits(context):
        Calendrier_Properties.FruitButton(context)

    @when(u'Cliquer sur "En ce moment"')
    def EnCeMoment(context):
        Calendrier_Properties.ThisMomentButton(context)

    @when(u'Cliquer sur "Légumes"')
    def Legumes(context):
        Calendrier_Properties.LegumeButton(context)

    @when(u'Cliquer sur "Année entière"')
    def AnneeEntiere(context):
        Calendrier_Properties.YearButton(context)

    @when(u'Cliquer sur "Fleurs"')
    def Fleurs(context):
        Calendrier_Properties.FlowerButton(context)

    @when(u'Cliquer sur "Tous"')
    def Tous(context):
        Calendrier_Properties.AllButton(context)

    @when(u'Cliquer sur Plantes aromatiques')
    def PlantesAo(context):
        Calendrier_Properties.Recolte(context)
        
    @then(u'Une page de la description de Plantes aromatiques est affichée')
    def DescPlantesAro(context):
        BASE_PAGE.Button_close(context)




'''@when(u'Cliquer sur Poireaux')
    def Poireaux(context):
        Calendrier_Properties.Recolte(context,'//*[@id="product-wrap"]/div/div[14]/div[1]/a')

    @then(u'Une page de la description de Poireaux est affichée')
    def DescPoireaux(context):
        print("Une page de la description de Poireaux est affichée")

    @when(u'Cliquer sur Pommes de terre')
    def PommeDeTerre(context):
        Calendrier_Properties.Recolte(context,'//*[@id="product-wrap"]/div/div[16]/div[1]/a')

    @then(u'Une page de la description de Pommes de terre est affichée')
    def DesPommeDeTerre(context):
        print("")

    @when(u'Cliquer sur Radis')
    def Radis(context):
        Calendrier_Properties.Recolte(context,'//*[@id="product-wrap"]/div/div[17]/div[1]/a')

    @then(u'Une page de la description de Radis est affichée')
    def DescRadis(context):
        print("Une page de la description de Pommes de terre est affichée")

    @when(u'Cliquer sur Salades')
    def Salades(context):
        Calendrier_Properties.Recolte(context,'//*[@id="product-wrap"]/div/div[18]/div[1]/a')

    @then(u'Une page de la description de Salades est affichée')
    def DescSalades(context):
        print("Une page de la description de Salades est affichée")


    @when(u'Cliquer sur Fraises')
    def Fraises(context):
        Calendrier_Properties.Recolte(context,'//*[@id="product-wrap"]/div/div[2]/div[1]/a')
    @then(u'Une page de la description de Fraises est affichée')
    def DescFraises(context):
        print("Une page de la description de Fraises est affichée")

    @when(u'Cliquer sur Rhubarbes')
    def Rhubarbes(context):
        Calendrier_Properties.Recolte(context,'//*[@id="product-wrap"]/div/div[6]/div[1]/a')

    @then(u'Une page de la description de Rhubarbes est affichée')
    def DescRhubarbes(context):
        print("Une page de la description de Rhubarbes est affichée")

    @when(u'Cliquer sur Betteraves rouges')
    def BetteravesRg(context):
        Calendrier_Properties.Recolte(context,'//*[@id="product-wrap"]/div/div[3]/div[1]/a')

    @then(u'Une page de la description de Betteraves rouges est affichée')
    def DescBetteravesRg(context):
        print("Une page de la description de Betteraves rouges est affichée")

    @when(u'Cliquer sur Bettes')
    def Bettes(context):
        Calendrier_Properties.Recolte(context,'//*[@id="product-wrap"]/div/div[4]/div[1]/a')
    @then(u'Une page de la description de Bettes est affichée')
    def DescBettes(context):
        print("Une page de la description de Bettes est affichée")

    @when(u'Cliquer sur Carottes')
    def Carottes(context):
        Calendrier_Properties.Recolte(context,'//*[@id="product-wrap"]/div/div[5]/div[1]/a')

    @then(u'Une page de la description de Carottes est affichée')
    def DescCarottes(context):
        print("Une page de la description de Carottes est affichée")

    @when(u'Cliquer sur Choux')
    def Choux(context):
        Calendrier_Properties.Recolte(context,'//*[@id="product-wrap"]/div/div[6]/div[1]/a')

    @then(u'Une page de la description de Choux est affichée')
    def DescChoux(context):
        print("Une page de la description de Choux est affichée")

    @when(u'Cliquer sur Courgettes')
    def Courgettes(context):
        Calendrier_Properties.Recolte(context,'//*[@id="product-wrap"]/div/div[8]/div[1]/a')

    @then(u'Une page de la description de Courgettes est affichée')
    def DescCourgettes(context):
        print("Une page de la description de Courgettes est affichée")

    @when(u'Cliquer sur Epinards')
    def Epinards(context):
        Calendrier_Properties.Recolte(context,'//*[@id="product-wrap"]/div/div[9]/div[1]/a')

    @then(u'Une page de la description de Epinards est affichée')
    def DescEpinards(context):
        print("Une page de la description de Epinards est affichée")

    @when(u'Cliquer sur Navets')
    def Navets(context):
        Calendrier_Properties.Recolte(context,'//*[@id="product-wrap"]/div/div[11]/div[1]/a')

    @then(u'Une page de la description de Navets est affichée')
    def DescNavtes(context):
        print("Une page de la description de Navets est affichée")

    @when(u'Cliquer sur Oignons')
    def Oignons(context):
        Calendrier_Properties.Recolte(context,'//*[@id="product-wrap"]/div/div[12]/div[1]/a')

    @then(u'Une page de la description de Oignons est affichée')
    def DescOignons(context):
        print("Une page de la description de Oignons est affichée")

'''
    
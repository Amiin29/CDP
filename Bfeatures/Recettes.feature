# language: fr
  Fonctionnalité: Recettes

    Scénario: Ajouter une recette sans résumé
      Etant donné La page de la liste des recette dans le backend est ouvertee
      Quand Cliquer sur le bouton "Ajouter une recette
      Et Saisir le titre
      Et Saisir le résumé
      Et Saisir la description d'image
      Et Saisir la liste des Ingrédients
      Et Saisir la Liste des étapes
      Et Cliquer sur le bouton "Sauvegarder"
      Alors La liste des recettes avec la nouvelle recette est affichée

    Scénario: Ajouter une recette sans résumé
      Etant donné La page de la liste des recette dans le backend est ouverte
      Quand Cliquer sur le bouton "Ajouter une recette
      Et Saisir le titre
      Et Saisir la description d'image
      Et Saisir la liste des Ingrédients
      Et Saisir la Liste des étapes
      Et Cliquer sur le bouton "Sauvegarder"
      Alors Un message d'erreur indiquant que le champ de résumé est obligatoire

    Scénario: Modifier une recette
      Etant donné La page de la liste des recettes publiées dans le backend est ouverte
      Quand Rechercher une recette
      Et Cliquer sur le bouton de modification
      Et Effacer quelque caractères
      Et Cliquer sur le bouton "Sauvegarder"
      Et Ouvrir la page d'accueil de site web
      Et Cliquer sur le bouton "Nos recettes " dans le menu
      Et Rechercher la recette
      Alors Pas de résultat

    Scénario: Publier une recette
      Etant donné La page de la liste des recettes non publiées dans le backend est ouverte
      Quand Rechercher une recette
      Et Cliquer sur le switch
      Et Ouvrir la page d'accueil de site web
      Et Cliquer sur le bouton "Nos recettes" dans le menu
      Et Rechercher la recette publiée
      Alors Seulement la recette est affichée dans la liste

    Scénario: Vérifier l'affichage de la recette dans le site
      Etant donné La page d'accueil de site web est ouverte
      Quand Cliquer sur le bouton "Nos recettes" dans le menu
      Et Rechercher la recette publiée dans le site
      Et Afficher la recette
      Alors La page de la recette avec les modifications dans le résumé est affichée

    Scénario: Rechercher une recette
      Etant donné La page de la liste des recette dans le backend est ouverte
      Quand Saisir le nom de la recette dans le champ de recherche
      Alors Seulement la recette est affichée dans la liste

    Scénario: Supprimer une recette
      Etant donné La page de la liste des recette dans le backend est ouverte
      Quand Rechercher une recette
      Et Cliquer sur le bouton de suppression
      Et Confirmer la suppression
      Et Rechercher la recettes
      Alors Aucune recette est affichée
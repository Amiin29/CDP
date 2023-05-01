# language: fr
  Fonctionnalité: Produits

    Scénario: Ajouter un produit en laissant un champ obligatoire vide
      Etant donné La page de la liste des produits est ouverte
      Quand Cliquer sur "Ajouter un produit"
      Et Saisir le titre de produit
      Et Choisir une catégorie
      Et Saisir la description d'image
      Et Saisir l'historique
      Et Saisir les propriétés
      Et Cliquer sur Sauvegarder
      Alors Un message d'erreur s'affiche indiquant que le champ "Astuces/Conservation/Dégustation" est obligatoire

    Scénario: Ajouter un produit
      Etant donné La page de la liste des produits est ouverte
      Quand Cliquer sur "Ajouter un produit"
      Et Saisir le titre de produit
      Et Choisir une catégorie
      Et Saisir la description d'image
      Et Saisir l'historique
      Et Saisir les propriétés
      Et Saisir les astuces
      Et Cliquer sur Sauvegarder
      Alors Le produit est ajouté à la liste des produits

    Scénario: Rechercher un produit
      Etant donné La page de la liste des produits est ouverte
      Quand Saisir le nom d'un produit dans le recherche
      Alors Seulement le produit souhaité est affiché est les autres produits sont masqués

    Scénario: Modifier le nom d'un produit
      Etant donné La page de la liste des produits est ouverte
      Quand Rechercher le produit à modifier
      Et Cliquer sur le bouton de modification
      Et Supprimer quelque caractères de nom
      Et Cliquer sur "Sauvegarder"
      Et Ouvrir la page de tous les récoltes dans le siteweb de la cueillette de Pithienville
      Et Cliquer sur le nom de produit modifié
      Alors Une page contenant une descrption de produit s'affiche avec un nom modifié

    Scénario: Supprimer un produit
      Etant donné La page de la liste des produits est ouverte
      Quand Rechercher le produit à surpprimer
      Et Cliquer sur le bouton de suppression
      Et Confirmer la suppression
      Alors Le produit est supprimé de la liste des produits
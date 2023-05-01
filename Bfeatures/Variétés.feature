# language: fr
  Fonctionnalité: Produits

    Scénario: Ajouter une variété sans contenu
      Etant donné La page de la liste des variétés est ouverte
      Quand Cliquer sur le bouton "Ajouter une variété"
      Et Choisir un produit
      Et Cliquer sur le bouton "Sauvegarder"
      Alors Un message d'erreur s'affiche indiquant que le champ "Contenu" est obligatoire

    Scénario: Ajouter une variété
      Etant donné La page de la liste des variétés est ouverte
      Quand Cliquer sur le bouton "Ajouter une variété"
      Et Choisir un produit
      Et Saisir un contenu
      Et Cliquer sur le bouton "Sauvegarder"
      Alors La variété est ajoutée à la liste des variétés

    Scénario: Rechercher une variété
      Etant donné La page de la liste des variétés est ouverte
      Quand Saisir le nom d'une variété dans le recherche
      Alors Seulement la variété souhaitée est affiché est les autres sont masqués

    Scénario: Modifier le nom d'un produit
      Etant donné La page de la liste des variétés est ouverte
      Quand Rechercher la variété à surpprimer
      Et Cliquer sur le bouton de modification
      Et Supprimer quelque caractères de contenu
      Et Cliquer sur "Sauvegarder"
      Et Ouvrir la page de tous les récoltes dans le siteweb de la cueillette de Pithienville
      Et Cliquer sur le nom de la variété modifiée
      Alors Une page contenant une descrption de produit s'affiche avec un contenu modifié

    Scénario: Supprimer un produit
      Etant donné La page de la liste des variétés est ouverte
      Quand Rechercher la variété à surpprimer
      Et Cliquer sur le bouton de suppression
      Et Confirmer la suppression
      Alors La variété est supprimée de la liste des variétés
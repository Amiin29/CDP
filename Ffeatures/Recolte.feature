# language: fr
  Fonctionnalité: Récoltes
    Scénario:Afficher les récoltes en ce moment
      Vérifier si le dropdown "Les récoltes" dans la page d'accueil fonctionne correctement
      Etant donné la page d'accueil est ouverte
      Quand Cliquer sur le bouton "Les récoltes" dans la bar de navigation
      Et Revenir à la page d'accueil
      Et Cliquer sur le bouton "En ce moment"
      Et Cliquer sur le nom de la recette du moment
      Et Cliquer sur Framboises
      Et Cliquer sur Betteraves rouges
      Et Cliquer sur Fleurs à sécher : les immortelles et les statices
      Et Cliquer sur le bouton "Calendrier"
      Et Cliquer sur le bouton "Des fruits, des légumes, des fleurs"
      Et Cliquer sur "Suivant"
      Alors Une page contenant une description d'une récoltee est affichée

    Scénario: Afficher les récoltes précédents
      Etant donné La page contenant une description d'une récolte est ouverte
      Quand Cliquer sur "Précédent"
      Et Cliquer sur "Tout"
      Alors Une page contenant une description d'une récolte est affichée

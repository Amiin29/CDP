# language: fr
  Fonctionnalité: Newsletter

    Scénario: Vérifier Newsletter
      Vérifer si le button de Newsletter dans l'interface accueil marche correctement

      Etant donné que La page d'accueil est ouverte
      Quand Cliquer sur le button de Newsletter
      
      # S'abonner en laissant le champ de l'email vide sachant que Le champ de saisie de l'email est obligatoire
      Et Cocher la case pour accepter et recevoir les newsletter
      Et Cliquer sur le button "Je m'abonne"
      # Un message s'affiche en indiquant que l'inscription est échouée et que je dois remplir le champ de l'email
      
      # S'abonner avec un email non valide
      Et Saisir un email non valide
      Et Cocher la case pour accepter et recevoir les newsletter et s'abonner
      Alors Un message s'affiche en indiquant que l'inscription est échouée et que je dois vérifier le champ de l'email

    Scénario: S'abonner au newsletter
      Etant donné que La page d'accueil est ouverte
      Quand Cliquer sur le button de Newsletter
      # S'abonner en remplissant seulement le champ de l'email avec un email valide sachant que seulement le champ de saisie d'email est obligatoire
      Et Saisir un email valide
      Et Cocher la case pour accepter et recevoir les newsletter
      # Un message s'affiche en indiquant que l'inscription est effectuée avec succès
      
      # S'abonner avec des chiffres dans le champ de Prénom
      Et Saisir des chiffres dans le Prénom
      Et Cocher la case pour accepter et recevoir les newsletter et s'abonner
      # Un message s'affiche en indiquant que l'inscription est échouée et que je dois vérifier le champ de Prénom

      # S'abonner avec des chiffres dans le champ de Nom
      Et Saisir des chiffres dans le Nom
      Et Cocher la case pour accepter et recevoir les newsletter et s'abonner
      # Un message s'affiche en indiquant que l'inscription est échouée et que je dois vérifier le champ de Nom

      # S'abonner avec des chiffres dans le champ de Ville
      Et Saisir des chiffres dans Ville
      Et Cocher la case pour accepter et recevoir les newsletter et s'abonner
      # Un message s'affiche en indiquant que l'inscription est échouée et que je dois vérifier le champ de Ville



      # S'abonner à la newsletter avec un numéro de téléphone non valide
      Et Saisir un numéro de Telephone non valide
      Et Cocher la case pour accepter et recevoir les newsletter et s'abonner
      # Un message s'affiche en indiquant que l'inscription est échouée et que je dois vérifier le champ de Télephone

      # S'abonner à la newsletter avec des coordonnées valides
      # Un Nom valide est un ensemble de caractères
      #  Un Prénom valide est un ensemble de caractères
      #  Un Téléphone valide est un ensemble de chiffres
      #  Un Email valide : avant le « @ », on accepte toutes les lettres minuscules et majuscules et qu'en plus, on accepte les points, les tirets et les tirets bas (underscore, touche 8 du clavier). Puis après le « @ » on accepte toutes les lettres, des points et des tirets/tirets bas.
      #  un Code postal valide est un ensemble de chiffres et de lettres
      #  une Ville valide est un ensemble de caractères
      Et Saisir un Nom valide
      Et Saisir un Prenom valide
      Et Saisir un numéro de téléphone valide
      Et Saisir un Email déjà utilisé et valide
      Et Saisir une Adresse valide
      Et Saisir un code postal valide
      Et Saisir une Ville valide
      Et Cocher la case pour accepter et recevoir les newsletter
      Et Cliquer sur le button "Je m'abonne"
      # Une interface indiquant que l'inscription est effectuée avec succès

      # S'abonner sans cocher la case pour accepter et recevoir les newsletter
      Et Décocher la case pour accepter et recevoir les newsletter
      Et Cliquer sur le button "Je m'abonne"
      Alors Un message s'affiche en indiquant que l'inscription est échouée et je dois cocher la case pour accepter et recevoir les newsletter


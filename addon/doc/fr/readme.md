# Everything

* Auteur: Nael Sayegh 
* URL: [infos@nael-accessvision.com](mailto:infos@nael-accessvision.com)
* Télécharger la [version stable][1] ;
<!-- * Download the [Latest version on Nael-AccessVision.com](https://) ; -->
* Compatibilité NVDA: 2021.3 et supérieurs ;
* [Code source sur GitHub][2] ;

# Présentation

Cette extension apporte au logiciel Everything la possibilité de changer la position des informations des colones énoncées par NVDA comme par exemple la date de modification, la taille ou le chemin, ainsi que la possibilité d'ctiver ou désactiver l'annonce du nom des colones.

## Fonctionnement

Une fois cette extension installée, par défaut l'annonce des colones est la suivante: nom, date, taille, chemin.  
Pour modifier cet ordre utilisez le raccourci ctrl+shift+O.  
Un fichier s'ouvre, pour modifier l'ordre, descendez jusqu'à la ligne qui commence par lines =  
Après le signe égal, vous pouvez déplacer les variables pour changer l'ordre d'apparition des colonnes.  
Veillez à laisser un espace entre chaque variable quand vous les modifiez.  
Par défaut l'annonce des colones est activée. Si vous souhaitez la désactiver descendez dans le fichier jusqu'à la ligne sayColumn=True.  
Pour la désactiver écrivez False après le signe =.  
Si vous souhaitez la réactiver écrivez le chiffre True après le signe =.  
Attention, la majuscule est importante lors du changement de cette valeur.  
Une fois fini, enregistrez les modifications et fermez le fichier.  
Pour que les modifications prennent effet, effectuer le raccourci ctrl+shift+r dans everything.

## Changements

### Version 2023.07.24
  * Première version

Copyright ©: 2023 (Nael Sayegh et Nael-Accessvision)

<!-- links section -->

[1]: https://github.com/Nael-Sayegh/Everything/releases/download/2023.07.24/everything-2023.07.24.nvda-addon

[2]: https://github.com/Nael-Sayegh/Everything


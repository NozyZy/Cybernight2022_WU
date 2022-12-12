## vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

> Categorie : Web
>
> vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
> 
> Vous avez essayé de vous déconnecter ?
>
> Difficulté : Easy
>
> Auteur : MrSheepSheep
>
> Link : https://roombaverse.cybernight-c.tf/

Le cauchemar de beaucoup, je le conçois.
Je vais vous conter comment m'est venu l'idée à partir de ce titre, si bien trouve (*quoi ?!* vous me direz)

Je discute avec mes mate pendant une pause et je dis 
> vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv ca correspond à au aucune chaine de caractères
> on dirait juste le bruit du roomba qui aspire
> vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

"le roomba qui aspire", retenez bien.



SINON, on tente la description (ajoutée plus tard durant le CTF) : se déconnecter
Là j'ouvre Burspsuite, un proxy, pour voir à quoi ressemblent les requêtes qui passent
Et je vois que le `/deconnexion` est effectué via une méthode GET. Or la "bonne" façon de faire une requete de déconnexion, c'est via un POST, puisque l'on envoie la demande de déconnexion.

Je tente donc de modifier la requete avec le proxy, POST ne donne rien d'intéressant.
Par contre, dès que je sens que la solution vient des méthodes, je tente toutjours la méthode OPTIONS, qui est censée nous fournir toutes les méthodes authorisées.

Le résultat est donc : `GET, POST, CLEAN, OPTIONS`
CLEAN
"Roomba qui aspire", ou autrement dit "qui **nettoie**", CLEAN en anglais

Je passe la méthode à CLEAN
J'ai en réponse un cookie `session: *une longue chaine*`
Je forward donc la réponse, le cookie est ajouté.
Je reviens sur ma page de compte (connecté), et apparaît en bas de ma page de compte : 


> vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
> 
> CYBN{VVvvvVVvvVvvVvvvvvvVVVVVV}

🚩 CYBN{VVvvvVVvvVvvVvvvvvvVVVVVV}

*Je mettrai à jour le flag si le site est un jour de nouveau accessible, je l'ai pas sauvegardé*


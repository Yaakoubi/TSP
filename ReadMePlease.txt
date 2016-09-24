Push 1 du 24 septembre (YY) :

classe edge proposée
graph contient maintenant des méthodes pour les edges
graph contient un plot_graph approprié, on l'appelle avec G.plot_graph()
__repr__ de graph modifiée pour afficher les edges aussi
le poids est integré dans la lecture d'edges
supposons que ce qu'a donnée le prof est RempProf ( méthodes de remplissage et d'affichage données par le prof )
on crée un graph dans le main de read_stp, et on le remplie en parallèle avec RempProf, ensuite on affiche le 1er graphe du prof, on ferme la fenêtre, le graphe affiché avec G.plot_graph s'affiche, c'est le même => Cool !
on suppose qu'on ne fait aucune redondance dans le remplissage, et donc on ne lit pas les arrêtes entre le point et lui même, et dans le cas d'un full duplex, on ne lit que la moitié basse de la matrice ( le rest étant redondant) , à modifier par la suite ?
ce qui reste à ajouter ajourd'hui (par moi):
- tests
- double dictionnaire, probablement avec la méthode G.set_dictionnary()


ce qui restera à faire:
- faire des tests, beaucoup de tests
- faire des captures d'écran pour montrer au prof qu'on a les même résultats
- supprimer, ou du moins mettre en commentaire la partie du prof, une fois qu'on fait le rapport et qu'on y mentionne qu'on a le même nombre d'arretes , le même nombre de noeux, les mêmes data.. etc ( avec des capt d'écran) on la supprime carrément
- ajouter des remarques (je suis pas doué pour ça, je ferai un minimum, pense à en ajouter)
- faire un rapport

Remarques :
- j'ai ajouté 2 fichiers tests qu'on doit mentionner dans le rapport et probablement les ajouter aussi dans l'archive à rendre:
( je les ai ajouté surtt pour "voir" un truc, c'est difficile de voir quelque chose à 100 noeuds et quelques milliers d'arrêtes :p )
- pense à revoir tout le code stp, du moins après le deuxième push que je ferai d'ici ce soir, et à faire des tests, sois pas gentil avec le code :-p
- s'il y a quoi que ce soit que tu comprends pas dans ce que j'ai ajouté, dis moi :)



----------------------------------------------------------------------------------------------------------------------------------


Push 2 du 24 septembre (YY) :

-----Pending-----


----------------------------------------------------------------------------------------------------------------------------------





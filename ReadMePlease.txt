Push 1 du 24 septembre (YY) :

classe edge proposée
graph contient maintenant des méthodes pour les edges
graph contient un plot_graph approprié, on l'appelle avec G.plot_graph()
__repr__ de graph modifiée pour afficher les edges aussi
le poids est integré dans la lecture d'edges
supposons que ce qu'a donnée le prof est RempProf ( méthodes de remplissage et d'affichage données par le prof )
on crée un graph dans le main de read_stp, et on le remplie en parallèle avec RempProf, ensuite on affiche le 1er graphe du prof, on ferme la fenêtre, le graphe affiché avec G.plot_graph s'affiche, c'est le même => Cool !
on suppose qu'on ne fait aucune redondance dans le remplissage, et donc on ne lit pas les arrêtes entre le point et lui même, et dans le cas d'un full matrix, on ne lit que la moitié basse de la matrice ( le rest étant redondant) , à modifier par la suite ?

ce qui reste à ajouter ajourd'hui (par moi):
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


Push 2 du 25 septembre (YY) :

double dictionnaire ajouté
fonction pour ajouter un arrête à chaque fois au double dictionnaire
fonction pour obtenir un arrête basé sur les indices des deux noeuds en bout
par exemple, si noeud entre noeud d'indice 1 et noeud d'indice 2,
on cherche dans le double dictionnaire s'il y a dans l'entrée noeud 1, une entrée noeud 2, si oui, renvoyer l'arrete
sinon, on cherche dans l'entrée noeud 2 une entrée noeud 1, si on est là, c'est qu'il y'en a certainement (graphe complet)
c'est surtout du à ce qu'on fait pas de redondance dans le graphe, on met une information que si elle n'est pas déjà connue
à priori, ça marche bien, rester à tester
sinon, y a aussi beaucoup de redondance à enlever une fois que le rapport est fait
aussi, comme y a un tableau qui contient les edges, et le double dictionnaire contient aussi les edges indexés selon les indices des noeuds et tout, je sais pas trop s'il faut supprimer le tableau ou pas, finalement on a une redondance, mais je sais po, 
faudrait qu'on en discute et qu'on la mette potentiellement dans la partie difficultés


----------------------------------------------------------------------------------------------------------------------------------


fonction get_edge_id_from_dict() ==> test avec != indices (les mêmes, qui n'existent pas, etc.)



----------------------------------------------------------------------------------------------------------------------------------


Phase 2 : 8 octobre :

J'ai verifié le poids des arbres et j'ai comparé avec les valeurs du dernier push que t'as fait, ce sont les mêmes
En gros, j'ai réarrangé un peu les choses, et puis j'ai pas utilisé les ID ( par définition, un arrête n'existe qu'entre start et arrival, tel que id_start < id_arrival, du coup, on peu ne pas comparer les ID, d'ailleurs faut éviter le plus possible de les utiliser )
aussi, j'ai fait mst comme une subclasse de Graph, héritage et tout ça
et j'ai fait father dans la classe node ( Maxime en a parlé l'autre fois à un certain moment, ça change pas grande chose, mais boff)

j'ai nommé le nouveau script à ScriptKrusal.sh
faut faire :
chmod +x ScriptKruskal.sh
( juste la première fois je crois, et à partir de là, tu fais :
./ScriptKrusal.sh
et ça lance le tout )
voilàà voilàà :)



----------------------------------------------------------------------------------------------------------------------------------







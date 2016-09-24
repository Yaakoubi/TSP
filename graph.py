import numpy   as np
import random as rand

from node import Node
from edge import Edge

class Graph(object):
    """
    Une classe generique pour representer un graphe comme un ensemble de
    noeuds.
    """


    def __init__(self, name='Sans nom'):
        self.__name = name
        self.__nodes = []   # Attribut prive.
        self.__edges = []  # Attribut prive.

    def add_node(self, node):
        "Ajoute un noeud au graphe."
        self.__nodes.append(node)

    def add_edge(self, edge):
        "Ajoute un arrete au graphe."
        self.__edges.append(edge)

    def get_name(self):
        "Donne le nom du graphe."
        return self.__name

    def get_nodes(self):
        "Donne la liste des noeuds du graphe."
        return self.__nodes

    def get_node(self,id):
        "retourne le noeud dont le numero est id"
        return self.__nodes[id]


    def get_edges(self):
        "Donne la liste des arretes du graphe."
        return self.__edges

    def get_nb_nodes(self):
        "Donne le nombre de noeuds du graphe."
        return len(self.__nodes)

    def get_nb_edges(self):
        "Donne le nombre de arretes du graphe."
        return len(self.__edges)

    def __repr__(self):
        name = self.get_name()
        nb_nodes = self.get_nb_nodes()
        nb_edges = self.get_nb_edges()
        s = 'Graphe {0!s} comprenant {1:d} noeuds et {2:d} arretes'.format(name, nb_nodes, nb_edges)
        for node in self.get_nodes():
            s += '\n  ' + repr(node)
        for edge in self.get_edges():
            s += '\n  ' + repr(edge)
        return s



    def plot_graph(self):
        """
        Plot the graph represented by `nodes` and `edges` using Matplotlib.
        Very basic for now.
        """

        import matplotlib.pyplot as plt
        from matplotlib.collections import LineCollection

        fig = plt.figure()
        ax = fig.add_subplot(111)

        # Plot nodes.
        x = [node.get_data()[0] for node in self.get_nodes()]
        y = [node.get_data()[1] for node in self.get_nodes()]

        # Plot edges
        edge_pos = np.asarray([(  self.__nodes[e.get_data()[0]].get_data(), self.__nodes[e.get_data()[1]].get_data()   ) for e in self.get_edges()   ])
        edge_collection = LineCollection(edge_pos, linewidth=1.5, antialiased=True,
                                         colors=(.8, .8, .8), alpha=.75, zorder=0)
        ax.add_collection(edge_collection)
        ax.scatter(x, y, s=35, c='r', antialiased=True, alpha=.75, zorder=1)
        ax.set_xlim(min(x) - 10, max(x) + 10)
        ax.set_ylim(min(y) - 10, max(y) + 10)

        plt.show()
        return



if __name__ == '__main__':


    G = Graph(name='Graphe test')
    for k in range(10): # nb_nodes ici = 10
        G.add_node(Node(name='Ntest {0:d}'.format(k),data=[1000*rand.random()//1,1000*rand.random()//1 ]))
    for i in range(G.get_nb_nodes()):
        for j in range(i) : # pas de redondance , donc nb_edges = nb_nodes * (nb_nodes-1) /2
            id_start = G.get_node(i).get_id() # == i
            id_arrival = G.get_node(j).get_id() # == j
            #print  id_start , id_arrival , '\n'
            Data = [id_start,id_arrival,id_start+id_arrival]
            G.add_edge(Edge(name='E from {0:d} to {1:d}'.format(id_start, id_arrival), data=Data))
    G.plot_graph ()
    print ( G )

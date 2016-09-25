import random as rand
import numpy   as np
from node import Node
from edge import Edge

class Graph(object):
    """
    Une classe generique pour representer un graphe comme un ensemble de
    noeuds.
    """

    __node_count = 0
    __edge_count = 0

    def __init__(self, name='Sans nom'):
        self.__name = name
        self.__nodes = []   # Attribut prive.
        self.__edges = []  # Attribut prive.
        self.__dict = { }

    def add_node(self, node):
        """Ajoute un noeud au graphe."""
        self.__nodes.append(node)
        self.__node_count += 1

    def add_edge(self, edge):
        """Ajoute un arrete au graphe."""
        self.__edges.append(edge)
        self.__edge_count += 1

    def get_name(self):
        """"Donne le nom du graphe."""
        return self.__name

    def get_nodes(self):
        """Donne la liste des noeuds du graphe."""
        return self.__nodes

    def get_node(self, indice):
        """retourne le noeud dont le numero est id"""
        return self.__nodes[indice]


    def get_edges(self):
        """Donne la liste des arretes du graphe."""
        return self.__edges

    def get_nb_nodes(self):
        """Donne le nombre de noeuds du graphe."""
        return self.__node_count

    def get_nb_edges(self):
        """Donne le nombre de arretes du graphe."""
        return self.__edge_count

    def add_to_dict (self,edge):
        """ ajoute un element dans le double dictionnaire
        si e est un arrete entre noeud 1 et noeud 2
        on ajoute noeud1 -> noeud2 -> e """
        tempo_dict = self.__dict.get(edge.get_data()[0])
        if ( tempo_dict == None ) :
            tempo_dict = {}
        tempo_dict[edge.get_data()[1]] = edge
        self.__dict[edge.get_data()[0]] = tempo_dict


    def get_edge_from_dict(self, indice1,indice2):
        """retourne l'arrete entre le noeud d'indice 1 et le noeud d'incide 2"""
        edge =  self.__dict.get(indice1).get(indice2)
        if (edge == None ) :
            edge = (self.__dict[indice2])[indice1]
        return edge


    def __repr__(self):
        """Redefinie l'ffichage """
        name = self.get_name()
        nb_nodes = self.get_nb_nodes()
        nb_edges = self.get_nb_edges()
        res = 'Graphe {0!s} comprenant {1:d} noeuds et {2:d} arretes'\
            .format(name, nb_nodes, nb_edges)
        for node in self.get_nodes():
            res += '\n  ' + repr(node)
        for edge in self.get_edges():
            res += '\n  ' + repr(edge)
        for node1 , data_node1 in self.__dict.items():
            for node2, edge in data_node1.items():
                res += '\n  new :' + repr(edge)
        return res



    def plot_graph(self):
        """
        Plot the graph represented by `nodes` and `edges` using Matplotlib.
        Very basic for now.
        """

        import matplotlib.pyplot as plt
        from matplotlib.collections import LineCollection

        fig = plt.figure()
        ax_fig = fig.add_subplot(111)

        # Plot nodes.
        x_coords = [node.get_data()[0] for node in self.get_nodes()]
        y_coords = [node.get_data()[1] for node in self.get_nodes()]

        # Plot edges
        edge_pos = np.asarray([(self.__nodes[edge.get_data()[0]].get_data(),\
                                self.__nodes[edge.get_data()[1]].get_data())\
                               for edge in self.get_edges()])
        edge_collection = LineCollection(edge_pos, linewidth=1.5, antialiased=True,
                                         colors=(.8, .8, .8), alpha=.75, zorder=0)
        ax_fig.add_collection(edge_collection)
        ax_fig.scatter(x_coords, y_coords, s=35, c='r', antialiased=True, alpha=.75, zorder=1)
        ax_fig.set_xlim(min(x_coords) - 10, max(x_coords) + 10)
        ax_fig.set_ylim(min(y_coords) - 10, max(y_coords) + 10)

        plt.show()
        return



if __name__ == '__main__':


    G = Graph(name='Graphe test')
    for k in range(10): # nb_nodes ici = 10
        coords = [1000*rand.random()//1, 1000*rand.random()//1]
        test_node = Node(name='Ntest {0:d}'.format(k), data=coords)
        G.add_node(test_node)
    for i in range(G.get_nb_nodes()):
        for j in range(i):#pas de redondance , donc nb_edges = nb_nodes * (nb_nodes-1) /2
            id_start = G.get_node(i).get_id()# == i
            id_arrival = G.get_node(j).get_id()# == j
            #print  id_start , id_arrival , '\n'
            e_data = [id_start, id_arrival, id_start+id_arrival]
            e = Edge(name='E from {0:d} to {1:d}'.format(id_start, id_arrival), data=e_data)
            G.add_edge(e)
            G.add_to_dict(e)
    G.plot_graph()

    print ( G.get_edge_from_dict ( 3 , 6 ))

    #print G


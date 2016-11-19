import random as rand
import numpy as np
from node import Node
from edge import Edge
from wline import File


class Graph(object):
    """
    Une classe generique pour representer un graphe comme un ensemble de
    noeuds.
    """

    __node_count = 0
    __edge_count = 0
    __usage = False

    def __init__(self, name='Sans nom'):
        self.__name = name
        self.__nodes = []   # Attribut prive.
        self.__edges = []  # Attribut prive.
        self.__dict = {}
        self.__total_weight = 0

    def add_node(self, node):
        """Ajoute un noeud au graphe."""
        assert(isinstance(node, Node))
        self.__nodes.append(node)
        self.__node_count += 1

    def add_edge(self, edge):
        """Ajoute une arete au graphe."""
        if isinstance(
                edge, Edge) and (
                edge.weight is not None) and (edge.start != edge.end):
            self.__edges.append(edge)
            self.__edge_count += 1

    def get_name(self):
        """" Donne le nom du graphe."""
        return self.__name

    def get_nodes(self):
        """ Donne la liste des noeuds du graphe."""
        return self.__nodes

    def get_node(self, indice):
        """ Retourne le noeud dont le numero est id"""
        return self.__nodes[indice]

    def get_edges(self):
        """ Donne la liste des aretes du graphe."""
        return self.__edges

    def get_nb_nodes(self):
        """ Donne le nombre de noeuds du graphe."""
        return self.__node_count

    def get_nb_edges(self):
        """ Donne le nombre d'aretes du graphe."""
        return self.__edge_count

    @property
    def weight(self):
        return self.__total_weight

    @property
    def usage(self):
        return self.__usage

    @property
    def dict(self):
        return self.__dict

    def add_weight(self, weight):
        """Ajoute un poids au graphe."""
        if (weight is not None) and (isinstance(
                weight, int) or isinstance(weight, float)):
            self.__total_weight += weight

            # This allows the kruskal usage to be set

    # This allows the kruskal usage to be set
    @usage.setter
    def usage(self, boo):
        if (boo is not None) and (isinstance(boo, bool)):
            self.__usage = boo

    def add_to_dict(self, edge):
        """ Ajoute un element dans le double dictionnaire
        si e est une arete entre noeud 1 et noeud 2
        on ajoute noeud1 -> noeud2 -> e """
        tempo_dict = self.__dict.get(edge.start)
        if tempo_dict is None:
            tempo_dict = {}
        tempo_dict[edge.end] = edge
        self.__dict[edge.start] = tempo_dict

    def get_edge_from_dict(self, node1, node2):
        """ Retourne l'arete entre le noeud 1 et le noeud 2"""
        data_node1 = self.__dict.get(node1)
        if data_node1 is None:
            data_node2 = self.__dict.get(node2)
            if data_node2 is None:
                return None
            return data_node2.get(node1)
        if data_node1.get(node2) is None:
            data_node2 = self.__dict.get(node2)
            return data_node2.get(node1)
        else:
            return data_node1.get(node2)

    def get_neighbors(self, node1):
        """retourne les voisins d'un noeud"""
        if node1 is not None and isinstance(node1, Node):
            # L = self.__dict.get(node1)
            local_dict = {}
            for node2, set1 in self.__dict.items():
                for node3, edge in set1.items():
                    if node1 == node2:
                        local_dict[node3] = edge
                    elif node1 == node3:
                        local_dict[node2] = edge
            return local_dict
        return None

    def get_neighbors2(self, node1):
        """retourne les voisins d'un noeud"""
        if node1 is not None and isinstance(node1, Node):
            # L = self.__dict.get(node1)
            local_dict = File()
            for node2, set1 in self.__dict.items():
                for node3 in set1.keys():
                    if node1 == node2:
                        # local_dict[node3] = edge
                        local_dict.enqueue(node3)
                        # print ( node3 )
                    elif node1 == node3:
                        # local_dict[node2] = edge
                        local_dict.enqueue(node2)
                        # print node2
            return local_dict
        return None

    def __repr__(self):
        """Redefinit l'affichage """
        name = self.get_name()
        nb_nodes = self.get_nb_nodes()
        nb_edges = self.get_nb_edges()
        res = 'Graphe {0!s} comprenant {1:d} noeuds et {2:d} arretes'\
            .format(name, nb_nodes, nb_edges)
        for node in self.get_nodes():
            res += '\n' + repr(node)
        for edge in self.get_edges():
            res += '\n' + repr(edge)
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
        edge_pos = np.asarray([[edge.start.get_data(),
                                edge.end.get_data()]
                               for edge in self.get_edges()])
        edge_collection = LineCollection(edge_pos, linewidth=1.5, antialiased=True,
                                         colors=(.8, .8, .8), alpha=.75, zorder=0)
        ax_fig.add_collection(edge_collection)
        ax_fig.scatter(
            x_coords,
            y_coords,
            s=35,
            c='r',
            antialiased=True,
            alpha=.75,
            zorder=1)
        ax_fig.set_xlim(min(x_coords) - 10, max(x_coords) + 10)
        ax_fig.set_ylim(min(y_coords) - 10, max(y_coords) + 10)

        plt.show()
        return


if __name__ == '__main__':

    G = Graph(name='Graphe test')
    for k in range(10):  # nb_nodes ici = 10
        coords = [1000 * rand.random() // 1, 1000 * rand.random() // 1]
        test_node = Node(name='Ntest {0:d}'.format(k), data=coords)
        G.add_node(test_node)
    for i in range(G.get_nb_nodes()):
        for j in range(
                i):  # pas de redondance , donc nb_edges = nb_nodes * (nb_nodes-1) /2
            start = G.get_node(i)
            arrival = G.get_node(j)
            # print  start , arrival , '\n'
            e_data = [start, arrival, 200 * rand.random() // 1]
            e = Edge(
                name='Test Edge',
                data=e_data)
            G.add_edge(e)
            G.add_to_dict(e)
    G.plot_graph()

    # print G

    print G.get_edge_from_dict(G.get_node(3), G.get_node(6))
    print G.get_edge_from_dict(G.get_node(6), G.get_node(3))
    print G.get_edge_from_dict(G.get_node(6), G.get_node(6))

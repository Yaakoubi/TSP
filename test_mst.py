from edge import Edge
from node import Node
from graph import Graph
from mst import Mst
import random as rand
import unittest

class TestMstMethods(unittest.TestCase):
    """ Teste les differentes fonctions de la classe Mst """

    def setUp(self):
        """ Liste des commandes qui seront lancees a chaque test """
        G = Graph(name='Graphe test')
        for k in range(10):  # nb_nodes ici = 10
            coords = [1000 * k, 700 * k]
            test_node = Node(name='Ntest {0:d}'.format(k), data=coords)
            G.add_node(test_node)
        for i in range(G.get_nb_nodes()):
            for j in range(
                    i):
                start = G.get_node(i)
                arrival = G.get_node(j)
                e_data = [start, arrival, 200 * i]
                e = Edge(
                    name='Test Edge',
                    data=e_data)
                G.add_edge(e)
                G.add_to_dict(e)

        self.kruskal_tree = Mst(original_graph=G, method='kruskal')
        self.prim_tree = Mst(original_graph=G, method='prim', heap=True)


    def test_kruskal(self):
        """ Verification de l'algorithme de kruskal """
        self.assertEqual(self.kruskal_tree.weight, 9000)

    def test_prim(self):
        """ Verification de l'algorithme de prim """
        self.assertEqual(self.prim_tree.weight, 9000)


if __name__ == '__main__':
    unittest.main()

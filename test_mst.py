from edge import Edge
from node import Node
from graph import Graph
from mst import Mst
import unittest


class TestMstMethods(unittest.TestCase):
    """ Teste les differentes fonctions de la classe Mst """

    def setUp(self):
        """ Liste des commandes qui seront lancees a chaque test """
        self.G = Graph(name='Graphe test')
        for k in range(10):  # nb_nodes ici = 10
            coords = [1000 * k, 700 * k]
            test_node = Node(name='Ntest {0:d}'.format(k), data=coords)
            self.G.add_node(test_node)
        for i in range(self.G.get_nb_nodes()):
            for j in range(
                    i):
                start = self.G.get_node(i)
                arrival = self.G.get_node(j)
                e_data = [start, arrival, 200 * i]
                e = Edge(
                    name='Test Edge',
                    data=e_data)
                self.G.add_edge(e)
                self.G.add_to_dict(e)

        self.kruskal_tree = Mst(original_graph=self.G, method='kruskal')
        self.prim_tree = Mst(original_graph=self.G, method='prim', heap=True)

    def test_kruskal(self):
        """ Verification de l'algorithme de kruskal """
        self.assertEqual(self.kruskal_tree.weight, 9000)

    def test_prim(self):
        """ Verification de l'algorithme de prim """
        self.assertEqual(self.prim_tree.weight, 9000)

    def test_kruskal_again(self):
        self.kruskal_tree.kruskal(original_graph=self.G)
        self.assertEqual(self.kruskal_tree.weight, 9000)

    def test_prim_again(self):
        self.prim_tree.prim(original_graph=self.G, heap=False)
        self.assertEqual(self.prim_tree.weight, 9000)

    def test_kruskal_init(self):
        self.kruskal_tree.kruskal(original_graph=None)
        self.assertEqual(self.kruskal_tree.weight, 0)

    def test_prim_init(self):
        self.prim_tree.prim(original_graph=int(), heap=False)
        self.assertEqual(self.prim_tree.weight, 0)


if __name__ == '__main__':
    unittest.main()

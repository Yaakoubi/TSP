from edge import Edge
from node import Node
from graph import Graph
import unittest
import random as rand


class TestgraphMethods(unittest.TestCase):
    """ Teste les differentes fonctions de la classe Graph."""

    def setUp(self):
        """ Liste de commandes qui sera lancee a chaque test """
        self._gra_test = Graph(name='Graphe test')
        for k in range(10):  # nb_nodes ici = 10
            coords = [1000 * rand.random() // 1, 1000 * rand.random() // 1]
            test_node = Node(name='Ntest {0:d}'.format(k), data=coords)
            self._gra_test.add_node(test_node)
            self.nod_test2 = test_node  # self.nod_test2 prendra comme valeur le dernier noeud
        for i in range(self._gra_test.get_nb_nodes()):
            for j in range(
                    i):  # pas de redondance , donc nb_edges = nb_nodes * (nb_nodes-1) /2
                start = self._gra_test.get_node(i)  # == i
                arrival = self._gra_test.get_node(j)  # == j
                # print  id_start , id_arrival , '\n'
                e_data = [start, arrival, 200 * rand.random() // 1]
                e = Edge(
                    name='Test Edge', data=e_data)
                self._gra_test.add_edge(e)
                self._gra_test.add_to_dict(e)
                self._edg_test2 = e  # self._edg_test2 prendra comme valeur la derniere arete

    def test_get_name(self):
        """ Verification du nom renvoye par la fonction get_name """
        self.assertEqual('Graphe test', self._gra_test.get_name())

    def test_add_and_get_node(self):
        """ Verifie si les noeuds entres s'ajoutent en fin de liste et s'ils correspondent a un type Node """
        self.failUnless(self._gra_test.get_node(-1) == self.nod_test2)
        self.assertRaises(
            AssertionError,
            self._gra_test.add_node,
            "Ceci n'est pas un noeud")

    def test_get_nodes(self):
        """Verifie si la liste contient le bon nombre de noeuds et si ceux-ci sont bien ordonnes """
        self.failUnless(self._gra_test.get_nodes()[-1] == self.nod_test2)
        self.assertEqual(len(self._gra_test.get_nodes()), 10)

    def test_add_and_get_edges(self):
        """ Verifie si les aretes entrees s'ajoutent en fin de liste et si elles correspondent a un type Edge """
        self.failUnless(self._gra_test.get_edges()[-1] == self._edg_test2)
        self.assertRaises(
            AssertionError,
            self._gra_test.add_edge,
            "Ceci n'est pas une arete")

    def test_get_nb_edges_and_nodes(self):
        """ Verifie si le nombre de noeuds entres correspond bien a celui retourne par les fonctions """
        self.assertEqual(
            self._gra_test.get_nb_edges(), len(
                self._gra_test.get_edges()))
        self.assertEqual(
            self._gra_test.get_nb_nodes(), len(
                self._gra_test.get_nodes()))

    def test_get_edge_from_dict(self):
        """ Verifie le bon fonctionnement de la fonction get_edge_from_dict """
        edge1 = self._gra_test.get_edge_from_dict(
            self._gra_test.get_node(1), self._gra_test.get_node(4))
        self.assertTrue(edge1 is not None)
        edge2 = self._gra_test.get_edge_from_dict(
            self._gra_test.get_node(1), self._gra_test.get_node(1))
        self.assertTrue(edge2 is None)
        edge3 = self._gra_test.get_edge_from_dict(
            self._gra_test.get_node(4), self._gra_test.get_node(1))
        self.assertTrue(edge3 is not None)

    def test_repr(self):
        """ Verification qu'une chaine de caracteres est bien renvoyee a l'affichage par le module print """
        self.assertTrue(isinstance(self._gra_test.__repr__(), str))


if __name__ == '__main__':
    unittest.main()

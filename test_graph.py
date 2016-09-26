from edge import Edge
from node import Node
from graph import Graph
import unittest
import random as rand
import random


class TestgraphMethods(unittest.TestCase):
    """ Teste les differentes fonctions de la classe Graph."""

    def setUp(self):
        """ Liste de commandes qui sera lancee a chaque test """
        self._gra_test = Graph(name='Graphe test')
        for k in range(10):  # nb_nodes ici = 10
            coords = [1000 * rand.random() // 1, 1000 * rand.random() // 1]
            test_node = Node(name='Ntest {0:d}'.format(k), data=coords)
            self._gra_test.add_node(test_node)
            self.nod_test2 = test_node # self.nod_test2 prendra comme valeur le dernier noeud
        for i in range(self._gra_test.get_nb_nodes()):
            for j in range(i):  # pas de redondance , donc nb_edges = nb_nodes * (nb_nodes-1) /2
                id_start = self._gra_test.get_node(i).get_id()  # == i
                id_arrival = self._gra_test.get_node(j).get_id()  # == j
                # print  id_start , id_arrival , '\n'
                e_data = [id_start, id_arrival, id_start + id_arrival]
                e = Edge(name='E from {0:d} to {1:d}'.format(id_start, id_arrival), data=e_data)
                self._gra_test.add_edge(e)
                self._gra_test.add_to_dict(e)
                self._edg_test2 = e # self._edg_test2 prendra comme valeur le dernier arrete





    def test_get_name(self):
        """ Verification du nom renvoye par la fonction get_name. """
        self.assertEqual('Graphe test', self._gra_test.get_name())


    def test_add_and_get_node(self):
        """ Verifie si les noeuds entrees s'ajoutent en fin de liste et s'ils correspondent a un type Node """
        self.failUnless(self._gra_test.get_node(-1) )== self.nod_test2
        #self.assertRaises(AssertionError,self._gra_test.add_node, "Ceci n'est pas un noeud")

    def test_get_nodes(self):
        """Verifie si la liste de noeuds renvoie bien des objets de type noeuds et si ceux-ci sont bien ordonnes """
        self.failUnless(self._gra_test.get_nodes()[-1] == self.nod_test2)
        self.assertEqual(len(self._gra_test.get_nodes()),10)

    def test_add_and_get_edges(self):
        """ Verifie si les aretes entrees s'ajoutent en fin de liste et si elles correspondent a un type Edge """
        self.failUnless(self._gra_test.get_edges()[-1] == self._edg_test2)
        self.assertRaises(AssertionError, self._gra_test.add_edge, "Ceci n'est pas une arete")

    def test_get_nb_edges_and_nodes(self):
        """ Verifie si le nombre de noeuds entres correspond bien a celui retourne par les fonctions """
        self.assertEqual(self._gra_test.get_nb_edges(), len(self._gra_test.get_edges()))
        self.assertEqual(self._gra_test.get_nb_nodes(), len(self._gra_test.get_nodes()))



    # A FINIR !!!!
    def test_get_edge_id_from_dict(self):
        """ Verifie le bon fonctionnement de la fonction get_edge_id_from_dict """
        self._gra_test.get_edge_id_from_dict(1, 4)
        self._gra_test.get_edge_id_from_dict(1, 1)
        #self._gra_test.get_edge_id_from_dict(1, -1)
        self._gra_test.get_edge_id_from_dict(4, 1)

    # A FINIR !!!!!
    def test_get_edge_from_dict(self):
        """ Verifie le bon fonctionnement de la fonction get_edge_from_dict """
        self._gra_test.get_edge_from_dict(1, 4)
        self._gra_test.get_edge_from_dict(1, 1)
        #self._gra_test.get_edge_from_dict(1, -1)
        self._gra_test.get_edge_from_dict(4, 1)


    def test_repr(self):
        """ Verification qu'une chaine de caracteres est bien renvoyee a l'affichage par le module print. """
        self.assertTrue(type(self._gra_test.__repr__()) is str)



if __name__ == '__main__':
    unittest.main()
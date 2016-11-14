from node import Node
from wline import Queue, Heap
import unittest


class TestGraphMethods(unittest.TestCase):
    """ Teste les differentes fonctions de la classe Graph."""

    def setUp(self):
        """ Liste de commandes qui seront lancees a chaque test """
        self.nodes = []
        for k in range(5):
            self.new = Node()
            self.new.min_weight = 100 - k * 10
            self.nodes.append(self.new)

        self.queue_def = Queue()
        self.heap_def = Heap()

        self.queue_line = Queue()
        self.queue_line.enqueue(self.nodes[1])
        self.queue_line.enqueue(self.nodes[3])
        self.queue_line.enqueue(self.nodes[0])

        self.heap_line = Heap()
        self.heap_line.enqueue(self.nodes[1])
        self.heap_line.enqueue(self.nodes[3])
        self.heap_line.enqueue(self.nodes[0])

    def test_queue_init_(self):
        """ Verifie que la liste initiale est vide """
        self.failUnless(len(self.queue_def.items) == 0)

    def test_queue_enqueue(self):
        """ Verifie l'ajout d'element """
        self.failUnless(self.queue_line.items[0] == self.nodes[1])

    def test_queue_is_empty(self):
        """ Teste la fonction verifiant si la liste est vide """
        self.assertTrue(self.queue_def.is_empty())
        self.assertFalse(self.queue_line.is_empty())

    def test_queue_contains_(self):
        """ Teste si l'appartenance se fait bien sur les items de la file """
        self.assertTrue(self.nodes[1] in self.queue_line)

    def test_queue_repr_(self):
        """ Verification qu'une chaine de caracteres est bien renvoyee a l'affichage par le module print """
        self.assertTrue(isinstance(self.queue_line.__repr__(), str))

    def test_queue_dequeue(self):
        """ Verifie l'ordre de sortie de la file en FIFO"""
        self.failUnless(self.queue_line.dequeue() == self.nodes[3])
        self.failUnless(self.queue_line.dequeue() == self.nodes[1])
        self.failUnless(self.queue_line.dequeue() == self.nodes[0])

    def test_heap_init_(self):
        """ Verifie que la liste initiale est vide """
        self.failUnless(len(self.heap_def.pq) == 0)
        self.failUnless(len(self.heap_def.entry_finder) == 0)

    def test_heap_enqueue(self):
        """ Verifie l'ajout d'element """
        self.failUnless(
            self.heap_line.entry_finder[
                self.nodes[1]] == [
                self.nodes[1].min_weight,
                self.nodes[1]])

    def test_heap_is_empty(self):
        """ Teste la fonction verifiant si la liste est vide """
        self.assertTrue(self.heap_def.is_empty())
        self.assertFalse(self.heap_line.is_empty())

    def test_heap_contains_(self):
        """ Teste si l'appartenance se fait bien sur les items de la file """
        self.assertTrue(self.nodes[1] in self.heap_line)

    def test_heap_repr_(self):
        """ Verification qu'une chaine de caracteres est bien renvoyee a l'affichage par le module print """
        self.assertTrue(isinstance(self.heap_line.__repr__(), str))

    def test_heap_dequeue(self):
        """ Verifie l'ordre de sortie de la file en FIFO"""
        self.failUnless(self.heap_line.dequeue() == self.nodes[3])
        self.failUnless(self.heap_line.dequeue() == self.nodes[1])
        self.failUnless(self.heap_line.dequeue() == self.nodes[0])


if __name__ == '__main__':
    unittest.main()

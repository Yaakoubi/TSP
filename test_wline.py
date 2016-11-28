from node import Node
from wline import Queue, Heap, Heap2, File, Stack
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
        self.heap2_def = Heap2()
        self.file_def = File()
        self.stack_def = Stack()

        self.queue_line = Queue()
        self.queue_line.enqueue(self.nodes[1])
        self.queue_line.enqueue(self.nodes[3])
        self.queue_line.enqueue(self.nodes[0])

        self.heap_line = Heap()
        self.heap_line.enqueue(self.nodes[1])
        self.heap_line.enqueue(self.nodes[3])
        self.heap_line.enqueue(self.nodes[0])

        self.heap2_line = Heap2()
        self.heap2_line.enqueue(self.nodes[1], 2)
        self.heap2_line.enqueue(self.nodes[3], 1)
        self.heap2_line.enqueue(self.nodes[0], 3)

        self.file_line = File()
        self.file_line.enqueue(self.nodes[1])
        self.file_line.enqueue(self.nodes[3])
        self.file_line.enqueue(self.nodes[0])

        self.stack_line = Stack()
        self.stack_line.push(self.nodes[1])
        self.stack_line.push(self.nodes[3])
        self.stack_line.push(self.nodes[0])

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
        self.failUnless(self.queue_line.dequeue() is None)

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

    def test_heap2_init_(self):
        """ Verifie que la liste initiale est vide """
        self.failUnless(len(self.heap2_def.pq) == 0)
        self.failUnless(len(self.heap2_def.entry_finder) == 0)

    def test_heap2_enqueue(self):
        """ Verifie l'ajout d'element """
        self.failUnless(
            self.heap2_line.entry_finder[
                self.nodes[1]] == [2, self.nodes[1]])

    def test_heap2_is_empty(self):
        """ Teste la fonction verifiant si la liste est vide """
        self.assertTrue(self.heap2_def.is_empty())
        self.assertFalse(self.heap2_line.is_empty())

    def test_heap2_contains_(self):
        """ Teste si l'appartenance se fait bien sur les items de la file """
        self.assertTrue(self.nodes[1] in self.heap2_line)

    def test_heap2_repr_(self):
        """ Verification qu'une chaine de caracteres est bien renvoyee a l'affichage par le module print """
        self.assertTrue(isinstance(self.heap2_line.__repr__(), str))

    def test_heap2_dequeue(self):
        """ Verifie l'ordre de sortie de la file en FIFO"""
        self.failUnless(self.heap2_line.dequeue() == self.nodes[3])
        self.failUnless(self.heap2_line.dequeue() == self.nodes[1])
        self.failUnless(self.heap2_line.dequeue() == self.nodes[0])
        self.failUnless(self.heap2_line.dequeue() is None)

    def test_file_init_(self):
        """ Verifie que la liste initiale est vide """
        self.failUnless(len(self.file_def.items) == 0)

    def test_file_enqueue(self):
        """ Verifie l'ajout d'element """
        self.failUnless(self.file_line.items[0] == self.nodes[1])

    def test_file_is_empty(self):
        """ Teste la fonction verifiant si la liste est vide """
        self.assertTrue(self.file_def.is_empty())
        self.assertFalse(self.file_line.is_empty())

    def test_file_contains_(self):
        """ Teste si l'appartenance se fait bien sur les items de la file """
        self.assertTrue(self.nodes[1] in self.file_line)

    def test_file_repr_(self):
        """ Verification qu'une chaine de caracteres est bien renvoyee a l'affichage par le module print """
        self.assertTrue(isinstance(self.file_line.__repr__(), str))

    def test_file_dequeue(self):
        """ Verifie l'ordre de sortie de la file en FIFO"""
        self.failUnless(self.file_line.dequeue() == self.nodes[1])
        self.failUnless(self.file_line.dequeue() == self.nodes[3])
        self.failUnless(self.file_line.dequeue() == self.nodes[0])

    def test_stack_init_(self):
        """ Verifie que la liste initiale est vide """
        self.failUnless(len(self.stack_def.items) == 0)

    def test_stack_push(self):
        """ Verifie l'ajout d'element """
        self.failUnless(self.stack_line.items[0] == self.nodes[1])

    def test_stack_is_empty(self):
        """ Teste la fonction verifiant si la liste est vide """
        self.assertTrue(self.stack_def.is_empty())
        self.assertFalse(self.stack_line.is_empty())

    def test_stack_top(self):
        """ Teste si l'appartenance se fait bien sur les items de la stack """
        self.assertTrue(self.stack_line.top() == self.nodes[0])

    def test_stack_repr_(self):
        """ Verification qu'une chaine de caracteres est bien renvoyee a l'affichage par le module print """
        self.assertTrue(isinstance(self.stack_line.__repr__(), str))

    def test_stack_pop(self):
        """ Verifie l'ordre de sortie de la stack en FIFO"""
        self.failUnless(self.stack_line.pop() == self.nodes[0])
        self.failUnless(self.stack_line.pop() == self.nodes[3])
        self.failUnless(self.stack_line.pop() == self.nodes[1])
        with self.assertRaises(IndexError):
            self.stack_line.pop()


if __name__ == '__main__':
    unittest.main()

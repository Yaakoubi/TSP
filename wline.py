from node import Node
from _heapq import heappop, heappush


class Queue(object):
    """Une implementation de la structure de donnees << file >>."""

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """"Ajoute  item a la fin de la file."""
        self.items.append(item)

    def is_empty(self):
        """Verifie si la file est vide."""
        return len(self.items) == 0

    def __contains__(self, item):
        return item in self.items

    def __repr__(self):
        return repr(self.items)

    def dequeue(self):
        if len(self.items):  # =list not empty
            return self.items.pop(self.items.index(min(self.items)))
            # eject item with minimum value = (here) smallest edge
        else:
            return None


class Heap(object):
    """Une implementation de la structure de donnees << file >> en utilisant les heaps"""

    def __init__(self):
        self.pq = []  # list of entries arranged in a heap
        self.entry_finder = {}  # mapping of tasks to entries

    def enqueue(self, item):
        """Add a new task or update the priority of an existing task"""
        entry = [item.min_weight, item]
        self.entry_finder[item] = entry
        heappush(self.pq, entry)

    def dequeue(self):
        """Remove and return the lowest priority Item"""
        while self.pq:
            item = heappop(self.pq)[1]
            if item in self.entry_finder:
                del self.entry_finder[item]
                return item
        return None

    def __repr__(self):
        return repr(self.pq)

    def is_empty(self):
        """Verifie si la file est vide."""
        return len(self.pq) == 0

    def __contains__(self, item):
        return item in self.entry_finder


class Heap2(object):
    """Une implementation de la structure de donnees << file >> en utilisant les heaps"""

    def __init__(self):
        self.pq = []  # list of entries arranged in a heap
        self.entry_finder = {}  # mapping of tasks to entries

    def enqueue(self, item, priority):
        """Add a new task or update the priority of an existing task"""
        entry = [priority, item]
        self.entry_finder[item] = entry
        heappush(self.pq, entry)

    def dequeue(self):
        """Remove and return the lowest priority Item"""
        while self.pq:
            item = heappop(self.pq)[1]
            if item in self.entry_finder:
                del self.entry_finder[item]
                return item
        return None

    def __repr__(self):
        return repr(self.pq)

    def is_empty(self):
        """Verifie si la file est vide."""
        return len(self.pq) == 0

    def __contains__(self, item):
        return item in self.entry_finder


class File(object):
    """Une implementation de la structure de donnees << file >>."""

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Ajoute `item` a la fin de la file."""
        self.items.append(item)

    def dequeue(self):
        """Retire l'objet du debut de la file."""
        return self.items.pop(0)

    def is_empty(self):
        """Verifie si la file est vide."""
        return len(self.items) == 0

    def __contains__(self, item):
        return item in self.items

    def __repr__(self):
        return repr(self.items)


class Stack(object):
    """Une implementation de la structure de donnees << pile >>."""

    def __init__(self):
        self.items = []

    def push(self, item):
        """Ajoute `item` sur le dessus de la pile."""
        self.items.append(item)

    def pop(self):
        """Retire l'objet du dessus de la pile."""
        if len(self.items) == 0:
            raise IndexError("pile vide")
        return self.items.pop()  # Les listes implementent deja pop() !

    def top(self):
        """Consulte l'objet du dessus de la pile."""
        return self.items[-1]    # L'item reste dans la pile.

    def is_empty(self):
        """Verifie si la pile est vide."""
        return len(self.items) == 0

    def __repr__(self):
        return repr(self.items)


if __name__ == '__main__':

    nodes = []
    for k in range(5):
        new = Node()
        new.min_weight = 100 - k * 10
        # if k == 0:
        #     new.min_weight = 0
        # else:
        #     new.min_weight = 9999
        nodes.append(new)

    # for node in nodes:
    #     print node
    #
    # print nodes[0] < nodes[1]
    # print nodes[0] >= nodes[1]
    # print nodes[0] == nodes[1]
    # print nodes[0] != nodes[0]
    # print nodes[0] == nodes[0]
    # print nodes[2] > nodes[1]
    # print nodes[2] <= nodes[1]
    #
    # waiting_line = Queue()
    # waiting_line.enqueue(nodes[1])
    # waiting_line.enqueue(nodes[3])
    # waiting_line.enqueue(nodes[0])
    # waiting_line.enqueue(nodes[4])
    # waiting_line.enqueue(nodes[2])
    #
    # print waiting_line
    #
    # print '------------------------'
    #
    # print waiting_line.dequeue()
    # print waiting_line.dequeue()
    # print waiting_line.dequeue()
    # print waiting_line
    # print waiting_line.dequeue()
    # print waiting_line.dequeue()
    # print waiting_line
    # print waiting_line.dequeue()
    #
    # waiting_line2 = Heap()
    # waiting_line2.enqueue(nodes[1])
    # waiting_line2.enqueue(nodes[3])
    # waiting_line2.enqueue(nodes[0])
    # waiting_line2.enqueue(nodes[4])
    # waiting_line2.enqueue(nodes[2])
    #
    # print '------------------------'
    #
    # print waiting_line2.dequeue()
    # print waiting_line2.dequeue()
    # print waiting_line2.dequeue()
    # print waiting_line2
    # print nodes[0] in waiting_line2
    # print waiting_line2.dequeue()
    # print waiting_line2.dequeue()
    # print waiting_line2
    # print waiting_line2.dequeue()
    #
    # print '------------------------'
    #
    # waiting_line3 = Heap2()
    # waiting_line3.enqueue(nodes[1], 5)
    # waiting_line3.enqueue(nodes[3], 3)
    # waiting_line3.enqueue(nodes[0], 2)
    # waiting_line3.enqueue(nodes[4], 4)
    # waiting_line3.enqueue(nodes[2], 0)
    #
    # print waiting_line3
    #
    # print '------------------------'
    #
    # print waiting_line3.dequeue()
    # print waiting_line3.dequeue()
    # print waiting_line3.dequeue()
    # print waiting_line3
    # print waiting_line3.dequeue()
    # print waiting_line3.dequeue()
    # print waiting_line3
    # print waiting_line3.dequeue()

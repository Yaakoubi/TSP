class Node(object):
    """
    Une classe generique pour representer les noeuds d'un graphe.
    """

    _node_count = -1   # Compteur global partage par toutes les instances.

    def __init__(self, name='Sans nom', data=None):
        self.__name = name
        self.__data = data
        Node._node_count += 1
        self.__id = Node._node_count
        self.__father = self
        self.__rank = 0
        self.__ancestor = self
        self.__min_weight = float('infinity')
        self.__prim_father = None

    def get_name(self):
        """"Donne le nom du noeud."""
        return self.__name

    def get_id(self):
        """Donne le numero d'identification du noeud."""
        return self.__id

    def get_data(self):
        """Donne les donnees contenues dans le noeud."""
        return self.__data

    def __repr__(self):
        indice = self.get_id()
        name = self.get_name()
        data = self.get_data()
        s = 'Noeud {0!s} (id {1:d})'.format(name, indice)
        s += ' (donnees: ' + repr(data) + ')'
        return s

    def reset_node_count(self):
        self._node_count = -1

    @property
    def father(self):
        return self.__father

    # This allows the start node to be set
    @father.setter
    def father(self, father):
        if father is not None:
            self.__father = father

    @property
    def prim_father(self):
        return self.__prim_father

    # This allows the start node to be set
    @prim_father.setter
    def prim_father(self, prim_father):
        self.__prim_father = prim_father

    @property
    def ancestor(self):
        """recursive function to get node's ancestor"""
        p1 = self.__ancestor
        p2 = self.__ancestor.father
        while p2 != p1:
            p1 = p2
            p2 = p1.father
        self.__ancestor = p1
        return p1

    @property
    def rank(self):
        return self.__rank

    # This allows the rank node to be set
    @rank.setter
    def rank(self, rank):
        if rank != 0:
            self.__rank = rank

    @property
    def min_weight(self):
        return self.__min_weight

    # This allows the min weight to be set
    @min_weight.setter
    def min_weight(self, min_weight):
        if isinstance(min_weight, (int, float)):
            self.__min_weight = min_weight

    def __gt__(self, other):
        if self.min_weight > other.min_weight:
            return True
        return False

    def __lt__(self, other):
        if self.min_weight < other.min_weight:
            return True
        return False

    def __ge__(self, other):
        if self.min_weight >= other.min_weight:
            return True
        return False

    def __le__(self, other):
        if self.min_weight <= other.min_weight:
            return True
        return False

if __name__ == '__main__':

    nodes = []
    for k in range(5):
        nodes.append(Node())

    nodes[1].father = nodes[0]
    nodes[2].father = nodes[1]
    nodes[3].father = nodes[1]

    for node in nodes:
        print repr(node) + "  \'s father is :  " + repr(node.father)

    print '\n'

    for node in nodes:
        print repr(node) + "  \'s ancestor is :  " + repr(node.ancestor)

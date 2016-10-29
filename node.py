class Node(object):
    """
    Une classe generique pour representer les noeuds d'un graphe.
    """

    __node_count = -1   # Compteur global partage par toutes les instances.

    def __init__(self, name='Sans nom', data=None):
        self.__name = name
        self.__data = data
        Node.__node_count += 1
        self.__id = Node.__node_count
        self.__father = None

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

    @property
    def father(self):
        if self.__father is not None:
            return self.__father
        return self

    # This allows the start node to be set
    @father.setter
    def father(self, father):
        if father is not None:
            self.__father = father

    @property
    def ancestor(self):
        p1 = self
        p2 = self.father
        while p2 != p1:
            p1 = p2
            p2 = p1.father
        return p1


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

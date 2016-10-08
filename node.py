class Node(object):
    """
    Une classe generique pour representer les noeuds d'un graphe.
    """

    __node_count = -1   # Compteur global partage par toutes les instances.
    __father = None

    def __init__(self, name='Sans nom', data=None):
        self.__name = name
        self.__data = data
        Node.__node_count += 1
        self.__id = Node.__node_count

    def get_name(self):
        "Donne le nom du noeud."
        return self.__name

    def get_id(self):
        "Donne le numero d'identification du noeud."
        return self.__id

    def get_data(self):
        "Donne les donnees contenues dans le noeud."
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
        return self.__father

    # This allows the start node to be set
    @father.setter
    def father(self, father):
        if father is not None :
            self.__father = father

    @property
    def ancestor(self):
        if self.__father is None:
            return self
        else :
            return self.__father.ancestor





if __name__ == '__main__':

    nodes = []
    for k in range(5):
        nodes.append(Node())

    for node in nodes:
        print node

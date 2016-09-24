class Edge(object):
    """
    Une classe generique pour representer les arretes d'un graphe.
    """

    __edge_count = -1   # Compteur global partage par toutes les instances.

    def __init__(self, name='Sans nom', data=None):
        self.__name = name
        self.__data = data
        Edge.__edge_count += 1
        self.__id = Edge.__edge_count

    def get_name(self):
        "Donne le nom de l'arrete."
        return self.__name

    def get_id(self):
        "Donne le numero d'identification de l'arrete."
        return self.__id

    def get_data(self):
        "Donne les donnees contenues dans l'arrete."
        return self.__data

    def __repr__(self):
        indice = self.get_id()
        name = self.get_name()
        data = self.get_data()
        s  = 'Edge {0!s} (id {1:d})'.format(name, indice)
        s += ' (donnees: ' + repr(data) + ')'
        return s


if __name__ == '__main__':

    edges = []
    for k in range(5):
        edges.append(Edge())

    for edge in edges:
        print edge

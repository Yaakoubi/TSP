class Edge(object):
    """
    Une classe generique pour representer les arretes d'un graphe.
    """

    __edge_count = -1   # Compteur global partage par toutes les instances.

    def __init__(self, name='Sans nom', data=None):
        self.__name = name
        if data is not None:
            self.__data = data
        else:
            self.__data = [None, None, None]
        Edge.__edge_count += 1
        self.__id = Edge.__edge_count

    def get_name(self):
        """"Donne le nom de l'arrete."""
        return self.__name

    def get_id(self):
        """Donne le numero d'identification de l'arrete."""
        return self.__id

    def get_data(self):
        """Donne les donnees contenues dans l'arrete."""
        return self.__data

    @property
    def start(self):
        if self.__data is not None:
            try:
                return self.__data[0]
            except IndexError:
                return None
        return None

    # This allows the start node to be set
    @start.setter
    def start(self, start):
        try:
            self.__data[0] = start
        except IndexError:
            self.__data.insert(0, start)

    @property
    def end(self):
        if self.__data is not None:
            try:
                return self.__data[1]
            except IndexError:
                return None
        return None

    # This allows the end node to be set
    @end.setter
    def end(self, end):
        try:
            self.__data[1] = end
        except IndexError:
            self.__data.insert(1, end)

    @property
    def weight(self):
        if self.__data is not None:
            try:
                return self.__data[2]
            except IndexError:
                return None
        return None

    # This allows the start node to be set
    @weight.setter
    def weight(self, weight):
        try:
            self.__data[2] = weight
        except IndexError:
            self.__data.insert(2, weight)

    def __repr__(self):
        indice = self.get_id()
        name = self.get_name()
        data = self.get_data()
        s = 'Edge {0!s} (id {1:d})'.format(name, indice)
        s += ' (donnees: ' + repr(data) + ')'
        return s

    def __ne__(self, other):
        if self.weight != other.weight:
            return True
        return False

    def __eq__(self, other):
        if self.weight == other.weight:
            return True
        return False

    def __gt__(self, other):
        if self.weight > other.weight:
            return True
        return False

    def __lt__(self, other):
        if self.weight < other.weight:
            return True
        return False

    def __ge__(self, other):
        if self.weight >= other.weight:
            return True
        return False

    def __le__(self, other):
        if self.weight <= other.weight:
            return True
        return False


if __name__ == '__main__':

    edges = []
    for k in range(5):
        new = Edge()
        new.weight = 100 - k * 10
        edges.append(new)

    for edge in edges:
        print edge

    # print edges[0] < edges[1]
    # print edges[0] >= edges[1]
    # print edges[0] == edges[1]
    # print edges[0] != edges[0]
    # print edges[0] == edges[0]
    # print edges[2] > edges[1]
    # print edges[2] <= edges[1]

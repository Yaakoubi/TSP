from graph import Graph
from mst import Mst
# from random import randint
from wline import File


class Cycle(Graph):
    """ This is a special kind of graph made to search for the shortest path"""

    # ordrerd_list = []
    file = File()

    def __init__(self, name='Sans nom', original_graph=None, method='kruskal', num_node = 0):
        Graph.__init__(self, name)
        self.dico_opt_path = {"a280": 2579, "ali535": 202339, "att48": 10628, "att532": 27686, "bayg29": 1610, "bays29": 2020,
"berlin52": 7542, "bier127": 118282, "brazil58": 25395, "brd14051": 469385, "brg180": 1950, "burma14": 3323,
"ch130": 6110, "ch150": 6528, "d198": 15780, "d493": 35002, "d657": 48912, "d1291": 50801, "d1655": 62128,
"d2103": 80450, "d15112": 1573084, "d18512": 645238, "dantzig42": 699, "dsj1000": 18660188,
"eil51": 426, "eil76": 538, "eil101": 629, "fl417": 11861, "fl1400": 20127, "fl1577": 22249, "fl3795": 28772,
"fnl4461": 182566, "fri26": 937, "gil262": 2378, "gr17": 2085, "gr21": 2707, "gr24": 1272, "gr48": 5046,
"gr96": 55209, "gr120": 6942, "gr137": 69853, "gr202": 40160, "gr229": 134602, "gr431": 171414, "gr666": 294358,
"hk48": 11461, "kroA100": 21282, "kroB100": 22141, "kroC100": 20749, "kroD100": 21294, "kroE100": 22068,
"kroA150": 26524, "kroB150": 26130, "kroA200": 29368, "kroB200": 29437, "lin105": 14379, "lin318": 42029,
"linhp318": 41345, "nrw1379": 56638, "p654": 34643, "pa561": 2763, "pcb442": 50778, "pcb1173": 56892,
"pcb3038": 137694, "pla7397": 23260728, "pla33810": 66048945, "pla85900": 142382641, "pr76": 108159,
"pr107": 44303, "pr124": 59030, "pr136": 96772, "pr144": 58537, "pr152": 73682, "pr226": 80369, "pr264": 49135,
"pr299": 48191, "pr439": 107217, "pr1002": 259045, "pr2392": 378032, "rat99": 1211, "rat195": 2323,
"rat575": 6773, "rat783": 8806, "rd100": 7910, "rd400": 15281, "rl1304": 252948, "rl1323": 270199,
"rl1889": 316536, "rl5915": 565530, "rl5934": 556045, "rl11849": 923288, "si175": 21407, "si535": 48450,
"si1032": 92650, "st70": 675, "swiss42": 1273, "ts225": 126643, "tsp225": 3916, "u159": 42080, "u574": 36905,
"u724": 41910, "u1060": 224094, "u1432": 152970, "u1817": 57201, "u2152": 64253, "u2319": 234256,
"ulysses16": 6859, "ulysses22": 7013, "usa13509": 19982859, "vm1084": 239297, "vm1748": 336556}


        if original_graph is not None:

            for node in original_graph.get_nodes():
                self.add_node(node)

            if method == 'kruskal':
                self.__spanning_tree = Mst(
                    original_graph=original_graph, method='kruskal')
                source = original_graph.get_node(0).ancestor

            elif method == 'prim':
                # source = original_graph.get_node(randint(0, original_graph.get_nb_nodes() - 1))
                source = original_graph.get_node(num_node)
                self.__spanning_tree = Mst(
                    original_graph=original_graph,
                    method='prim',
                    heap=True,
                    source=source)

            self.add_to_list(source)
            self.trace_cycle(original_graph)
            # self.__spanning_tree.plot_graph()
            # self.plot_graph()
            # print self.__spanning_tree.get_neighbors(source).keys()

            self.poids_algo, self.poids_opt = self.weight, self.dico_opt_path[name[:len(name)-4]]
            self.err_rel = ((1000 * (float(self.poids_algo) - float(self.poids_opt))) // float(self.poids_algo)) / 1000
            print "Poids obtenu via l'algorithme de Rosenkrantz : " + str(self.poids_algo)
            print "Poids optimal : " + str(self.poids_opt) + "\nErreur relative : " + str(self.err_rel * 100) + "%"

    @property
    def spanning_tree(self):
        return self.__spanning_tree

    def add_to_list(self, node):
        # self.ordrerd_list.append(node)
        self.file.enqueue(node)
        # print "node = ", node
        local_node_neighbors = self.__spanning_tree.get_neighbors(node)
        # print "local_neighbors == " , local_node_neighbors , '\n\n'
        for local_node, local_edge in local_node_neighbors.items():
            if not ( local_node in self.file ) :
                self.add_to_list(local_node)


    def trace_cycle(self, original_graph):
        # for i in xrange(0,original_graph.get_nb_nodes()):
        #     self.add_edge(original_graph.get_edge_from_dict(self.ordrerd_list[i-1],self.ordrerd_list[i]))
        source = self.file.dequeue()
        node2 = source
        while not self.file.is_empty():
            node1 = node2
            node2 = self.file.dequeue()
            edge_to_add = original_graph.get_edge_from_dict(node1, node2)
            self.add_edge(edge_to_add)
            self.add_weight(edge_to_add.weight)
        edge_to_add = original_graph.get_edge_from_dict(source, node2)
        self.add_edge(edge_to_add)
        self.add_weight(edge_to_add.weight)

from read_stsp import read_edges
from read_stsp import read_header
from read_stsp import read_nodes
from graph import Graph
from cycle import Cycle
from random import randint

if __name__ == "__main__":
    import sys

    finstance = sys.argv[1]
    G = Graph()
    with open(finstance, "r") as fd:
        header = read_header(fd)
        # print 'Header: ', header
        dim = header['DIMENSION']
        edge_weight_format = header['EDGE_WEIGHT_FORMAT']

        print "Reading nodes"
        nodes = read_nodes(header, fd, G)

        print "Reading edges"
        edges = read_edges(header, fd, G)

    method = None
    if len(sys.argv) >= 3:
        method = sys.argv[2]

    # G.plot_graph()
    # print (G)

    # prim_tree = Mst(original_graph=G, method='prim', heap=True)
    # print 'Poids total du graphe 2 : ' + header.__getitem__('NAME') + ' = '
    # + str(prim_tree.weight) + '\n'

    # kruskal_tree = Mst(original_graph=G, method='kruskal')
    # kruskal_tree.plot_graph()
    # print 'Poids total du graphe : ' + header.__getitem__('NAME') + ' = ' +
    # str(kruskal_tree.weight) + '\n'

    # for i in prim_tree.get_nodes():
    # print i.get_id() , prim_tree.get_neighbors(i) , ' ------ ' ,
    # i.ancestor.get_id(), '\n\n'

    nb_nodes = G.get_nb_nodes()
    graph_min = None
    # graph_min = Graph()
    # graph_min.add_weight(float('infinity'))
    if method is None or method == 'kruskal':
        cycle1 = Cycle(name=header['NAME'], original_graph=G, method='kruskal')
        graph_min = cycle1
    # print "nombre de noeuds : ", nb_nodes
    if method is None or method == 'prim':
        if nb_nodes > 600 and method is None:
            repetitions = [randint(0, G.get_nb_nodes() - 1)
                           for i in xrange(50)]
            print repetitions
        else:
            repetitions = xrange(nb_nodes)
        for num_node in repetitions:
            cycle2 = Cycle(
                name=header['NAME'],
                original_graph=G,
                method='prim',
                num_node=num_node)
            if graph_min is None or cycle2.weight < graph_min.weight:
                graph_min = cycle2
                # print "Poids obtenu via l'algorithme de Rosenkrantz : " + str(graph_min.weight)
                # print "Poids optimal : " + str(graph_min.poids_opt) + \
                #       "\nErreur relative : " + str(graph_min.err_rel * 100) + "%"

    graph_min.plot_graph()
    # graph_min.spanning_tree.plot_graph()
    if graph_min.prim:
        print "Poids obtenu avec Prim pour le graphe " + header['NAME'] + ": " + str(graph_min.poids_algo)
        print "Noeud source : ", str(graph_min.source)
    elif graph_min.kruskal:
        print "Poids obtenu avec Kruskal pour le graphe " + header['NAME'] + ": " + str(graph_min.poids_algo)
    if graph_min.found:
        print "Poids optimal : ", str(graph_min.poids_opt), "\nErreur relative : ", str(graph_min.err_rel * 100), "%\n"
    else:
        print 'valeur du chemin optimal non trouvee\n'

    print graph_min.ordrerd_list

"""Main TSP hook."""

from tsp_helper import get_distance
from graph import Graph
from node import Node
from edge import Edge
from cycle import Cycle


def get_visit_order(geo_points):
    """THIS IS THE ONLY FUNCTION THAT YOU NEED TO MODIFY FOR PHASE 5.

    The only argument, *geoPoints*, is a list of points that user has marked.
    Each element of geoPoints is an instance of the GeoPoint class. You need to
    create your graph using these points. You obtain the distance between two
    points by calling the *getDistance* function; for example:

    get_distance(geoPoints[0], geoPoints[1])

    Run your tsp solver and return the locations visit order. The return value,
    *order*, must be a list of indices of points, specifying the visit order.

    In the example implementation below, we visit each point by the order
    in which they were marked (clicked).
    """
    # longueur = len(geoPoints)
    print "first leg length: ", get_distance(geo_points[0], geo_points[1])
    # order = range(longueur)  # default order
    # order += [order[0]]

    # longueur_totale = 0
    # for x in xrange(longueur-1):
    #     longueur_totale += get_distance(geoPoints[x], geoPoints[x+1])
    # longueur_totale += get_distance(geoPoints[-1],geoPoints[0])
    # print "Longueur totale du cycle Google maps : " +str(longueur_totale)
    # print order

    graph = Graph(name='Graphe test')
    for k in xrange(len(geo_points)):
        coords = [geo_points[k].lat, geo_points[k].lng]
        test_node = Node(name='Ntest {0:d}'.format(k), data=coords)
        graph.add_node(test_node)

    for i in range(graph.get_nb_nodes()):
        for j in range(
                i):  # pas de redondance , donc nb_edges = nb_nodes * (nb_nodes-1) /2
            start = graph.get_node(i)
            arrival = graph.get_node(j)
            # print  start , arrival , '\n'
            e_data = [
                start, arrival, get_distance(
                    geo_points[i], geo_points[j])]
            e = Edge(
                name='Edge' + str(i) + '-' + str(j),
                data=e_data)
            graph.add_edge(e)
            graph.add_to_dict(e)

    cycle1 = Cycle("Kruskal", original_graph=graph, method='kruskal')
    graph_min = cycle1
    repetitions = xrange(len(geo_points))
    for num_node in repetitions:
        cycle2 = Cycle(
            name="Prim" + str(num_node),
            original_graph=graph,
            method='prim',
            num_node=num_node)
        if graph_min is None or cycle2.weight < graph_min.weight:
            graph_min = cycle2

    print "Longueur totale du cycle etudiant : " + str(graph_min.weight)
    graph_min.plot_graph()

    return graph_min.ordrerd_list

from read_stsp import read_edges
from read_stsp import read_header
from read_stsp import read_nodes
from graph import Graph


if __name__ == "__main__":

    import sys

    finstance = sys.argv[1]
    G = Graph()
    with open(finstance, "r") as fd:

        header = read_header(fd)
        print 'Header: ', header
        dim = header['DIMENSION']
        edge_weight_format = header['EDGE_WEIGHT_FORMAT']

        print "Reading nodes"
        nodes = read_nodes(header, fd, G)

        print "Reading edges"
        edges = read_edges(header, fd, G)

    # G.plot_graph()
    #print (G)

    G_arb = Graph()
    for node in G.get_nodes():
        G_arb.add_node(node)
    list_edges = G.get_edges()
    ordered_weight_list = []
    for edge in list_edges:
        weight, edge = edge.weight, edge
        ordered_weight_list.append((weight,edge))
    ordered_weight_list.sort()

    # i = -1
    # connex_graph = []
    # arborescence = []
    # for weight,edge in ordered_weight_list:
    #     if (edge.start or edge.end) not in connex_graph:
    #         connex_graph.append(edge.start)
    #         connex_graph.append(edge.end)
    #         arborescence.append(edge)

    id_cg = 0
    dico = {}
    dico["connex_graph", str(id_cg)] = []
    arborescence = []
    num_elt = 0
    connexion = []

    for weight,edge in ordered_weight_list:
        if num_elt == 0:
            dico["connex_graph", str(id_cg)].append(edge.start)
            dico["connex_graph", str(id_cg)].append(edge.end)
            arborescence.append(edge)
            num_elt += 1
            continue

        i, k = 0, 0
        # print i,k
        cycle = False
        while i <= id_cg:
            if (edge.start and edge.end) in dico["connex_graph", str(i)]:
                cycle = True
                break
            elif (edge.start or edge.end) in dico["connex_graph", str(i)]:
                k = i+1
                while k <= id_cg:
                    print "hello"
                    if (edge.start or edge.end) in dico["connex_graph", str(k)]:
                        print "hello2"
                        if ( (i, k) or (k, i) ) in connexion:
                            cycle = True
                            break
                        connexion.append((i,k))
                    k += 1
                if not cycle:
                    dico["connex_graph", str(i)].append(edge.start)
                    dico["connex_graph", str(i)].append(edge.end)
                    arborescence.append(edge)
                    break
            # elif (not cycle and i == id_cg) :
            #     id_cg += 1
            #     dico["connex_graph", str(id_cg)] = []
            #     dico["connex_graph", str(id_cg)].append(edge.start)
            #     dico["connex_graph", str(id_cg)].append(edge.end)
            #     arborescence.append(edge)
            i += 1

        # if cycle == False :
        #     arborescence.append(edge)



            #
            # if (edge.start or edge.end) not in dico["connex_graph", str(i)]:
            #     dico["connex_graph", str(i)].append(edge.start)
            #     dico["connex_graph", str(i)].append(edge.end)
            #     if id_cg = 0:
            #         arborescence.append(edge)

    # print arborescence

    # from copy import copy
    # G_arb = copy(G)
    # i = -1
    # for elt in G_arb.get_edges():
    #     i += 1
    #     if elt not in arborescence:
    #         print "ok!"
    #         del G_arb.get_edge(i)
    #

    # G_arb.plot_graph()


    for edge in arborescence :
        G_arb.add_edge(edge)

    print G_arb.get_edges()
    print G_arb.get_nodes()
    G_arb.plot_graph()


    # for elt in arborescence:
    #     G_arb.add_edge(elt)
    # G_arb.plot_graph()
    # print G_arb

    # # i = 0
    # while i<len(arborescence)
    #     if G_arb =
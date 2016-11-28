#!/bin/bash

rm -r htmlcov/
coverage erase
coverage run -a edge.py
coverage run -a graph.py
coverage run -a node.py
coverage run -a wline.py
coverage run -a cycle.py
coverage run -a test_edge.py
coverage run -a test_node.py
coverage run -a test_graph.py
coverage run -a test_mst.py
coverage run -a test_wline.py

coverage run -a read_stsp.py instances/instances/stsp/bayg29.tsp 
coverage run -a read_stsp.py instances/instances/stsp/dantzig42.tsp 
coverage run -a read_stsp.py instances/instances/stsp/gr21.tsp 
coverage run -a read_stsp.py instances/instances/stsp/pa561.tsp 
coverage run -a read_stsp.py instances/instances/stsp/bays29.tsp 
coverage run -a read_stsp.py instances/instances/stsp/fri26.tsp 
coverage run -a read_stsp.py instances/instances/stsp/gr24.tsp 
coverage run -a read_stsp.py instances/instances/stsp/swiss42.tsp 
coverage run -a read_stsp.py instances/instances/stsp/brazil58.tsp 
coverage run -a read_stsp.py instances/instances/stsp/gr120.tsp 
coverage run -a read_stsp.py instances/instances/stsp/gr48.tsp 
coverage run -a read_stsp.py instances/instances/stsp/Test_full_matrix.tsp 
coverage run -a read_stsp.py instances/instances/stsp/brg180.tsp 
coverage run -a read_stsp.py instances/instances/stsp/gr17.tsp 
coverage run -a read_stsp.py instances/instances/stsp/hk48.tsp 
coverage run -a read_stsp.py instances/instances/stsp/Test_lower_diag_row.tsp
coverage run -a read_stsp.py instances/instances/stsp/Test_lower_row.tsp
coverage run -a read_stsp.py instances/instances/stsp/Test_upper_diag_row.tsp
coverage run -a test_read_stsp.py instances/instances/stsp/Test_lower_row.tsp
coverage run -a test_read_stsp.py instances/instances/stsp/Test_upper_diag_row.tsp

coverage run -a main.py instances/instances/stsp/gr120.tsp prim
coverage run -a main.py instances/instances/stsp/brazil58.tsp prim
coverage run -a main.py instances/instances/stsp/swiss42.tsp prim
coverage run -a main.py instances/instances/stsp/hk48.tsp prim
coverage run -a main.py instances/instances/stsp/gr48.tsp prim
coverage run -a main.py instances/instances/stsp/dantzig42.tsp prim
coverage run -a main.py instances/instances/stsp/bays29.tsp prim
coverage run -a main.py instances/instances/stsp/bayg29.tsp prim
coverage run -a main.py instances/instances/stsp/gr21.tsp prim
coverage run -a main.py instances/instances/stsp/fri26.tsp prim
coverage run -a main.py instances/instances/stsp/gr24.tsp prim
coverage run -a main.py instances/instances/stsp/Test_full_matrix.tsp prim
coverage run -a main.py instances/instances/stsp/gr17.tsp prim
coverage run -a main.py instances/instances/stsp/KruskalGraph.tsp prim
coverage run -a main.py instances/instances/stsp/Test_lower_row.tsp prim
coverage run -a main.py instances/instances/stsp/Test_upper_diag_row.tsp prim
coverage run -a main.py instances/instances/stsp/Test_lower_diag_row.tsp prim



coverage run -a main.py instances/instances/stsp/gr120.tsp kruskal
coverage run -a main.py instances/instances/stsp/brazil58.tsp kruskal
coverage run -a main.py instances/instances/stsp/swiss42.tsp kruskal
coverage run -a main.py instances/instances/stsp/hk48.tsp kruskal
coverage run -a main.py instances/instances/stsp/gr48.tsp kruskal
coverage run -a main.py instances/instances/stsp/dantzig42.tsp kruskal
coverage run -a main.py instances/instances/stsp/bays29.tsp kruskal
coverage run -a main.py instances/instances/stsp/bayg29.tsp kruskal
coverage run -a main.py instances/instances/stsp/gr21.tsp kruskal
coverage run -a main.py instances/instances/stsp/fri26.tsp kruskal
coverage run -a main.py instances/instances/stsp/gr24.tsp kruskal
coverage run -a main.py instances/instances/stsp/Test_full_matrix.tsp kruskal
coverage run -a main.py instances/instances/stsp/gr17.tsp kruskal
coverage run -a main.py instances/instances/stsp/KruskalGraph.tsp kruskal
coverage run -a main.py instances/instances/stsp/Test_lower_row.tsp kruskal
coverage run -a main.py instances/instances/stsp/Test_upper_diag_row.tsp kruskal
coverage run -a main.py instances/instances/stsp/Test_lower_diag_row.tsp kruskal


coverage report -m wline.py cycle.py node.py main.py mst.py graph.py edge.py test_read_stsp.py read_stsp.py test_edge.py  test_node.py test_graph.py 
coverage html wline.py cycle.py node.py main.py mst.py graph.py edge.py test_read_stsp.py read_stsp.py test_edge.py  test_node.py test_graph.py 

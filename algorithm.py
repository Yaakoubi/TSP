# -*- coding: utf-8 -*-

from node2 import Node


class Algorithm(object):
    """
    Une classe pour lancer l'éxecution de l'algorithme sum-product
    """
    def __init__(self):
        """initialise les noeuds et remplit la matrice des probabilités"""
        c_node = Node(1, None, [0.999, 0.001], "C")
        t_node = Node(2, None, [0.998, 0.002], "T")
        a_node = Node(3, [t_node, c_node], [0.999, 0.06,
                                            0.71, 0.05, 0.001, 0.94, 0.29, 0.95], "A")
        m_node = Node(4, [a_node], [0.95, 0.1, 0.05, 0.9], "M")
        j_node = Node(5, [a_node], [0.99, 0.3, 0.01, 0.7], "J")
        self.__Nodes = [c_node, t_node, a_node, m_node, j_node]
        self.__Dict = {'C': 0, 'T': 1, 'A': 2, 'M': 3, 'J': 4}

    def calcul(self, variable, valeur, tab1):
        """lance le calcul pour l'algo de sum-product"""
        prob_dict = {}
        for couple in tab1:
            var = couple[0]
            val = couple[1]
            prob_dict[var] = val
        prob_dict[variable] = valeur
        return self.parcours("C", prob_dict)

    def next_of_kin(self, var):
        """retourne l'élement suivant à traiter dans la liste des noeuds"""
        if var is not None:
            indice = self.__Dict[var] + 1
            if indice < len(self.__Nodes):
                return self.__Nodes[indice].get_name()
        return None

    def get_probability(self, var, local_dict, boo):
        """cherche une probabilité dans la matrice de données"""
        node = self.__Nodes[self.__Dict[var]]
        fathers = node.fathers
        chaine = boo
        for parent in fathers:
            chaine += repr(local_dict[parent.get_name()])
        return node.direct_prob(chaine)

    def parcours(self, var, var_connues):
        """fonction récursive qui cherche la formule de l'algo sum-product"""
        if var is not None:
            next_of_kin = self.next_of_kin(var)
            # print "var = " + repr(var) + "  " + repr (varConnues.get(var))
            val = var_connues.get(var)
            if val is not None:
                proba_tempo = self.get_probability(var, var_connues, repr(val))
                if next_of_kin is not None:
                    return proba_tempo * \
                        self.parcours(next_of_kin, var_connues)
                else:
                    return proba_tempo
            else:
                prob_dict1 = var_connues.copy()
                prob_dict1[var] = 1
                prob_dict2 = var_connues.copy()
                prob_dict2[var] = 0
                # print "probDict = " + repr(probDict2)
                prob1 = self.get_probability(var, prob_dict1, "1")
                prob2 = self.get_probability(var, prob_dict2, "0")
                if next_of_kin is not None:
                    return prob1 * self.parcours(next_of_kin, prob_dict1) + \
                        prob2 * self.parcours(next_of_kin, prob_dict2)
                else:
                    return 1


if __name__ == '__main__':
    Al = Algorithm()
    print "----Debut Algo----"
    print " p(C = 1) = " + "%.3f" % (Al.calcul("C", 1, []))
    print " p(T = 0) = " + "%.3f" % (Al.calcul("T", 0, []))
    print " p(A = 1) = " + "%.3f" % (Al.calcul("A", 1, []))
    print " p(M = 0) = " + "%.3f" % (Al.calcul("M", 0, []))
    print " p(J = 1) = " + "%.3f" % (Al.calcul("J", 1, []))
    print " p(C = 1 , A = 1) = " + "%.3f" % (Al.calcul("C", 1, [["A", 1]]))
    print " p(C = 0 , J = 0) = " + "%.3f" % (Al.calcul("C", 0, [["J", 0]]))
    print " p(M = 1 , A = 1) = " + "%.3f" % (Al.calcul("M", 1, [["A", 1]]))
    print " p(M = 1 | A = 1) = " + "%.3f" % (Al.calcul("M", 1, [["A", 1]]) / Al.calcul("A", 1, []))
    print " p(A = 1 | C = 1 , T = 0) = " + "%.3f" % \
                                           (Al.calcul("A", 1, [["C", 1], ["T", 0]]) / Al.calcul("C", 1, [["T", 0]]))

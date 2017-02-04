# -*- coding: utf-8 -*-


class Node(object):
    """
    Une classe pour representer les noeuds d'un graphe.
    """

    __fathers = []
    __self_probs = []

    def __init__(self, node_id, fathers, probs, name='Sans nom',):
        self.__name = name
        self.__id = node_id
        if fathers is not None:
            self.__fathers = fathers
        else:
            self.__fathers = []
        if probs is not None:
            if len(probs) == 2**(len(self.__fathers) + 1):
                self.__self_probs = probs

    def get_name(self):
        """"Donne le nom du noeud."""
        return self.__name

    def get_id(self):
        """Donne le numero d'identification du noeud."""
        return self.__id

    def __repr__(self):
        indice = self.get_id()
        name = self.get_name()
        s = 'Noeud {0!s} (id {1:d})'.format(name, indice) + ')'
        return s

    @property
    def fathers(self):
        if self.__fathers is not None:
            return self.__fathers
        return self

    @property
    def probs(self):
        if self.__self_probs is not None:
            return self.__self_probs
        return self

    @fathers.setter
    def fathers(self, fathers):
        """This allows the node's fathers to be set"""
        if fathers is not None:
            self.__fathers = fathers

    def direct_prob(self, bin_value):
        """cherche une probabilité directement dans la matrice des probabilités"""
        if bin_value is not None:
            return self.__self_probs[self.bin2dec(bin_value)]
        return None

    @staticmethod
    def bin2dec(string):
        """convertit une valeur binaire en décimal"""
        result = 0
        for car in string:
            result *= 2
            if car == '1':
                result += 1
            elif car == '0':
                pass
            else:
                return None
        return result


if __name__ == '__main__':

    C = Node(1, None, [0.999, 0.001], "C")
    T = Node(2, None, [0.998, 0.002], "T")
    A = Node(3, [T, C], [0.999, 0.06, 0.71,
                         0.05, 0.001, 0.94, 0.29, 0.95], "A")
    M = Node(4, [A], [0.95, 0.1, 0.05, 0.9], "M")
    J = Node(5, [A], [0.99, 0.3, 0.01, 0.7], "J")

    print " --- Verification de l'implémentation initale --- "

    print " p(C = 1 ) = " + repr(C.direct_prob("1"))
    print " p(A = 1 | T = 1 , C = 1 ) = " + repr(A.direct_prob("111"))
    print " p(A = 1 | T = 0 , C = 1 ) = " + repr(A.direct_prob("101"))
    print " p(A = 1 | T = 0 , C = 0 ) = " + repr(A.direct_prob("100"))
    print " p(A = 0 | T = 1 , C = 0 ) = " + repr(A.direct_prob("010"))
    print " p(M = 1 | A = 0 ) = " + repr(M.direct_prob("10"))
    print " p(J = 1 | A = 0 ) = " + repr(J.direct_prob("10"))
    print " p(T = 0 ) = " + repr(T.direct_prob("0"))

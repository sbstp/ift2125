# Write your names here :
# Student 1 : Gabriel Lemyre
# Student 2 : Simon Bernier St-Pierre

import numpy as np
import random

# DO NOT write anything oustide functions and main (except imports)
# DO NOT call main()
# DO NOT change the methods names
# Please remove all the print functions used for debugging purposes
# Please maintain an average of +-80 characters by line >..........>.............>..............>..............>..............>................>......not like this
# Please change the filename according to your names
# Submit **only*** this file on Studium, NOT a .zip, NOT a full folder
# Remaining of the homework needs to be handed (in paper) before the demo.


def random_graph(n, m):
    # Input : size n, m
    # Output : matrice representant A[i][j] = 1 ssi S_i contient l'element j

    # A completer...
    # Look at Demo5 for inspiration on how to use random package
    A = np.zeros((n, m))  # need to create the nxm boolean array here
    for i in range(n):
        for j in range(m):
            A[i][j] = random.randint(0, 1)

    return A


def intersection(A):  # O(n * m)
    n, m = A.shape
    S = set()
    for i in range(n):  # for each set
        Si = set(j for j in range(m) if A[i][j])  # O(m)
        if len(Si) == 0:  # https://studium.umontreal.ca/mod/forum/discuss.php?d=519988#p980016
            return set()
        for v in S:
            # check if any number in Si is in S
            if v in Si:
                break
        else:
            # no element of Si is in S, add any element to it
            if len(Si) > 0:
                S.add(next(iter(Si)))
        assert any(v in S for v in Si)  # just making sure
    return S


def experiment(n, m, nb_experiments):
    # Cette fonction doit rester exactement comme ceci
    # Do not change anything here
    size_of_S = []
    for exp in range(nb_experiments):
        A = random_graph(n, m)
        S = intersection(A)
        size_of_S.append(len(S))
    return size_of_S


if __name__ == "__main__":  # main() will only be called when using "python file.py"
    # Rien d'autre ne doit etre necessaire dans le main pour retourner moyenne/std
    # Nothing else should go there when you submit your code, do not change anything
    n = 20  # ensembles
    m = 100  # nombres
    k = 50

    size_of_S = experiment(n, m, k)
    # Ceci devrait vous donner la moyenne et ecart-type
    print("mean", np.mean(size_of_S), "std", np.std(size_of_S))

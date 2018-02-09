# Gabriel Lemyre
# Simon Bernier St-Pierre
# utf8, LF

from multiprocessing import Process
import exemplaires


def is_perm(p):
    """
    S'assure que la permuation est valide. Chaque valeur doit être unique et inférieure ou égale aux nombre d'éléments.
    """
    return all(x <= len(p) for x in p) and len(p) == len(set(p))


def check_perms(**kwargs):
    """
    S'assure que toute les permutations sont de même taille et qu'elle sont valides.
    """
    if len(set(len(p) for p in kwargs.values())) > 1:
        raise ValueError("Les permutations ne sont pas de même longeur")
    for name, val in kwargs.items():
        if not is_perm(val):
            raise ValueError("Erreur, {}={} n'est pas une permutation".format(name, val))


def prod(p1, p2):
    """
    Effectue le produit de permutations.
    """
    r = [0] * len(p1)
    for idx, val in enumerate(p1):
        r[idx] = p2[val - 1]
    return tuple(r)


def perm2(k, p, p1, p2):
    """
    Utilise une méthode bête récursive/exponentielle pour tester chaque combinaison de permutations.
    Si on atteint la limite k, on arrête avec False.
    Si on obtient un produit qui fonctionne, on arrête avec True
    Sinon on continue à chercher avec k-1 et l'option p1/p2
    """
    check_perms(p=p, p1=p1, p2=p2)

    def rec(k, c):
        if k < 0:
            return False
        if p == c:
            return True
        return rec(k - 1, prod(c, p1)) or rec(k - 1, prod(c, p2))
    return rec(k - 1, p1) or rec(k - 1, p2)


# test with pytest

def test_prod():
    p = (2, 4, 1, 3, 5)
    q = (5, 4, 3, 2, 1)
    assert prod(p, q) == (4, 2, 5, 3, 1)


def test_is_perm():
    assert is_perm((1, 3, 2))
    assert not is_perm((3, 1, 1))
    assert not is_perm((3, 2))


TIMEOUT = 60  # in seconds

input_set = vars(exemplaires)
for i in range(1, 8):
    # little hack to grab all the input sets
    k = input_set['k%d' % i]
    p = input_set['p%d' % i]
    p1 = input_set['p1%d' % i]
    p2 = input_set['p2%d' % i]

    def runner(k, p, p1, p2):
        try:
            v = perm2(k, p, p1, p2)
            print(i, v)
        except ValueError as e:
            print(i, str(e))

    # use a process to timeout on sets that take too much time
    t = Process(target=runner, args=(k, p, p1, p2))
    t.start()
    t.join(TIMEOUT)
    if t.is_alive():
        print(i, 'Timed out')
        t.terminate()

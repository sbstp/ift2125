#!/usr/bin/env python3
# -*- coding: utf8 -*-


def split(A, n):
    """
    Divise A en exactement n sous-listes. Si il n'est pas possible
    de diviser en n sous-listes égales, le surplus est redistribué
    dans les premières listes.
    """
    p = len(A)//n
    m = len(A) % n
    for i in range(n):
        idx = p + 1 if i < m else p
        chunk = A[:idx]
        if len(chunk) == 0:
            break
        yield chunk
        A = A[idx:]


def mergesort4(A):
    """
    Effectue un mergesort and divisant en 4 sous-listes.
    """
    n = len(A)
    if n == 1:
        return A
    # créer une liste de paires (index, chunk)
    # chunk est un morceaux de la liste A, environ 1/4
    # index est la position dans la chunk qui lui est associée
    chunks = [[0, mergesort4(chunk)] for chunk in split(A, 4)]

    result = [0] * n
    for k in range(n):
        # ici on sélectionne la valeur à la position de chaque chunk,
        # parmis les chunks qui ont toujours des valeurs disponibles
        candidates = [(ref, chunk[index]) for ref, (index, chunk)
                      in enumerate(chunks) if index < len(chunk)]
        # ici on choisi la valeur la plus basse parmis les candidats
        ref, val = min(candidates, key=lambda pair: pair[1])
        # ici on modifie l'index associé à la valeur choisie
        chunks[ref][0] += 1
        # on assigne la valeur au tableau résultat
        result[k] = val

    return result


import random
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(numbers)
print(numbers)
print(mergesort4(numbers))

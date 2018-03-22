# IFT 2125 : Devoir 3
# Etudiant 1 :
# Etudiant 2 :

import numpy as np
from math import ceil

# DO NOT write anything outside functions and main (except imports)
# DO NOT call main()
# DO NOT change the methods names
# Please remove all the print functions used for debugging purposes
# Please change the filename according to your names
# Submit **only*** this file on Studium, NOT a .zip, NOT a full folder
# Remaining of the homework needs to be handed (in paper) before the demo.


def merge(A, B):
    A = mergesort4(A)
    B = mergesort4(B)
    nA = len(A)
    nB = len(B)
    iA = 0
    iB = 0
    r = []
    while True:
        if iA < nA and iB < nB:  # A and B still have elements
            if A[iA] < B[iB]:
                r.append(A[iA])
                iA += 1
            else:
                r.append(B[iB])
                iB += 1
        elif iA < nA:  # B is done
            r.append(A[iA])
            iA += 1
        elif iB < nB:  # A is done
            r.append(B[iB])
            iB += 1
        else:  # A and B are done, lists are sorted.
            break
    return r


def split(A):
    n = len(A)
    half = ceil(n / 2)
    return A[:half], A[half:]


def mergesort4(A, n=0):
    n = len(A)
    if n <= 1:
        return A
    else:
        A1, A2 = split(A)
        return merge(merge(*split(A1)),
                     merge(*split(A2)))


# Your code will be tested using tests similar to these ones.
# Be sure that it does not yield any error and that the two given tests give "True".
if __name__ == "__main__":

    A = [2, 2, 1, 0, 4, -1, -12, 14]
    print("Array : ", A)
    test1 = mergesort4(A, len(A)) == sorted(A)
    print("correctly sorted?", test1)

    B = np.random.randint(low=0, high=100, size=(20))
    print("Array : ", B)
    test2 = mergesort4(B, len(B)) == sorted(B)
    print("correctly sorted?", test2)

    print("Votre note serait =", np.mean([test1, test2])*100, "%")

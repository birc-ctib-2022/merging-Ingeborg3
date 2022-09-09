"""Code for merging two sorted lists."""


def merge(x: list[int], y: list[int]) -> list[int]:
    """
    Merge two sorted lists.

    Returns a list that contains all the elements in x and y
    in sorted order.

    >>> merge([1, 2, 4, 6], [1, 3, 4, 5])
    [1, 1, 2, 3, 4, 4, 5, 6]
    """
    z = []
    i, j = 0,0
    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            z.append(x[i])
            i += 1
        else: 
            z.append(y[j])
            j += 1
    if i == len(x): # all elements of x added to z.
        for n in y[j:]:
            z.append(n)
    if j == len(y): 
        # all elements of y added to z.
        for n in x[i:]:
            z.append(n)
    return z
# Kan også gøres som funktion p. 140. 

def remove_from_tuple(tup, elem):
    if elem not in tup:
        return tup
    else:
        new_tup = list(tup)
        new_tup.remove(elem)
        return tuple(new_tup)

print(remove_from_tuple((1, 2, 3), 1))  # (2, 3)
print(remove_from_tuple((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))  # (1, 2, 1, 2, 4, 5, 2, 3, 4, 2, 4, 2)
print(remove_from_tuple((2, 4, 6, 6, 4, 2), 9))  # (2, 4, 6, 6, 4, 2)
def get_sequence(tup, element):
    first_idx = tup.index(element) if element in tup else None
    if first_idx is None:
        return ()
    try:
        second_idx = tup.index(element, first_idx + 1)
    except ValueError:
        second_idx = None
    if second_idx is None:
        return tup[first_idx:]
    return tup[first_idx:second_idx + 1]


print(get_sequence((1, 2, 3), 8))
print(get_sequence((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(get_sequence((1, 2, 8, 5, 1, 2, 9), 8))
from collections import Counter

def create_sets(lists):
    result_sets = []
    for lst in lists:
        result_set = set()
        count_dict = Counter(lst)
        for num, freq in count_dict.items():
            if freq == 1:
                result_set.add(num)
            else:
                result_set.add(str(num) * freq)
        result_sets.append(result_set)
    return result_sets

list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

result_sets = create_sets([list_1, list_2, list_3])
for result_set in result_sets:
    print(result_set)

def calculate_structure_sum(*args):
    summ = 0
    for item in args:
        if isinstance(item, list):
            for element in item:
                summ += calculate_structure_sum(element)
        elif isinstance(item, tuple):
            for element in item:
                summ += calculate_structure_sum(element)
        elif isinstance(item, set):
            for element in item:
                summ += calculate_structure_sum(element)
        elif isinstance(item, dict):
            for key, value in item.items():
                summ += calculate_structure_sum(key, value)
        elif isinstance(item, str):
            summ += len(item)
        elif isinstance(item, int):
            summ += item
    return summ


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
def print_params(a = 1, b = "String", c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [23, "Gamer", True]
values_dict = {"a": "Key", "b": True, "c": 1}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']

print_params(*values_list_2, 42)
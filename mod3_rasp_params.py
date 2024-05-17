def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params()

def print_params(*params):
    print(params)
print_params(1, 2, 3, 4, 5, 6, 7)

def print_params():
    print("Hi")
print_params()

def print_params(b='строка'):
    print(b)
print_params(b=25)

def print_params(c=True):
    print(c)
print_params(c=[1, 2, 3])

def print_params(a, b, c):
    print(a, b, c)
values_list = [1, "Hello", False]
values_dict = {'a': 1,  'b': True,  'c': 3.3}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ["OK", 5]
print_params(*values_list_2, 42)
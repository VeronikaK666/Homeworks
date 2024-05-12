import random
def print_params():
    numbers_ = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
    result_ = random.choice(numbers_)
    return result_, result_
result_ = print_params()
print(result_)

def print_params(numbers_):
    print('it is', numbers_)
print_params('1')
print_params('2')



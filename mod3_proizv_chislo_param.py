#DOMASHKA!!!

def test(*args):
    print(f'first position: {args[0]}, second position: {args[1]}, last position: {args[-1]}')
test('peach', (3, 4, 5), 'watermelon', 6, 'orange', 'apple', [1, 2])

def test(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
test(cat='Barsik', dog='Rex')

def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n * factorial_recursive(n - 1)


print(factorial_recursive(4))

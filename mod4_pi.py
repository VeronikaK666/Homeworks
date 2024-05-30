def test_function(x):
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function() #Process finished with exit code 0
test_function(0) #Я в области видимости функции test_function

#inner_function() - Ошибка: name 'inner_function' is not defined



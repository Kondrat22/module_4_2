def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()  # так просто не вызывает


# inner_function()  # так возникает ошибка

test_function()

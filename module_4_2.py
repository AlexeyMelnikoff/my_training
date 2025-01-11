def test_function ():
    def inner_function ():
        print("Я в области видимости функции test_function")
    inner_function()

#inner_function() #Дает ошибку, т.к. данная функция работает только внутри функции test_function
test_function ()
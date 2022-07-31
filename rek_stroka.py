def get_numbers2(source, position=0):
    if not (len(source) - position > 0):
        return

# на входе в рекурсию печатаем цифры
    if source[position].isnumeric():
        print(source[position], end='')
    get_numbers2(source, position + 1)
# на выходе из рекурсии печатаем остальные символы
    if not source[position].isnumeric():
        print(source[position], end='')


stroka = 'hdf736239jnfbvsk'
get_numbers2(stroka)

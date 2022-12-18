def convert_to_num(alpha):
    if alpha in 'аисъАИСЪ':
        return 1
    if alpha in 'бйтыБЙТЫ':
        return 2
    if alpha in 'вкуьВКУЬ':
        return 3
    if alpha in 'глфэГЛФЭ':
        return 4
    if alpha in 'дмхюДМХЮ':
        return 5
    if alpha in 'енцяЕНЦЯ':
        return 6
    if alpha in 'ёочЁОЧ':
        return 7
    if alpha in 'жпшЖПШ':
        return 8
    if alpha in 'зрщЗРЩ':
        return 9
    return 'введено неправильное слово '

def get_num_of_city(place):
    len_of_city = len(place)
    summa = 0
    for i in range(len(place)):
        summa += convert_to_num(place[i])
    while summa > 22:
        summa -= 22
    return summa

print(get_num_of_city('москва'))
print(get_num_of_city('екатеринбург'))
print(get_num_of_city(''))

def get_num_of_birthday(birthday):
    summa = 0
    for i in range(len(birthday)):
        if birthday[i] in '123456789':
            summa += int(birthday[i])
    while summa > 22:
        summa -= 22
    return summa

print(get_num_of_birthday('30.10.1999'))
print(get_num_of_birthday('12/09/1981'))

def get_main_num(paramert, birthday):
    num1 = get_num_of_city(paramert)
    num2 = get_num_of_birthday(birthday)
    summa = num1 + num2
    while summa > 22:
        summa -= 22
    return summa


print(get_main_num('Екатеринбург', '12.09.1981'))






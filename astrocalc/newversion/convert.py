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
    return 0

def get_num_of_place(place):
    len_of_city = len(place)
    summa = 0
    for i in range(len(place)):
        if convert_to_num(place[i]) != 0:
            summa += convert_to_num(place[i])
        else:
            return False
    while summa > 22:
        summa -= 22
    return summa



def get_num_of_birthday(birthday):
    summa = 0
    for i in range(len(str(birthday))):
        if str(birthday)[i] in '123456789':
            summa += int(str(birthday)[i])
    while summa > 22:
        summa -= 22
    return summa

print(get_num_of_birthday('30.10.1999'))
print(get_num_of_birthday('12/09/1981'))
print(get_num_of_birthday('01/01/2001'))

def get_main_num(paramert, birthday):
    num1 = get_num_of_place(paramert)
    num2 = get_num_of_birthday(birthday)
    summa = num1 + num2
    while summa > 22:
        summa -= 22
    return summa


print(get_main_num('Екат', '30.10.1999'))






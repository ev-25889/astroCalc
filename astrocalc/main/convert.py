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


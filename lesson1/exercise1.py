duration = int(input('Введите длительность в секунудах: '))

if duration < 60:
    print(duration, ' сек')

elif 60 <= duration < 60 ** 2:
    print(duration//60, ' мин', duration % 60, ' сек')

elif 60 ** 2 <= duration < 24 * 60 ** 2:
    print(duration//60**2, ' час', duration//60%60, ' мин', duration%60, ' сек')

elif 24 * 60**2 <= duration <365 * 24 * 60**2:
    print(duration//60**2//24, ' дн', duration // 60**2%24, ' час', duration//60%60, ' мин',
          duration % 60, ' сек')

elif 365 * 24 * 60**2 <= duration:
    print(duration//365//24//60**2, ' г', duration//60**2//24%365, ' дн', duration//60**2%24,
          ' час', duration//60%60, ' мин', duration%60, ' сек')

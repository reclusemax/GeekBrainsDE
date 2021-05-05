list_of_numbers = [x for x in range(20)]

for num in list_of_numbers:
    if num == 1 or (num%10 == 1 and num > 20):
        print(num, 'процент')
    elif 1 < num < 5 or (1 < num%10 < 5 and num > 20):
        print(num, ' процента')
    else:
        print(num, ' процентов')

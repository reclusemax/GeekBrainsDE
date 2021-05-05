list_of_numbers = [i**3 for i in range(1000) if i%2]

#Пункт A
sum = 0
for num in list_of_numbers:
    sum_of_digit =0
    for i in str(num):
        sum_of_digit +=int(i)
    if not sum_of_digit%7:
        sum += num
print(sum)

#Бункт B(C)
sum = 0
for num in map(lambda x: x + 17, list_of_numbers):
    sum_of_digit = 0
    for i in str(num):
        sum_of_digit += int(i)
    if not sum_of_digit%7:
        sum += num
print(sum)

n = int(input('Введите номер месяца:')) # номер 1

z = {1, 2, 12}
v = {4, 5, 3}
o = {11, 9, 10}
l = {6, 7, 8}

if n in z: print('Зима.')
elif n in v: print('Весна.')
elif n in o: print('Осень.')
elif n in l: print('Лето.')
    
else: print('Неверный номер месяца.')

#################################################

age = int(input('Введите возраст:'))    #номер 2
word = 'лет'

if age%10 == 1: word = 'год'
elif age%10 in range(2,5): word = 'года'

print('Вам',age,word)
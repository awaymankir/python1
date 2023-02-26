
# Задача №2

n = input("Введите трехзначное число: ")
 
a = int(n[0])
b = int(n[1])
c = int(n[2])
 
print("Сумма цифр числа:", a + b + c)

#задача №4

s = int(input("Введите число"))

print((s//6), ((s//6)*4), (s//6))

# Задача №6

number = str(input('введите номер билета: '))
ticket = [int(x) for x in number]
middle = len(ticket) // 2

if sum(ticket[0:middle]) == sum(ticket[middle:]):
print('YES')
else:
print('NO')

# Задача 8


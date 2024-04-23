# ex 1
x = 2
print(x, type(x))

x += 3
print(x, type(x))

x = (x + 1) / 2
print(x, type(x))

x = x + 1 / 2
print(x, type(x))

x = x < 5
print(x, type(x))

x = str(x)
print(x, type(x))

# ex 2

summa = 1 + 2 + 3 + 4 + 5
average = summa / 5
print("Среднее значение этих 5 чисел равно:", "{:.5f}".format(average))

# ex 3

summa = 1 + 2 + 3 + 4 + 5
count = 5
average = summa / count
print("Среднее значение этих 5 чисел равно:", "{:.5f}".format(average))
while True:
    number = (int(input("Введите число ")))
    if number == 0:
        break
    summa += number
    count += 1
    average = summa / count
    print( f'Среднее значение этих {count} чисел равно:{average:.5f}')

# доп задание 1
import math
import matplotlib.pyplot as plt
import numpy as np
g = 9.80665
v0 = 5.0
a = 40.0
a = math.radians(a)
h_max = ((v0**2) * (math.sin(a))**2) / (2 * g)
L = ((v0**2) * (math.sin(2 * a))) / g
print("Котик может прыгнуть в высоту : ", "{:.5f}".format(h_max), "в длину :", "{:.5f}".format(L))

def max_distance():
    return 45

def max_height():
    return 90


max_distance = max_distance()
print(f"Для максимальной дальности угол равен: {max_distance} градусов")
max_height = max_height()
print(f"Для максимальной высоты угол равен: {max_height} градусов")

def angleV(x, y, t):
    Vx = x // t
    Vy = y // t
    v = math.sqrt(Vx**2 + Vy**2)
    angle = math.atan((Vy/Vx))
    return math.degrees(angle), v

x = 2
y = 3
t = 1
angle, v = angleV(x, y, t)
print("Для попадания в точку (2,3) м через 1 с, угол должен быть равен:", "{:.5f}".format(angle), " градусов и скорость:",  "{:.5f}".format(v), " м/с")


v0 = 5
a = 40
g = 9.80665

rad = np.radians(a)
time_of_flight = 2 * v0 * np.sin(rad) / g
time = np.linspace(0, time_of_flight, num=100)

x = v0 * np.cos(rad) * time
y = v0 * np.sin(rad) * time - 0.5 * g * time ** 2

plt.figure()
plt.plot(x, y)
plt.title('Траектория прыжка')
plt.grid(True)
plt.show()

# доп задание 2

n = int(input("Введите целое число: "))
summator = sum(int(i) for i in str(n))
print("Сумма цифр числа:", summator)

while len(str(summator)) > 1:
    summator = sum(int(i) for i in str(summator))
    print("Сумма цифр числа: ", summator)

# доп задание 3

list_of_numbers = []

while True:
    n = input("Введите число или нажмите Enter для завершения: ")

    if n == "":
        break

    n = int(n)
    list_of_numbers.append(n)

if list_of_numbers:
    print("Максимальное число: ", max(list_of_numbers))
    print("Минимальное число: ", min(list_of_numbers))
else:
    print('Sorry, ты решил ничего не вводить')

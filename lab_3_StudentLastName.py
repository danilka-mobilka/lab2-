# Завдання № 1
# 1
import math

# Параметри
mu = 0
sigma = 1

# Точка, в якій обчислюємо функцію
x = 1

# Обчислення значення функції Гауса (нормальний розподіл)
f = (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-(x - mu)**2 / (2 * sigma**2))

print(f)

# 2
import math as m

x = 1
mu = 0
sigma = 1

# Основний код (залишається без змін)
f = (1 / (sigma * m.sqrt(2 * m.pi))) * m.exp(- ((x - mu) ** 2) / (2 * sigma ** 2))

print(f"Значення функції Гауса при x={x}, μ={mu}, σ={sigma}: {f:.5f}")

# Додатково можна перевірити для інших значень
test_values = [-2, -1, 0, 1, 2]
print("\nПеревірка для інших значень x:")
for x_val in test_values:
    f_val = (1 / (sigma * m.sqrt(2 * m.pi))) * m.exp(- ((x_val - mu) ** 2) / (2 * sigma ** 2))
    print(f"f({x_val}) = {f_val:.5f}")


# 3
import math

def gauss(x, mu=0, sigma=1):
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(- ((x - mu) ** 2) / (2 * sigma ** 2))

# print(gauss(1))

# print(gauss(1, mu=2, sigma=2))

x = int(input("Уведіть x: "))

print(f"x= {x}: {gauss(x, mu=2, sigma=2):.5f}")


# Завдання № 2

# Ось невелика розповідь:Якось Джон (John) мав три яблука, Мері (Mary) мала п’ять яблук, а Адам (Adam) мав шість яблук. Усі вони були дуже щасливі та жили довго. Кінець історії.

# Створення змінних та надання значень
john = 3
mary = 5
adam = 6

# Виведення змінних в один рядок, розділених комами
print(john, mary, adam, sep=', ')

# Створення змінної totalApple з сумою
totalApple = john + mary + adam

# Виведення значення totalApple
print(totalApple)

# Виведення рядка та цілого числа разом
print("Загальна кількість яблук:", totalApple)

#Завдання № 3
# Вихідний код
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#Завдання №4
#3x³ - 2x² + 3x - 1
# Зчитуємо значення x з клавіатури
x = float(input("Введіть значення x: "))

# Обчислюємо значення виразу: 3x³ - 2x² + 3x - 1
result = 3*x**3 - 2*x**2 + 3*x - 1

# Виводимо результат
print(f"Значення виразу 3x³ - 2x² + 3x - 1 при x = {x} дорівнює: {result}")

#Завдання №5
# Код редактора містить коментарі. Спробуйте покращити його: додайте або видаліть коментарі там, де ви вважаєте це доречним (так, іноді видалення коментаря може зробити код більш читабельним) і змініть імена змінних там, де, на вашу думку, це покращить розуміння коду.
# this program computes the number of seconds in a given number of hours
# this program has been written two days ago

a = 2 # number of hours
seconds = 3600 # number of seconds in 1 hour

print("Hours: ", a) #printing the number of hours
print("Seconds in Hours: ", a * seconds) # printing the number of seconds in a given number of hours

#here we should also print "Goodbye", but a programmer didn't have time to write any code
print("Goodbye")

#this is the end of the program that computes the number of seconds in 3 hour


#Завдання №6
#Завершити код, щоб отримати результати чотирьох основних арифметичних операцій.
# input a float value for variable a here
a = float(input("Введіть число a: "))

# input a float value for variable b here
b = float(input("Введіть число b: "))

# output the result of addition here
print(f"{a} + {b} = {a + b}")

# output the result of subtraction here
print(f"{a} - {b} = {a - b}")

# output the result of multiplication here
print(f"{a} * {b} = {a * b}")

# output the result of division here
if b != 0:
    print(f"{a} / {b} = {a / b}")
else:
    print("Ділення на нуль неможливе!")

print("\nThat's all, folks!")
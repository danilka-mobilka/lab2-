#1 Zminyty kod prohramy, shchoby ochykuvanyy rezultat vyhlyadav nastupnym chynom:
print("Programming", "Essential", "in")
print("Python")
print("Programming***Essentials***in...Python")

#3 Vyvesty na ekran nastupnyy ryadok:
print ("I'm student")

# Завдання 5: перевести 500 з десяткової в сімкову
num1 = 500
result1 = ""
n = num1
while n > 0:
    result1 = str(n % 7) + result1
    n //= 7
print(f"500 у сімковій системі: {result1}")

# Завдання 6: перевести 77716 з десяткової в сімкову
num2 = 77716
result2 = ""
n = num2
while n > 0:
    result2 = str(n % 7) + result2
    n //= 7
print(f"77716 у сімковій системі: {result2}")



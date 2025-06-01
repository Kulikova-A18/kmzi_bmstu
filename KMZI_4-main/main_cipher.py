# --------- start print ------------
def print_gcd(a, b):
    print(f"\nФункция для нахождения НОД({a},{b})")
    while b != 0:
        print(f'{a} = {a//b} * {b} + {a%b}')
        a, b = b, a % b
# --------- end print ------------

# Функция для вычисления НОД и обратного элемента
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    print(f"{y1} - ({b} / {a}) * {x1} = ")
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi):
    print_gcd(e, phi)
    print()
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("Обратного элемента не существует")
    else:
        print(f"=> обратный элемент = {x} mod {phi}={x % phi}")
        return x % phi

# Функция для вычисления модульного возведения в степень
def modular_exponentiation(base, exponent, modulus):
    result = 1
    print(f"{base} mod {modulus} = {base % modulus}")
    base = base % modulus
    while exponent > 0:
        if (exponent % 2) == 1:  # Если exponent нечетный
            print(f"(e нечетный тогда) e mod 2 = {exponent} mod 2 = {exponent % 2} => ({result} * {base}) mod {modulus} = {(result * base) % modulus} ")
            result = (result * base) % modulus
        exponent = exponent >> 1  # Делим exponent на 2
        print(f"e = {exponent} / 2 = { exponent >> 1}")
        if(exponent != 0):
            print(f"c = {base}^2 mod {modulus} = {base * base} mod {modulus} = {(base * base) % modulus}")
        base = (base * base) % modulus
    return result

def modular_exponentiation2(base, exponent, modulus):
    result = 1
    print(f"{base} mod {modulus} = {base % modulus}")
    base = base % modulus
    while exponent > 0:
        if (exponent % 2) == 1:  # Если exponent нечетный
            print(f"(d нечетный тогда) d mod 2 = {exponent} mod 2 = {exponent % 2} => ({result} * {base}) mod {modulus} = {(result * base) % modulus}")
            result = (result * base) % modulus
        exponent = exponent >> 1  # Делим exponent на 2
        print(f"d = {exponent} / 2 = { exponent >> 1}")
        if(exponent != 0):
            print(f"{base}^2 mod {modulus} = {base * base} mod {modulus} = {(base * base) % modulus}")
        base = (base * base) % modulus
    return result

# Параметры RSA (помните, что p и q должны быть простыми числами)
p = 223
q = 149
e = 17
print(f"e = {e}")
# Вычисление модуля n и функции Эйлера φ(n)
print(f"Выбраны простые числа: p = {p}, q = {q}")
n = p * q
phi_n = (p - 1) * (q - 1)
print(f"n = p * q = {p} * {q} = {n}")
print(f"φ(n): φ(n) = (p - 1) * (q - 1) = ({p} - 1) * ({q} - 1) = {phi_n}\n")

# Открытый текст x (в двоичном виде)
x = int("101110101101110", 2)  # Преобразуем двоичное число в десятичное

# Шифрование
ciphertext = modular_exponentiation(x, e, n)

# Вывод результатов
print(f"\nОткрытый текст (в двоичном виде): x_2 = {bin(x)[2:]}")
print(f"Открытый текст (в десятичном виде): x_10 = {x}")

print(f"\nЗашифрованный текст (в десятичном виде): {ciphertext}")
print(f"Зашифрованный текст (в двоичном виде): {bin(ciphertext)[2:]}")

# Расшифровка
print(f"\nВычисление закрытого ключа d: \nd * e ≡ 1 (mod φ(n)) => \nd * {e} ≡ 1 (mod {phi_n}) =>")
d = mod_inverse(e, phi_n)  # Вычисляем закрытый ключ d
print(f"Закрытый ключ d: {d}")

print(f"\n(проверка) Расшифрование")
decrypted_text = modular_exponentiation2(ciphertext, d, n)
# Вывод расшифрованного текста
print(f"\nРасшифрованный текст (в десятичном виде): {decrypted_text}")
print(f"Расшифрованный текст (в двоичном виде): {bin(decrypted_text)[2:]}")

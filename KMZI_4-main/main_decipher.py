# Функция для расширенного алгоритма Евклида
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def print_gcd(a, b):
    print(f"\nНОД({a},{b})")
    while b != 0:
        print(f'{a} = {a//b} * {b} + {a%b}')
        a, b = b, a % b
def print_extended_gcd1(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = print_extended_gcd1(b % a, a)
        print(f"{y} - ({b} / {a}) * {x}")
        return g, y - (b // a) * x, x

# Функция для нахождения закрытого ключа d
def find_private_key(e, phi_N):
    g, d, _ = extended_gcd(e, phi_N)
    return d % phi_N  # Убедимся, что d положительное

def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

def mod_inverse(p, q, M_1, M_2):
    """Находит мультипликативную обратную к e по модулю phi"""
    print_gcd(p, q)
    print()
    gcd, x, min_x = print_extended_gcd1(p, q)
    if gcd != 1:
        raise Exception("Обратного элемента не существует")
    else:
        print()
        print(f"=> x_0 = {M_1} * {q} * {min_x} + {M_2} * {p} * {x % q}")
        print(f"=> x_0 = {min_x * M_1 * q + M_2 * p * (x % q)} mod {p * q}")
        x_0 = min_x * M_1 * q + M_2 * p * (x % q)
        if(x_0 < 0):
            while x_0 < 0:
                x_0 = x_0 + (p * q)
            print(f"=> x_0 = {x_0} mod {p * q}\n")
    print(f"y_10 = {x_0}")
    print(f"y_2 = {decimal_to_binary(x_0)}")


# Основная функция
def rsa_example():
    # Шаг 1: Определение параметров RSA
    p = 131
    q = 211
    N = p * q  # N = p * q
    phi_N = (p - 1) * (q - 1)  # φ(N) = (p-1)(q-1)
    e = 17  # Открытый экспонент

    print(f"Шаг 1: Выбор простых чисел p = {p}, q = {q}")
    print(f"N = p * q = {N}")
    print(f"φ(N) = (p - 1) * (q - 1) = {phi_N}")

    # Шаг 2: Нахождение закрытого ключа d
    d = find_private_key(e, phi_N)  # d такое, что (d * e) mod φ(N) = 1
    print(f"\nШаг 2: Нахождение закрытого ключа d")
    print(f"Используем расширенный алгоритм Евклида для нахождения d:")
    print(f"d ≡ e^(-1) (mod φ(N))")
    print(f"d ≡ {e}^(-1) (mod {phi_N})")
    print(f"Закрытый ключ d: {d}")

    # Шаг 3: Шифртекст в двоичном формате
    Y_binary = '101010001010101'  # Пример шифртекста
    Y_decimal = int(Y_binary, 2)  # Преобразование в десятичное число
    print(f"\nШаг 3: Шифртекст Y в двоичном формате: {Y_binary}")
    print(f"Y в десятичной системе: {Y_decimal}")

    # Шаг 4: Вычисление d_p и d_q
    d_p = d % (p - 1)
    d_q = d % (q - 1)
    print(f"\nd_p = d mod (p-1) = {d} mod ({p}-1) = {d_p}")
    print(f"d_q = d mod (q-1) = {d} mod ({q}-1): {d_q}")

    # Шаг 5: Вычисление y_p и y_q
    y_p = Y_decimal % p
    y_q = Y_decimal % q
    print(f"\ny_p = Y mod p = {Y_decimal} mod {p} = {y_p}")
    print(f"y_q = Y mod q = {Y_decimal} mod {q} = {y_q}")

    # Шаг 6: Вычисление M_1 и M_2 (тут надо менять)
    M_1 = 121
    M_2 = 40

    print(f"\nM_1 = (y_p)^(d_q) mod p = {y_p}^{d_p} mod {p} = {M_1}")
    print(f"M_2 = (y_q)^(d_p) mod q = {y_q}^{d_q} mod {q} = {M_2}")

    # Шаг 7: Решение системы линейных уравнений
    print(f"\nРешение системы:\nx ≡ M_1 mod p\nx ≡ M_2 mod q")
    print(f"\nx ≡ {M_1} mod {p}\nx ≡ {M_2} mod {q}")
    mod_inverse(p, q , M_1, M_2)


# Запуск примера RSA
rsa_example()

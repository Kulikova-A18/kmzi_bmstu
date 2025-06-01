def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = 10783160963
phi_n = 10782953280
p_plus_q = n - phi_n + 1
print(f"p + q = {n} - {phi_n} + 1 = {p_plus_q}")

for p in range(2, p_plus_q):
    q = p_plus_q - p
    if p * q == n and is_prime(p) and is_prime(q):
        print(f"простые множители: p = {p}, q = {q}")
        break

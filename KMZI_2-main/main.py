initial_plaintext = '0000000000000000'
keys = ['10101010', '11111111', '01010101', '11111111']

def s_box(input_bits):
    s_box = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7]
    output = ''
    
    print(f"S-box input: {input_bits}")
    
    for i in range(0, len(input_bits), 4):
        bits_chunk = input_bits[i:i + 4]
        decimal_value = int(bits_chunk, 2)
        s_box_value = s_box[decimal_value]
        formatted_value = format(s_box_value, '04b')
        
        print(f"На итерации (i={i}):")
        print(f"  Берем '{bits_chunk}', преобразуем в десятичное ({decimal_value}),")
        print(f"  получаем s_box[{decimal_value}] = {s_box_value}, форматируем в '{formatted_value}'.")
        
        output += formatted_value
    
    print(f"Итоговая строка S-box output: '{output}'")
    return output

def p_box(input_bits):
    p_box = [0, 4, 1, 5, 2, 6, 3, 7]
    output = ''
    
    print(f"P-box input: {input_bits}")
    
    for i in p_box:
        bit = input_bits[i]
        output += bit
        
        print(f"  Берем бит из позиции {i}: '{bit}', добавляем к выходу.")
    
    print(f"Итоговая строка P-box output: '{output}'")
    return output


def f_function(p_r, k):
    p_r_int = int(p_r, 2)
    k_int = int(k, 2)
    
    xor_result = format(p_r_int ^ k_int, '08b')
    s_output = s_box(xor_result)
    p_output = p_box(s_output)

    return p_output

def print_scheme(iteration, p_l, p_r, f_result, k):
    print(f"n--- Iteration {iteration} ---")
    print(f"Left Block (L):  {p_l}")
    print(f"Right Block (R): {p_r}")
    print(f"Key (K):        {k}")
    print(f"f(R, K):       {f_result}")

    new_p_r = format(int(p_l, 2) ^ int(f_result, 2), '08b')
    print(f"L' = R:       {p_r}")
    print(f"R' = L XOR f(R, K): {new_p_r}")
    print("---------------------------")

    return new_p_r

def feistel_cipher(p0, keys):
    p_l = p0[:8]
    p_r = p0[8:]

    print(f"Initial: p(0) = {p0}")

    results_table = []

    for i in range(4):
        f_result = f_function(p_r, keys[i])

        new_p_l = p_r
        new_p_r = format(int(p_l, 2) ^ int(f_result, 2), '08b')

        new_p_r = print_scheme(i + 1, p_l, p_r, f_result, keys[i])

        results_table.append({
            "Iteration": i + 1,
            "Left Block (L)": p_l,
            "Right Block (R)": p_r,
            "Key (K)": keys[i],
            "f(R,K)": f_result,
            "New Left Block": new_p_l,
            "New Right Block": new_p_r
        })

        p_l = new_p_l
        p_r = new_p_r

        current_state = p_l + p_r
        print(f"p({i + 1}) -> Left: {p_l}, Right: {p_r}, Combined: {current_state}")
        print(f"p({i + 1}) = {p_r}{p_l}")
        
    ciphertext = p_r + p_l
    print(f"nFinal ciphertext: p(4) = {ciphertext}")

    print("n--- Results Table ---")
    print("{:<12} {:<15} {:<15} {:<10} {:<10} {:<15} {:<15}".format("Iteration", "Left Block", "Right Block", "Key", "f(R,K)", "New Left", "New Right"))
    for result in results_table:
        print("{:<12} {:<15} {:<15} {:<10} {:<10} {:<15} {:<15}".format(
            result["Iteration"],
            result["Left Block (L)"],
            result["Right Block (R)"],
            result["Key (K)"],
            result["f(R,K)"],
            result["New Left Block"],
            result["New Right Block"]
        ))

    return ciphertext

num = 1
ciphertext = feistel_cipher(initial_plaintext, keys)

class ShiftRegister:
    def __init__(self, initial_state, feedback_taps):
        self.state = initial_state  # Состояние регистра (список битов)
        self.feedback_taps = feedback_taps  # Индексы битов для обратной связи
    def step(self):
        current_state_str = ''.join(map(str, self.state))
        new_bit = sum(self.state[tap] for tap in self.feedback_taps) % 2
        self.state = [new_bit] + self.state[:-1]
        new_state_str = ''.join(map(str, self.state))
        operation = f"sum({[self.state[tap] for tap in self.feedback_taps]}) mod 2"
        return current_state_str, new_bit, new_state_str, operation
    def get_output(self, length):
        output_sequence = []
        print(f"[Генерация выходной последовательности длиной {length}]")
        print(f"{'Шаг':<5} {'Состояние':<15} {'Новый бит':<10}  {'Новое состояние'}     {'Операция'}")
        print("-" * 60)
        for step_number in range(length):
            current_state, new_bit, new_state, operation = self.step()
            output_sequence.append(new_bit)
            print(f"{step_number + 1:<5} {current_state:<15} {new_bit:<10}  {new_state}     {operation}")
        print(f"Сгенерированная выходная последовательность: {output_sequence}")
        return output_sequence
    def get_feedback_polynomial(self):
        # Формирование многочлена на основе feedback_taps
        polynomial_terms = []
        degree = len(self.state) - 1
        for tap in self.feedback_taps:
            polynomial_terms.append(f"x^{degree - tap}" if degree - tap > 1 else (f"x" if degree - tap == 1 else "1"))
        polynomial = " + ".join(polynomial_terms)
        return f"P(x) = {polynomial}"
    def display_state(self):
        return f"Регистровый: {''.join(map(str, self.state))}"
    def display_int_state(self):
        return f"{''.join(map(str, self.state))}"
def generate_output_sequences(initial_states, feedback_taps):
    registers = [ShiftRegister(state, taps) for state, taps in zip(initial_states, feedback_taps)]
    output_sequences = []
    print("[Генерация выходных последовательностей]")
    print(f"{'Регистры':<15} {'Выходная последовательность'}")
    print("-" * 40)

    for i, register in enumerate(registers):
        print(f"[{i+1}] Регистровый {i + 1}    {register.display_int_state()}")

    print(f"\n")

    for i, register in enumerate(registers):
        print(f"[{i+1}] Регистровый {i + 1}")
        output_sequence = register.get_output(16)
        output_sequences.append(output_sequence)
        feedback_polynomial = register.get_feedback_polynomial()
        print(f"Регистровый {i + 1}: {register.display_state()} -> {output_sequence} | {feedback_polynomial}")
        print(f"\n")
    return output_sequences

def custom_zip(iterable1, iterable2):
    print(f"[1] Создание гаммы")
    print(f"- Открытый текст: {iterable1}\n- ключевой поток: {iterable2}")
    min_length = min(len(iterable1), len(iterable2))
    for i in range(min_length):
        print(f"Объединяем элементы: {iterable1[i]} (из открытого текста) и {iterable2[i]} (из ключевого потока) -> {iterable1[i], iterable2[i]}")
        yield (iterable1[i], iterable2[i])

def encrypt_with_keystream(plaintext, keystream):
    encrypted = []
    print("[Шифрование открытого текста с использованием гаммы]")

    # Используем нашу функцию zip для объединения элементов из plaintext и keystream
    zipped = list(custom_zip(plaintext, keystream))
    print(f"[2] Зашифрование с использованием гаммы")
    print(f"{'Открытый текст':<15} {'Гамма':<10} {'Зашифрованный бит'}")
    print("-" * 40)
    for p_bit, k_bit in zipped:
        encrypted_bit = p_bit ^ k_bit
        oper = f"{p_bit} ^ {k_bit}"
        encrypted.append(encrypted_bit)
        print(f"{p_bit:<15}     {k_bit:<10}     {encrypted_bit}")

    return encrypted

def main():

    initial_states = [
        [1, 0, 1, 0],  # Регистр 0
        [0, 1, 0, 1],  # Регистр 1
        [0, 1, 1, 0]   # Управляющий регистр
    ]
    print(f"Регистр 0 - {initial_states[0]} (далее по коду- Регистровый 1)")
    print(f"Регистр 1 - {initial_states[1]} (далее по коду- Регистровый 2)")
    print(f"Управляющий регистр - {initial_states[2]} (далее по коду - Регистровый 3)\n")
    # x^4 + 1 - [3]
    # x^3 + 1 - [2]
    # x^2 + 1 - [1]
    # x + 1 - [0]
    feedback_taps = [
        [3, 2],  # Регистр 0: x^4 + x^3 + 1
        [3, 1],  # Регистр 1: x^4 + x + 1
        [3, 2, 1, 0] # Управляющий регистр: x^4 + x^3 + x^2 + x + 1
    ]
    output_sequences = generate_output_sequences(initial_states, feedback_taps)
    plaintext_input = [1,1,0,0,1,0,1,1,0,1,1,1,0,0,1,0] 
    print("Текст:", plaintext_input)
    keystream = output_sequences[2]
    encrypted_text = encrypt_with_keystream(plaintext_input, keystream)
    print("Зашифрованный текст:", encrypted_text)
if __name__ == "__main__":
    main()

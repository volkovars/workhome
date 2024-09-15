def float_to_ieee754_32bit(value):
    if value == 0.0:
        return '0' * 32, '00000000'
    
    if value == float('inf'):
        return '0' * 8 + '11111111' + '00000000000000000000000', '7F800000'
    
    if value == float('-inf'):
        return '1' * 8 + '11111111' + '00000000000000000000000', 'FF800000'
    
    if value != value:
        return '0' * 8 + '11111111' + '10000000000000000000000', '7FC00000'

    sign = 0
    if value < 0:
        sign = 1
        value = -value

    exponent = 127 

    while value < 1.0:
        value *= 2.0
        exponent -= 1
    while value >= 2.0:
        value /= 2.0
        exponent += 1

    mantissa = value - 1.0
    mantissa_bits = []
    
    for _ in range(23):
        mantissa *= 2
        if mantissa >= 1.0:
            mantissa_bits.append(1)
            mantissa -= 1.0
        else:
            mantissa_bits.append(0)

    exponent_bits = format(exponent + 127, '08b') 
    mantissa_bits = ''.join(map(str, mantissa_bits))

    binary_representation = f"{sign:01b}" + exponent_bits + mantissa_bits

    hex_representation = hex(int(binary_representation, 2))[2:].zfill(8).upper()

    return binary_representation, hex_representation

try:
    input_str = input("Введите вещественное число: ")
    number = float(input_str.replace(',', '.'))
    binary_representation, hex_representation = float_to_ieee754_32bit(number)
    print(f'Число {number} в формате IEEE 754 (32-бит) в бинарном виде: {binary_representation}')
    print(f'Число {number} в формате IEEE 754 (32-бит) в шестнадцатеричном виде: {hex_representation}')
except ValueError:
    print("Ошибка: Пожалуйста, введите корректное вещественное число.")
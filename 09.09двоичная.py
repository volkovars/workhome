def binary_to_decimal(binary_str):
    if ',' in binary_str:
        int_part, frac_part = binary_str.split(',')
    else:
        int_part = binary_str
        frac_part = ''

    int_decimal = int(int_part, 2) if int_part else 0

    frac_decimal = 0
    for i, bit in enumerate(frac_part):
        frac_decimal += int(bit) * (2 ** -(i + 1))

    return int_decimal + frac_decimal

binary_str = input("Введите число в двоичной сс: ")

try:
    decimal_value = binary_to_decimal(binary_str)
    formatted_value = f"{decimal_value}".replace('.', ',')
    print(f"Число {binary_str} в десятичной сс: {formatted_value}")
except ValueError:
    print("Введено некорректное двоичное число.")
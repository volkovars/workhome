def bin_dec(bin_str):
    if "," in bin_str:
        int_part, fract_part = bin_str.split(",")
    else:
        int_part, fract_part = bin_str, ""

    int_value = int(int_part, 2)

    fract_value = 0
    for i, digit in enumerate(fract_part):
        fract_value += int(digit) * (2 ** -(i + 1))
    return int_value + fract_value

def bin_hex(bin_str):
    if "," in bin_str:
        int_part, fract_part = bin_str.split(",")  # исправлено: используем split вместо запятой
    else:
        int_part, fract_part = bin_str, ""
    
    hex_int_part = hex(int(int_part, 2))[2:] if int_part else ""

    hex_fract_part = ""
    if fract_part:
        fract = float(f'0.{fract_part}')
        while fract and len(hex_fract_part) < 10:
            fract *= 16
            digit = int(fract)
            hex_fract_part += hex(digit)[2:]
            fract -= digit
    return hex_int_part + ("," + hex_fract_part if hex_fract_part else "")

def dec_bin(dec_num):
    if isinstance(dec_num, int):
        return bin(dec_num)[2:]
    int_part = int(dec_num)
    fract_part = dec_num - int_part
    bin_int_part = bin(int_part)[2:]
    bin_fract_part = ""
    while fract_part and len(bin_fract_part) < 10:
        fract_part *= 2
        bit = int(fract_part)
        bin_fract_part += str(bit)
        fract_part -= bit

    return bin_int_part + ("," + bin_fract_part if bin_fract_part else "")

if __name__ == "__main__":
    dec_num = float(input("Введите десятичное число: "))  # исправлено: преобразование в float
    bin_str = input("Введите двоичное число: ")  # исправлено: переименованная переменная
    print(bin_dec(bin_str))
    print(bin_hex(bin_str))
    print(dec_bin(dec_num))
def to_signed_binary(num, bits=8):
    if num >= 0:
        return format(num, f'0{bits}b')
    else:
        return format((1 << bits) + num, f'0{bits}b')

def from_signed_binary(binary_str):
    bits = len(binary_str)
    num = int(binary_str, 2)
    if binary_str[0] == '1':  
        num -= (1 << bits)  
    return num

def to_hex(num, bits=8):
    if num >= 0:
        return format(num, f'0{bits // 4}X').upper()
    else:
        
        return format((num + (1 << bits)) & (2**bits - 1), f'0{bits // 4}X').upper()

def from_hex(hex_str, bits=8):
    try:
        num = int(hex_str, 16)
        if num >= (1 << (bits - 1)): 
            num -= (1 << bits)
        return num
    except ValueError:
        return "Ошибка: неверное шестнадцатеричное число."

if __name__ == "__main__":
    while True:
        try:
            user_input = input("Введите целое число: ")
            if user_input.lower() == 'exit':
                break
            num = int(user_input)
            
            bits = 8 
            
            binary_representation = to_signed_binary(num, bits)
            print(f"{num} в дополнительном коде ({bits} бит): {binary_representation}")

            
            hex_representation = to_hex(num, bits)
            print(f"{num} в шестнадцатеричном представлении ({bits} бит): {hex_representation}")

           
            restored_number = from_signed_binary(binary_representation)
            print(f"Бинарное представление {binary_representation} обратно в число: {restored_number}")

            restored_from_hex = from_hex(hex_representation, bits)
            print(f"Шестнадцатеричное представление {hex_representation} обратно в число: {restored_from_hex}")

        except ValueError:
            print("Ошибка: введите целое число.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
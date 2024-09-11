def int_fract(double_num):
    int_part = ""
    fract_part = ""
    flag = False
    for i in double_num:
        if i == ",":
            flag = True
            continue
        if flag == False:
           int_part = int_part + i
        else:
           fract_part = fract_part + i
    if flag == False:
        fract_part = "0"
    return str(int_conv(int_part)) + "," + str(fract_conv(fract_part))


def int_conv(int_part):
    number = ""
    degree = 0
    for a in reversed(int_part):
        number = int(a) * (2 ** degree)
        degree = degree + 1
    return degree



def fract_conv(fract_part):
    number = ""
    degree = 1
    for b in fract_part:
        number = int(b) * (2 ** degree)
        degree = degree + 1
    return degree


if __name__ == "__main__":
    double_num = str(input("Введите двоичное число: "))
    print(int_fract(double_num))
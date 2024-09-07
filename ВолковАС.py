import math

def task18(message, page, line, symbol):
    i = 2 ** ((inp4 * 8) / (inp1 * inp2 * inp3))
    return int (i)

def task19 (alphabet, alphabet2):
    i = (math.log2(inp5)) / (math.log2(inp6))
    return i

def task20 (letter, bit):
    i = inp7 / (math.log2(inp8))
    return int (i)


def task7 (paint, white, blue):
    k = (inp9 * inp10) / (2 ** inp11)
    return int (k)

def task191(friend):
    n = 2 ** inp12
    return int (n)


def task201(Petya):
    n = 2 ** inp13
    return int (n)


if __name__ == "__main__" :
    #inp1 = int (input("количество страниц: "))
    #inp2 = int (input("количество строк: "))
    #inp3 = int (input("количество символов: "))
    #inp4 = int (input("количество байтов: "))
    #print (task18(inp1, inp2, inp3, inp4))
    #inp5 = int (input("мощность 1 алфавита: "))
    #inp6 = int (input("мощность 2 алфавита: "))
    #print (task19(inp5, inp6))
    #inp7 = int (input("количество бит: "))
    #inp8 = int (input("мощность алфавита: "))
    #print (task20(inp7, inp8))
    #inp9 = int (input("израсходовали белой краски: "))
    #inp10 = int (input("израсходовали синей краски: "))
    #inp11 = int (input("количество бит на синию и белую краску: "))
    #print (task7(inp9, inp10, inp11))
    #inp12 = int (input("количество бит на информацию: "))
    #print (task191(inp12))
    inp13 = int (input("количество бит на информацию: "))
    print (task201(inp13))

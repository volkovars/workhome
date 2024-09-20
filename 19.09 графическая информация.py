import math
def task1(n, m,):
    k = 1
    V = n * m * k #находим объем памяти этого изображения
    return int (V)

def task2(before, after,):
    result = after / before #находим во сколько раз увеличился объем памяти
    return int (result)

def task3(nn, mm, vv):
    vv = vv * 1024 * 8 #переводим Кб в биты
    k = vv / (nn * mm) #определяем кол-во цветов
    return int (k)

def task4 (k, vvv):
    vvv = vvv * 8 #переводим из байты в бит
    k = math.log2 (k) #узнаём сколько бит в одной точке
    mn = vvv / k #кол-во точек на экране
    return int (mn)
    




if __name__ == "__main__" :
    #n = int (input("ширина: "))
    #m = int (input("высота: "))
    #print (task1(n, m))
    #before = int (input("количество цветов до: "))
    #after = int (input("количество цветов после: "))
    #print (task2(before, after))
    #nn = int (input("ширина: "))
    #mm = int (input("высота: "))
    #vv = int (input("объем памяти: "))
    #print (task3(nn, mm, vv))
    k = int (input("количество цветов: "))
    vvv = int (input("объем памяти: "))
    print (task4(k, vvv))
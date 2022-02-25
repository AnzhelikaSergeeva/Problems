def bubbleSort(mass):
    for i in range(len(mass)):
        for j in range(0, len(mass) - i - 1):
            if isFewer(mass[j], mass[j+1]):
                mass[j], mass[j + 1] = mass[j + 1], mass[j]
    return mass


def isFewer(s1, s2):
    n1 = s1 + s2
    n2 = s2 + s1
    if n1 < n2:
        return True
    else:
        return False


def maxNuber(mass):
    bubbleSort(mass)
    new_s = ''
    for i in mass:
        new_s += i
    return new_s


stroka = input("Введите список чисел, разделенных пробелом: ")
num_list = stroka.split()
print(maxNuber(num_list))
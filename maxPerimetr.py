
def quickSort(mass):
    if len(mass) <= 1:
        return mass
    pivot = mass[0]
    less = [i for i in mass if i < pivot]
    equally = [i for i in mass if i == pivot]
    more = [i for i in mass if i > pivot]
    return quickSort(more) + equally + quickSort(less)


def maxPerimetr(mass):
    mass = quickSort(mass)
    while len(mass) > 2:
        a = mass[0]
        b = mass[1]
        for i in range(2, len(mass)):
            if (a < b + mass[i]) and (b < a + mass[i]) and (mass[i] < a + b):
                return a + b + mass[i]
        mass.remove(mass[0])
    return 0


stroka = input("Введите список чисел, разделенных пробелом: ")
num_list = stroka.split()
num_list = [int(i) for i in num_list]


print(maxPerimetr(num_list))
import numpy as np

#Zadanie 1
def zad_1():
    a = np.arange(48)
    s = slice(3, 48, 3)
    print("Zadanie 1:", a[s])

def zad_2():
    floats = np.array([3.13, 15.15, 24.4])
    convert = floats.astype('int64')
    print(convert.dtype)

def main():
    zad_1()
    zad_2()


main()
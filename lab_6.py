import numpy as np

#Zadanie 1
def zad_1():
    a = np.arange(48)
    s = slice(3, 48, 3)
    print("Zadanie 1:", a[s])

def zad_2():
    floats = np.array([3.13, 15.15, 24.4])
    convert = floats.astype('int64')
    print("Zadanie 2:", convert.dtype)

def zad_3(n):
    tab = np.arange(n*n)
    tab = tab.reshape((n,n))
    print("Zadanie 3:",'\n', tab)

def zad_4(podstawa, ilosc):
    potegi = np.logspace(podstawa, 4, num=ilosc)
    print(potegi)

def zad_5(n):
    mat = np.arange(n)
    mat_diag = np.diag(mat)
    print("Zadanie 5:", '\n', mat_diag[::-1])

def main():
    zad_1()
    zad_2()
    zad_3(5)
    zad_4(2, 4)
    zad_5(5)

main()
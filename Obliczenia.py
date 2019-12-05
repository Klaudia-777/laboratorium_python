import random

def rownanie():
        print("Wprowadz dane do rownanie kwadratowego:")
        print(" a:")
        a = int(input())
        print(" b:")
        b = int(input())
        print(" c:")
        c = int(input())

        delta = b**b - 4*a*c
        if delta < 0:
                print("Nie ma rozwiazan rzeczywitych")
        else:
                x1 = (-b - delta**(1/2))/2*a
                x2 = (-b + delta**(1/2))/2*a
                print(f'Wyniki:'
                        f'X1 ={x1}, X2 ={x2}\n')


def sortuj():
    liczby = []
    for k in range(50):
        liczby.append(random.randint(1,1000 ))
    print(liczby)

    for i in range(len(liczby)):
        j = len(liczby) - 1
        while j>i:
            if liczby[j] > liczby[j-1]:
                x = liczby[j]
                liczby[j] = liczby[j - 1]
                liczby[j - 1] = x
            j -= 1
    print(f"Posortowane malejaco:\n{liczby}")


#Iloczyn skalarny
def scalarProduct(vector1, vector2):
    if len(vector1) == len(vector2):
        sum = 0
        for i in range(len(vector1)):
            sum = sum + vector1[i] * vector2[i]
    else:
        raise Exception("Uneven lengths of given vectors!")
    return sum


rownanie()
sortuj()


a = [1, 2, 12, 4]
b = [2, 4, 2, 8]

scalar = scalarProduct(a, b)
print(f"\nIloczyn skalarny: {scalar}")


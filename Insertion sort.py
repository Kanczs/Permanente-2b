import time
import random

def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and key < A[i]:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    return A


n = 85000
lista = list(range(n))
random.shuffle(lista)


t_inicio = time.time()
l = insertion_sort(lista)
t_final = time.time()
tiempo = t_final - t_inicio
print(f" Insertion Sort  = {n} fue de:",tiempo)
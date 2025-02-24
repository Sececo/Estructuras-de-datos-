#insert sort
#Lista sin ordenar
A = [89,4,5,0,1243,5,5,2,45]
print(A)
for i in range(1, len(A)):
    b = A[i]
    j = i - 1
    while j >= 0 and A[j] > b:
        A[j + 1] = A[j]
        j -= 1
    A[j + 1] = b

#Lista ordenada
print(A)

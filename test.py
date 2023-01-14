A = [5,3,2,4,1]
for i in range(1, A.__len__()):
    key = A[i]
    j = i-1
    while A[j] > key and j >= 0:
        A[j+1] = A[j]
        j = j-1
    A[j +1] = key
print(A)
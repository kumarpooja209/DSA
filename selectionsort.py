#selection sort
a=[77, 45, 3, 12, 1]
for i in range(len(a)):
    low=i
    for j in range(i+1, len(a)):
        if a[low]>a[j]:
            low=j
    a[i], a[low] =a[low], a[i]
a

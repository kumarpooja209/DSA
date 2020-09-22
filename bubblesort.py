#bubble sort
def bubble(a):
    n=len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j]>a[j+1]:
                a[j], a[j+1]=a[j+1], a[j]
                
                
a=[77, 45, 3, 12, 1]
bubble(a)
a

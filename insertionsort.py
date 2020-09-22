#insertion sort
def insert(a):
    for i in range(1, len(a)):
        ele=a[i]
        j=i-1
        while j>=0 and ele<a[j]:
            a[j+1]=a[j]
            j-=1
        a[j+1]=ele
a=[12, 13, 11, 5, 8]
insert(a)
a
        

#Quick Sort
def partition(a, low, high):
    i=low-1
    p=a[high]
    for j in range(low, high):
        if a[j]<p:
            i=i+1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[high]=a[high],a[i+1]
    return(i+1)
     
def quick(a, low, high):
    if low<high:
        pi=partition(a, low, high)
        quick(a, low, pi-1)
        quick(a, pi+1, high)
        
a=[10, 20, 30, 40, 55, 3, 12, 77]
n=len(a)
quick(a, 0, n-1)
a

#binary search ---- Iterative
def binary(a, l, h, x):
    while l<=h:
        mid= l+(h-l) //2
        if a[mid]==x:
            return mid
        elif a[mid]<x:
            l=mid+1
        else:
            high=mid-1
    return -1
a=[2, 4, 6, 9, 11, 15]
x=11
res=binary(a, 0, len(a)-1, x)
res

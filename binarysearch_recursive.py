#binary search ---- recursive
def binary(a, l, h, x):
    if h>=l:
        mid= l+(h-l) //2
        if a[mid]==x:
            return mid
        elif a[mid]>x:
            return binary(a, l, mid-1, x)
        else:
            return binary(a, mid+1, h, x)
    return -1
a=[2, 4, 6, 9, 11, 15]
x=11
res=binary(a, 0, len(a)-1, x)
res
        

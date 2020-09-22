##mergesort
def merge(arr):
    if len(arr)>1:
        mid=len(arr)//2
        l=arr[mid:]
        r=arr[:mid]
        
        merge(l)
        merge(r)
        i=j=k=0
        
        while(i<len(l) and j<len(r)):
            if(l[i]<r[j]):
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=r[j]
                j+=1
            k+=1
        while i<len(l):
                arr[k]=l[i]
                i+=1
                k+=1
                
        while j<len(r):
                arr[k]=r[j]
                j+=1
                k+=1
                



arr = [13, 41, 52, 7, 2, 88]  
merge(arr)
arr

#Explaination Video: https://classroom.codingninjas.com/app/classroom/me/11600/content/201706/offering/2611193

def partition(a,si,ei):
    # find number of elements smaller than pivot
    pivotele=a[si]
    count=0
    for i in range(si,ei+1):
        if a[i]<pivotele:
            count+=1
    a[si],a[si+count]=a[si+count],a[si]
    pivot_index=si+count

    i=si
    j=ei
    while i<j:
        if a[i]<pivotele:
            i+=1
        elif a[j]>pivotele:
            j-=1
        else:
            a[i] , a[j] = a[j] , a[i]
            i+=1
            j-=1
    return pivot_index
    

def quickSort(a, si, ei):
    if si>=ei:
        return 
    pi=partition(a,si,ei)
    quickSort(a,si,pi-1)
    quickSort(a,pi+1,ei)


a=[int(x) for x in input().split()]
quickSort(a, 0, len(a)-1)
print(a)
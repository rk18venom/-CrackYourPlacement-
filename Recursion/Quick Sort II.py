def partition(arr, low, high):
    pivot=arr[low]
    i=low
    j=high
    while i<j:
        while arr[i]<=pivot and i<=high-1:
            i+=1
        while arr[j]> pivot and j>=low+1:
            j-=1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j]=arr[j], arr[low]
    return j
    
def qS(arr, low, high):
    if low < high:
        pI=partition(arr, low, high)
        qS(arr, low, pI-1)
        qS(arr, pI+1, high)

def quickSort(arr, n):
    qS(arr, 0, n-1)
    return arr
    
n=int(input())
arr=[int(x) for x in input().split()]
arr=quickSort(arr, n)
print(arr)
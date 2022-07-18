#Problem Link: https://classroom.codingninjas.com/app/classroom/me/11600/content/201706/offering/2611191/problem/44


def merge(arr1,arr2,arr):
    i=0
    j=0
    k=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
            arr[k]=arr1[i]
            i=i+1
            k=k+1
        elif arr1[i]>arr2[j]:
            arr[k]=arr2[j]
            j=j+1
            k=k+1
    while i<len(arr1):
        arr[k]=arr1[i]
        i=i+1
        k=k+1
    while j<len(arr2):
        arr[k]=arr2[j]
        j=j+1
        k=k+1
    return arr
            
    
        
def mergeSort(arr):
    # Please add your code here
    if len(arr)==0 or len(arr)==1:
        return
    mid = (len(arr))//2
    s1=arr[0:mid]
    s2=arr[mid:]
    
    mergeSort(s1)
    mergeSort(s2)
    
    merge(s1,s2,arr)
    

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr)
print(*arr)

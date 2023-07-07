def merge(arr1,arr2,n,m):
        #code here
        i=n-1
        j=0
        while(i>=0 and j<m):
            if arr1[i]>arr2[j]:
                arr1[i], arr2[j]=arr2[j],arr1[i]
            i-=1
            j+=1
        arr1.sort()
        arr2.sort()
            
n,m = map(int, input().split())
arr1=[int(x) for x in input().split()]
arr2=[int(x) for x in input().split()]
merge(arr1, arr2, n, m)
print(arr1+arr2)
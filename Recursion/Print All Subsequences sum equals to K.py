def printAllSubsequencesSumK(arr, n, i, curr, x, s):
    if i>=n:
        if s==x:
            print(curr)
        return 
    curr.append(arr[i])
    s+=arr[i]
    printAllSubsequencesSumK(arr, n, i+1, curr, x, s)
    curr.pop()
    s-=arr[i]
    printAllSubsequencesSumK(arr, n, i+1, curr, x, s)

n1=int(input())
arr1=[int(x) for x in input().split()]
x=int(input())
printAllSubsequencesSumK(arr1, n1, 0, [], x, 0)
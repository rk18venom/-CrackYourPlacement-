def printAllSubsequencesSumKBool(arr, n, i, curr, x, s):
    if i>=n:
        if s==x:
            print(curr)
            return True
        return False
    curr.append(arr[i])
    s+=arr[i]
    if printAllSubsequencesSumKBool(arr, n, i+1, curr, x, s)==True:
        return True
    curr.pop()
    s-=arr[i]
    if printAllSubsequencesSumKBool(arr, n, i+1, curr, x, s)==True:
        return True
    return False

n1=int(input())
arr1=[int(x) for x in input().split()]
x=int(input())
printAllSubsequencesSumKBool(arr1, n1, 0, [], x, 0)
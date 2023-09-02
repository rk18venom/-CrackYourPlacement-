def countSubsequencesSumK(arr, n, i, curr, x, s):
    if i>=n:
        if s==x:
            return 1
        return 0
    curr.append(arr[i])
    s+=arr[i]
    ans1=countSubsequencesSumK(arr, n, i+1, curr, x, s)
    curr.pop()
    s-=arr[i]
    ans2=countSubsequencesSumK(arr, n, i+1, curr, x, s)
    return ans1+ans2

n1=int(input())
arr1=[int(x) for x in input().split()]
x=int(input())
print(countSubsequencesSumK(arr1, n1, 0, [], x, 0))
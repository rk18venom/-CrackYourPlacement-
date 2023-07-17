def nextLargerElement(arr,n):
        #code here
        ans = [-1]
        result = []
        for i in arr[::-1]:
            if i < ans[-1]:
                result.append(ans[-1])
                ans.append(i)
            else :
                while ans[-1] != -1 and ans[-1] <= i :
                    ans.pop()
                result.append(ans[-1])
                ans.append(i)
        result.reverse()
        return result

n=int(input())
arr=[int(x) for x in input().split()]
print(nextLargerElement(arr,n))

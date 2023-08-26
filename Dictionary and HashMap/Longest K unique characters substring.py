#Problem Link: https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1

def longestKSubstr(s, k):
    # code here
    ans,c,dict1 = -1, "",{}
    for i in s:
        c += i
        # ma[i] = 1 + ma.get(ma[i],0)
        if i not in dict1: dict1[i] = 1
        else: dict1[i] += 1
        if len(dict1) == k: ans = max(ans,len(c))
        elif len(dict1) > k: 
            dict1[c[0]] -= 1
            if dict1[c[0]] == 0: del dict1[c[0]]
            c = c[1:]
    return ans

s=input()
k=int(input())
print(longestKSubstr(s,k))
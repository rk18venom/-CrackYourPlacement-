#Problem Link: https://codeforces.com/problemset/problem/1703/E


t=int(input())
while t>0:
    n=int(input())
    arr=[[x for x in input()] for i in range(n)]
    count=0
    m=n-1
    ans=[]
    for i in range((n+1)//2):
        for j in range(n//2):
            nowi=i
            nowj=j
            oldnowj=nowj
            sum_ = int(arr[nowi][nowj])
            nowj=n-nowi-1
            nowi=oldnowj
            sum_+=int(arr[nowi][nowj])
            oldnowj=nowj
            nowj=n-nowi-1
            nowi=oldnowj
            sum_+=int(arr[nowi][nowj])
            oldnowj=nowj
            nowj=n-nowi-1
            nowi=oldnowj
            sum_+=int(arr[nowi][nowj])
            count+=min(sum_, 4-sum_)
    print(count)
    
    t=t-1
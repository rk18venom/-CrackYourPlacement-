#Problem Link: https://practice.geeksforgeeks.org/problems/swapping-pairs-make-sum-equal4142/1?page=2&sprint=a663236c31453b969852f9ea22507634&sprint=a663236c31453b969852f9ea22507634&sortBy=submissions

def findSwapValues(a, n, b, m):
    # Your code goes here
    s1=sum(a)
    s2=sum(b)
    
    if s1>s2:
        dict1={}
        for x in a:
            dict1[x]=dict1.get(x,0)+1
        
        diff=s1-s2
        if diff%2!=0:
            return -1
        else:
            diff=diff//2
            for y in b:
                val=diff+y
                if dict1.get(val,0)!=0:
                    return 1
        
    else:
        dict2={}
        for y in b:
            dict2[y]=dict2.get(y,0)+1
        
        diff=s2-s1
        if diff%2!=0:
            return -1
        else:
            diff=diff//2
            for x in a:
                val=diff+x
                if dict2.get(val,0)!=0:
                    return 1
    return -1
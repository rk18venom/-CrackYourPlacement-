def sol(arr):
    n = len(arr)
    dict1={}
    data=[]
    for x in arr:
        if x not in dict1:
            dict1[x]=1
            print("No")
            data.append(x)
        else:
            print("Yes")
            data.append(x)
    return data

arr=[x for x in input().split()]
print(sol(arr))
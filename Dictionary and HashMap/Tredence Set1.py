def sol(arr):
    n = len(arr)
    data=[]
    for x in arr:
        if x not in data:
            print("No")
            data.append(x)
        else:
            print("Yes")
            data.append(x)
    return data

arr=[x for x in input().split()]
print(sol(arr))
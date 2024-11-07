#Link: https://www.geeksforgeeks.org/problems/split-array-in-three-equal-sum-subarrays/1

#Solution

def findSplit(arr):
    # Return an array of possible answer, driver code will judge and return true or false based on
    s=sum(arr)
    #print(s)
    if s%3!=0:
        return [-1,-1]
    e=s//3
    prefixSum=0
    n=len(arr)
    l=[]
    initial=0
    tot=0
    for i in range(n):
        prefixSum+=arr[i]
        
        if prefixSum==e:
            prefixSum=0
            tot+=1
            l.append([initial, i])
            initial = i+1
            if tot==3:
                break
            
    if tot==3:
        return l[:2]
    else:
        return [-1,-1]

#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        result = findSplit(arr)

        if result == [-1, -1]:
            print("false")
        else:
            print("true")

#Link: https://www.geeksforgeeks.org/problems/attend-all-meetings/1

#Solution

#1. Using Sorting

def canAttend(arr):
        # Your Code Here
        sorted_list = sorted(arr, key=lambda x: x[0])
        prevEndTime=None
        n=len(arr)
        for i in range(n):
            if prevEndTime==None:
                prevEndTime=sorted_list[i][1]
            elif prevEndTime<=sorted_list[i][0]:
                prevEndTime=sorted_list[i][1]
            else:
                return False
        return True
                


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        # a = list(map(int, input().strip().split()))
        arr = []
        # j = 0
        for i in range(n):
            a = list(map(int, input().strip().split()))
            x = a[0]
            # j += 1
            y = a[1]
            # j += 1
            arr.append([x, y])
        ans = canAttend(arr)
        if ans:
            print("true")
        else:
            print("false")

# } Driver Code Ends


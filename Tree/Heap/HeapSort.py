#Problem Link: https://practice.geeksforgeeks.org/problems/heap-sort/1

import heapq

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        heapq.heapify(arr)
        
        
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        l=[]
        for x in arr:
            heapq.heappush(l,x)
        self.heapify(l, n, 0)
        return l
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        c=Solution()
        l=c.buildHeap(arr,n)
        for i in range(n):
            m=heapq.heappop(l)
            arr[i]=m
        return arr
    

test_cases = int(input())
for cases in range(test_cases):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    Solution().HeapSort(arr,n)
    print(*arr)

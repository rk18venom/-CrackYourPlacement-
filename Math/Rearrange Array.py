#Problem Link: https://www.interviewbit.com/problems/rearrange-array/

class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, Arr):
        n=len(Arr)
        '''dict1={}
        for i in range(n):
            dict1[i]=Arr[Arr[i]]
        for i in range(n):
            Arr[i]=dict1[i]
        '''
        #O(1) Space
        
        for i in range(n):
            x=Arr[i]
            y=Arr[x]
            Arr[i]=x+(y%n)*n
        
        for i in range(n):
            Arr[i]=Arr[i]//n
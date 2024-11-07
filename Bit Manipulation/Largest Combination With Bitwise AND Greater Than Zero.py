#Link: https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/description/?envType=daily-question&envId=2024-11-07

#Solution
#1. For the bitwise AND to be greater than zero, at least one bit should be 1 for every number in the combination.
#2. The candidates are 24 bits long, so for every bit position, we can calculate the size of the largest combination such that the bitwise AND will have a 1 at that bit position.

def largestCombination(candidates):
        bitCount=[0]*24
        for i in range(24):
            for num in candidates:
                if (num & (1<<i))!=0:
                    bitCount[i]+=1
        return max(bitCount)

#Main

t=int(input())
while t!=0:
     n=int(input())
     candidates=list(map(int,input().split()))
     print(largestCombination(candidates))
     t-=1


    
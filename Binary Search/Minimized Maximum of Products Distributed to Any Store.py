#Link: https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/description/?envType=daily-question&envId=2024-11-14

#Solution
'''
Approach 1: Binary Search on The Answer
Intuition
To approach this problem, let’s first consider a slightly different question:

Given the parameters (n and quantities) and an additional integer x, can we determine if it's possible to distribute the products such that no store receives more than x products?

A natural approach is to assign products to stores while avoiding overloading any single store. As we allocate products, we keep track of how many products of each type remain and how many stores are still available. If we can distribute all products without exceeding the limit at any store, we confirm that distribution is possible; otherwise, it is not.

Now, how does this help with our original problem?

We want to find the smallest x for which such a valid distribution exists, ensuring no store gets more than x products. Notice that for any x≥max(quantities[i]), the answer is trivially true because each store could handle just one type of product. A naive approach would be to linearly search for the smallest x in the range [0,max(quantities[i])] where the distribution is valid. However, this would result in a time limit exceeded (TLE) error for larger inputs.

To optimize, we leverage the problem's monotonic property: if a distribution is possible for a certain x, it will be possible for any x 
′
 >x. Conversely, if it’s not possible for x, it won’t be for any x 
′
 <x. This allows us to apply Binary Search to efficiently find the smallest valid x.
'''

class Solution:
    def can_distribute(self, x, quantities, n):
        # Pointer to the first not fully distributed product type
        j = 0
        # Remaining quantity of the jth product type
        remaining = quantities[j]

        # Loop through each store
        for i in range(n):
            # Check if the remaining quantity of the jth product type
            # can be fully distributed to the ith store
            if remaining <= x:
                # If yes, move the pointer to the next product type
                j += 1
                # Check if all products have been distributed
                if j == len(quantities):
                    return True
                else:
                    remaining = quantities[j]
            else:
                # Distribute the maximum possible quantity (x) to the ith store
                remaining -= x

        return False

    def minimizedMaximum(self, n, quantities):
        # Initialize the boundaries of the binary search
        left = 0
        right = max(quantities)

        # Perform binary search until the boundaries converge
        while left < right:
            middle = (left + right) // 2
            if self.can_distribute(middle, quantities, n):
                # Try for a smaller maximum
                right = middle
            else:
                # Increase the minimum possible maximum
                left = middle + 1

        return left
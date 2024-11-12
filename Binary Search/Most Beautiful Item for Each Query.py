#Link: https://leetcode.com/problems/most-beautiful-item-for-each-query/description/

#Solution
import bisect

def maximumBeauty(items, queries):
    sorted_list = sorted(items, key=lambda x: x[0])
    dict1={}
    dict1[0]=0
    max_beauty=0

    for price, beauty in sorted_list:
        max_beauty = max(max_beauty, beauty)
        dict1[price] = max_beauty
    
    ans=[]
    sorted_prices = sorted(dict1.keys())
    
    # Process each query
    for query in queries:
        # Find the largest price less than or equal to the query price
        idx = bisect.bisect_right(sorted_prices, query) - 1
        ans.append(dict1[sorted_prices[idx]])
    
    return ans

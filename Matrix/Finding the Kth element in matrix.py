#Problem Link: https://practice.geeksforgeeks.org/problems/find-nth-element-of-spiral-matrix/1

def findK(l, n, m, r):
        # Write Your Code here
        CS = 0
        CE = len(l[0])-1
        RS = 0
        RE = len(l)-1
        ans =[]
        total_elements = len(l[0])*len(l)
        while total_elements>0:
    
            for x in range(CS,CE+1):
                ans.append(l[RS][x])
                
            RS=RS+1
            
            total_elements= total_elements-(CE-CS+1)
            if total_elements == 0:
                break
            
            for k in range(RS,RE+1):
                ans.append(l[k][CE])
            
            CE=CE-1
            
            total_elements=total_elements-(RE-RS+1)
            if total_elements == 0:
                break
            
            for m in range(CE,(CS-1),-1):
                ans.append(l[RE][m])
                
            RE=RE-1
            
            total_elements= total_elements-(CE-CS+1)
            if total_elements == 0:
                break
            
            for n in range(RE,(RS-1),-1):
                ans.append(l[n][CS])
                
            CS=CS+1
            total_elements= total_elements-(RE-RS+1)
            
        
        #print(ans)    
        return ans[r-1]

n, m, r= map(int, input().split())
matrix=[[int(x) for x in input().split()] for i in range(n)]
print(findK(matrix, n, m, r))
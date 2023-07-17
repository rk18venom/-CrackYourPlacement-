class queue():
    def __init__(self):
        self.q=[]
    
    def push(self, x):
        self.q.append(x)
    
    def top(self):
        if len(self.q)==0:
            return None
        return self.q[0]
    
    def pop(self):
        x=None
        if len(self.q)<=1:
            x=self.q[0]
            self.q=[]
            return x
        x=self.q[0]
        self.q=self.q[1:]
        return x
    
    def size(self):
        return len(self.q)
    

def solution(A):
    q=queue()
    dict1={}
    ans=''
    for x in A:
        dict1[x]=dict1.get(x,0)+1
        q.push(x)
        if q.top() is not None:
            if dict1[q.top()]==1:
                ans+=q.top()
            else:
                while q.size()!=0:
                    y=q.top()
                    if dict1[y]>=1:
                        q.pop()
                    else:
                        break
                if q.size()==0:
                    ans+='#'
                else:
                    ans+=q.top()
    return ans

s=input()
print(solution(s))
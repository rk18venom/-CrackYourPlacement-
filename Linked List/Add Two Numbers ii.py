class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
        
def nums(head):
    ans=''
    while head!=None:
        ans+=str(head.val)
        head=head.next
    return int(ans)

def length(head):
    if head is None:
        return 0
    return 1+length(head.next)

def linear(n, head):
    i=0
    l=len(n)
    temp=head
    prev=head
    while i<l or head is not None:
        if head is None:
            newNode=ListNode(n[i])
            prev.next=newNode
            head=newNode
        else:
            head.val=n[i]
        prev=head
        head=head.next
        i+=1
    return temp

class Solution:
    def addTwoNumbers(self, l1, l2):
        n1=nums(l1)
        n2=nums(l2)
        n3=str(n1+n2)
        ans=linear(n3,l1)
        return ans


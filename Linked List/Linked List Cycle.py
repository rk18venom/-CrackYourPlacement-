#Problem Link: https://leetcode.com/problems/linked-list-cycle/description/

#Fast and Slow Algorithm 
class NodeLL:
    def __init__(self, data):
        self.data=data
        self.next=None

def hasCycle(head):
    fast=head
    second=head
    while fast!=None and fast.next!=None:
        fast=fast.next.next
        second=second.next
        if fast==second:
            return True
    return False

def takeInput():
    n=int(input())
    m=int(input())
    head = None
    tail=None
    check=None
    curr=head
    i=1

    for i in range(n):
        ele=int(input())
        newNode=NodeLL(ele)
        #Head insertion
        if head is None:
            head=newNode
            curr=head
        else:
            curr.next=newNode
            curr=curr.next
            tail=curr
            if i==m:
                check=curr
        i+=1
    tail.next=check
    return head

head=takeInput()
print(hasCycle(head))
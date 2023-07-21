#Problem link: https://practice.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1

class LLNode:
    def __init__(self,data):
        self.data=data
        self.next=None

def reverseLL(head):
    if head is None:
        return head
    prev=None
    iterator=head
    tail=head
    while iterator!=None:
        curr=iterator
        iterator=curr.next
        curr.next=prev
        prev=curr
    return prev, tail
    
def reverse(head, k):
    # Code here
    if head is None:
        return head
    
    head1=head
    tail1=head
    count=k
    while count!=1 and head!=None:
        head=head.next
        tail1=head
        count-=1
    
    head2=None
    if tail1!=None:
        head2=tail1.next
        tail1.next=None
    
    head1, tail1=reverseLL(head1)
    head2=reverse(head2,k)
    tail1.next=head2
    return head1

def takeInput():
    n=int(input())
    k=int(input())
    arr=[int(x) for x in input().split()]
    head=None
    curr=head
    for x in arr:
        newNode=LLNode(x)
        if head==None:
            head=newNode
            curr=head
        else:
            curr.next=newNode
            curr=curr.next
    return head, k

def printLL(head):
    temp = head
    while (temp.next!= None):
        print(str(temp.data), end=" -> ")
        temp = temp.next
    print(temp.data)

llHead, k=takeInput()
ansHead=reverse(llHead, k)
printLL(ansHead)
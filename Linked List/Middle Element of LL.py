#Problem Link: https://leetcode.com/problems/middle-of-the-linked-list/

#Fast and Slower pointer
class NodeLL:
    def __init__(self, data):
        self.data=data
        self.next=None

def length(head):
    if head == None:
        return 0
    count=0
    while head!=None:
        count+=1
        head = head.next
    return count

def middleNode(head):
        first=head
        second=head
        l=length(head)
        while first!=None and first.next!=None:
            first=first.next.next
            second=second.next
        if l%2==0:
            return second
        else:
            return second

def takeInput():
    n=int(input())
    m= int(input("No. of pointer at which you want cycle in LL from beginning: "))
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
print(middleNode(head).data)
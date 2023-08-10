#Problem Link: https://leetcode.com/problems/reorder-list/

class NodeLL:
    def __init__(self, data):
        self.data=data
        self.next=None

def length(head):
    if head==None:
        return 0
    l=0
    while head!=None:
        l+=1
        head=head.next
    return l

def reorderList(head) -> None:
    arr=[]
    curr=head
    temp=head
    while curr!=None:
        arr.append(curr.data)
        curr=curr.next
    i=0
    j=length(head)-1
    m=0
    while temp!=None:
        if m%2==0:
            temp.data=arr[i]
            i+=1
        else:
            temp.data=arr[j]
            j-=1
        temp=temp.next
        m+=1
    return head

def takeInput():
    n=int(input())
    m=int(input("No. of pointer at which you want cycle in LL from beginning: "))
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

def printLL(head):
    temp = head
    while (temp.next!= None):
        print(str(temp.data), end=" -> ")
        temp = temp.next
    print(temp.data)

head=takeInput()
head=reorderList(head)
printLL(head)
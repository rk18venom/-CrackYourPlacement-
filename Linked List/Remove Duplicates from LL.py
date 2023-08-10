#Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/


class NodeLL:
    def __init__(self, data):
        self.data=data
        self.next=None


def deleteDuplicates(head):
    if head is None:
        return head
    prev=None
    curr=head
    while curr!=None:
        if prev==None:
            prev=curr
        else:
            if prev.val!=curr.val:
                prev.next=curr
                prev=prev.next
        curr=curr.next
    prev.next=None
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

head=takeInput()
print(deleteDuplicates(head))

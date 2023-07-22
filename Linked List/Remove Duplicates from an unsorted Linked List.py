#Problem Link: https://practice.geeksforgeeks.org/problems/remove-duplicates-from-an-unsorted-linked-list/1

class LLNode:
    def __init__(self,data):
        self.data=data
        self.next=None

def removeDuplicates(head):
    # code here
    # return head after editing list
    dict1={}
    ans=None
    curr=None
    while head!=None:
        if dict1.get(head.data,0)==0:
            if ans is None:
                ans=head
                curr=head
            else:
                curr.next=head
                curr=curr.next
        dict1[head.data]=dict1.get(head.data,0)+1
        head=head.next
    curr.next=None
    return ans

def takeInput():
    n=int(input())
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
    return head

def printLL(head):
    temp = head
    while (temp.next!= None):
        print(str(temp.data), end=" -> ")
        temp = temp.next
    print(temp.data)

llHead=takeInput()
ansHead=removeDuplicates(llHead)
printLL(ansHead)
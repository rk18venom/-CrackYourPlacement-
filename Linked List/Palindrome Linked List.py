#Problem Link: https://leetcode.com/problems/palindrome-linked-list/description/
class NodeLL:
    def __init__(self, data):
        self.data=data
        self.next=None

def isPalindrome(head):
    s=[]
    
    while head!=None:
        s.append(head.data)
        head=head.next
    
    return s[::-1]==s

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
print("Is Palindrome?",isPalindrome(head))
        
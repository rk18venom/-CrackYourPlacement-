#Problem Link: https://practice.geeksforgeeks.org/problems/rotate-a-linked-list/1?page=2&status[]=unsolved&category[]=Hash&category[]=Linked%20List&category[]=Searching&category[]=Recursion&curated[]=1&sortBy=submissions

def rotate(head, k):
    # code here
    temp=head
    while temp.next!=None:
        temp=temp.next
    
    while k!=0:
        prev=head
        head=head.next
        prev.next=None
        temp.next=prev
        temp=prev
        k-=1
    return head


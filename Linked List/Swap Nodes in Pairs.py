#Problem Link: https://leetcode.com/problems/swap-nodes-in-pairs/

#Video Link: https://www.youtube.com/watch?v=kLbHAlVv-Mc

#Note: Don't forget to maintain the prev node

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def solve(head,prev):
    if head==None:
        return None
    
    if head.next==None:
        return None
    
    
    nextnode=head.next
    head.next=head.next.next
    nextnode.next=head
    head=nextnode
    if prev!=None:
        prev.next=head
    solve(head.next.next,head.next)
    
class Solution:
    def swapPairs(self, head):
        temp=head
        newnode=None
        if head!=None and head.next!=None:
            root=head.next.val
            newnode=ListNode(root)
        
        solve(temp,None)
        if newnode!=None:
            newnode.next=temp
            temp=newnode
        return temp
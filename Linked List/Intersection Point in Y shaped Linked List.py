#Link of Question: https://practice.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1?page=3&status[]=unsolved&category[]=Arrays&category[]=Strings&category[]=Hash&category[]=Linked%20List&category[]=Searching&category[]=Recursion&curated[]=1&sortBy=submissions
def length(head):
    l=0
    while head!=None:
        l+=1
        head=head.next
    return l

def intersetPoint(head1,head2):
    #code here
    m=length(head1)
    n=length(head2)
    if m>=n:
        diff=m-n
        while diff!=0:
            head1=head1.next
            diff-=1
    else:
        diff=n-m
        while diff!=0:
            head2=head2.next
            diff-=1
        
    while head1!=head2:
        head1=head1.next
        head2=head2.next
    if head1==head2:
        return head1.data
    else:
        return -1
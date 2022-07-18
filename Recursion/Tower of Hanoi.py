#Explaination Video: https://classroom.codingninjas.com/app/classroom/me/11600/content/201706/offering/2611196


def towerOfHanoi(n, A, B, C):
    if n==0:
        return
    if n==1:
        print(A, C)
        return
    towerOfHanoi(n-1, A, C, B)
    print(A, C)
    towerOfHanoi(n-1, B, A, C)
    

n=int(input())
towerOfHanoi(n, 'A', 'B' , 'C')
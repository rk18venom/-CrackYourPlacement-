#Problem Link: https://classroom.codingninjas.com/app/classroom/me/11600/content/201706/offering/2611188/problem/91

def removeConsecutiveDuplicates(string):
    # Please add your code here
    if len(string)==0 or len(string)==1:
        return string
    if string[0]==string[1]:
        smallerOutput=string[0]+string[2:]
        return removeConsecutiveDuplicates(smallerOutput)
    else:
        smallerOutput=string[1:]
        ans=removeConsecutiveDuplicates(smallerOutput)
        return string[0]+ans
        
def removeConsecutiveDuplicatesModified(s):
    if len(s)==0 or len(s)==1:
        return s
    if s[0]==s[1]:
        smallerOutput=removeConsecutiveDuplicatesModified(s[2:])
        return s[1]+smallerOutput if smallerOutput[0]!=s[1] else smallerOutput
    else:
        smallerOutput=removeConsecutiveDuplicatesModified(s[1:])
        return s[0]+smallerOutput if smallerOutput[0]!=s[0] else smallerOutput

# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))

#Problem Link:  https://leetcode.com/problems/valid-parentheses/submissions/?ref=localhost

def isValid(s):
    stack=[]
    for i in range(len(s)):
        if s[i] in ['(', '[', '{']:
            stack.append(s[i])
        else:
            if s[i] in [')', ']', '}']:
                if len(stack)!=0:
                    ele=stack.pop()
                    if ele=='(' and s[i]!=')':
                        return False
                    elif ele=='[' and s[i]!=']':
                        return False
                    elif ele=='{' and s[i]!='}':
                        return False
                else:
                    return False

    if len(stack)!=0:
        return False
    return True

s=input()
ans=isValid(s)
print(ans)

# a file for debug

#MIT.Recursion on non-numerics_palindrome
#判断一个值是不是palindrome

def isPalin(s):
    
    def toChar(s):
        s=s.lower()
        ans=""
        for c in s:
            if c in 'qwertyuioplkjhgfdsazxcvbnm':
                ans+=c
        return ans
    
    def isPal(s):
        
if len(s)==0 or len(s)==1:
            return True
        else：
            return s[0]==s[-1] and isPal(s[1:-1])

    return isPal(toChar(s))


print("is eve a panlindrome")
print(isPalin('eve'))


# indent
# chinese charactor in python2
# chinese colon and english colon
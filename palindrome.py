def isPal(x):
    def tochar(x):
        x = x.lower()
        ans = ""
        for a in x:
            if a in 'qwertyuiopasdfghjklzxcvbnm':
                ans += a
        return ans
    
    def Pal(s):
        print(s)
        if(len(s) == 0 or len(s) == 1):
            return True
        else:
            return s[0] == s[-1] and Pal(s[1:-1])

    return Pal(tochar(x))


print(isPal("Hello,;23sdfh"))
print(isPal("Hello,;23solleh"))
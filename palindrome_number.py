class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=str(x)
        if len(n)==1:
            return True
        else:
            if x>0:
                return n==n[::-1]
            else:
                if n[-1]!="-":
                    return False
                else:
                    return True

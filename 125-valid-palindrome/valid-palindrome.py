class Solution(object):
    def isPalindrome(self, s):
        first = 0
        second = len(s)-1
        while first < second:
            if not s[first].isalnum():
                first += 1
            elif not s[second].isalnum():
                second -= 1
            else:
                if s[first].lower() != s[second].lower():
                        return False
                first += 1
                second -= 1   
        return True
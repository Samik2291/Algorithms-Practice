class Solution(object):
    def isPalindrome(self, s):
        first = 0
        second = len(s)-1
        while first < second:
            if s[first].isalnum():
                if s[second].isalnum():
                    if s[first].lower() != s[second].lower():
                        return False
                    first += 1
                    second -= 1
                else:
                    second -= 1
                    continue
            else:
                first += 1
                continue   
        return True

        
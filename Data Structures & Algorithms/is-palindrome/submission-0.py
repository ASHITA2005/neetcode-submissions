class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isalnum(c):
            if c >= 'a' and c <= 'z':
                return True
            if c >= 'A' and c <= 'Z':
                return True
            if c >= '0' and c <= '9':
                return True
            return False
        clean_str = ''
        for char in s:
            if char == ' ':
                continue
            if isalnum(char):
                clean_str += char.lower()
        #print(''.join(reversed(clean_str)))
        return clean_str == ''.join(reversed(clean_str))


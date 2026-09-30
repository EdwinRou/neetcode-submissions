class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = s.lower()
        clean_s = re.sub(r'[^a-z0-9]', '', s)
        revert_s = str(clean_s[::-1])
        return revert_s == clean_s
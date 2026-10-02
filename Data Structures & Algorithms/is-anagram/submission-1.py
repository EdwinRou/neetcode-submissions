class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def string_to_dict(s: str) ->bool:
            s_dict = {}
            for letter in s:
                if letter in s_dict:
                    s_dict[letter] +=1
                else :
                    s_dict[letter] = 1
            return s_dict
        s_dict, t_dict = string_to_dict(s), string_to_dict(t)
        if s_dict == t_dict:
            return True
        else:
            return False
        

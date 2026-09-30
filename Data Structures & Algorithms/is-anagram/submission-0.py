class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def word_dict(word):
            word_dict = {}
            for letter in word:
                if letter in word_dict:
                    word_dict[letter] += 1
                else:
                    word_dict[letter] = 1
            return word_dict

        s_dict, t_dict = word_dict(s), word_dict(t)
        return s_dict == t_dict
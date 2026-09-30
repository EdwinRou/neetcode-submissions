class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def string_to_frozenset(s:str) -> dict:
            s_dict = {}
            for letter in s:
                if letter in s_dict:
                    s_dict[letter] += 1
                else :
                    s_dict[letter] = 1
            return frozenset(s_dict.items())

        anagram_dict = {}
        stringlist_by_anagram = []

        for string in strs:
            string_set = string_to_frozenset(string)

            if string_set in anagram_dict:
                index = anagram_dict[string_set]
                stringlist_by_anagram[index].append(string)
            else:
                anagram_dict[string_set] = len(stringlist_by_anagram)
                stringlist_by_anagram.append([string])

        return stringlist_by_anagram
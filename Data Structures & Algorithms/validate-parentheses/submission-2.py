class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False
        open_word = {"(", "[", "{"}
        closed_word = {")", "]", "}"}
        full_words = {"()", "[]", "{}"}
        pile = []
        for word in s:
            if word in open_word:
                pile.append(word)
            elif word in closed_word:
                if len(pile) == 0:
                    return False
                last_open_word = pile.pop(-1)
                if last_open_word + word in full_words:
                    pass
                else :
                    return False
        return len(pile) == 0


            
        return True
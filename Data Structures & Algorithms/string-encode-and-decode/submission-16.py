class Solution:

    def encode(self, strs: List[str]) -> str:

        coded_string = ""

        for string in strs:
            length = len(string)
            coded_string += f"{length}:" + string
        print("coded_string: ", coded_string)
        return coded_string

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        strs = []
        index = 0
        while index + 1 < len(s):
            string_number = ''
            digit_index = index
            while s[digit_index] != ":":
                string_digit = s[digit_index]
                string_number += string_digit
                digit_index += 1
            number = int(string_number)

            string = s[index+1+len(string_number) : index+1+ len(string_number)+number]
            strs.append(string)
            index += number + 1 + len(string_number)

        return strs

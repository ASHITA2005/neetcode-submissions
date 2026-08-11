class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += f'{len(word)}*{word}'
        #print(encoded_string)
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            num = ''
            while i < len(s) and s[i] != '*':
                num += s[i]
                i += 1
            #print(num)
            len_word = int(num)
            i += 1
            word = s[i: i+len_word]
            decoded_strs.append(word)
            i += len_word

        return decoded_strs

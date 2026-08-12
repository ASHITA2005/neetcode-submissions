
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = {}
        for i in range(len(strs)):
            sorted_word = tuple(sorted(strs[i]))
            if sorted_word in sorted_strs:
                sorted_strs[sorted_word].append(strs[i])
            else:
                sorted_strs[sorted_word] = [strs[i]]
        result = []
        for value in sorted_strs:
            result.append(sorted_strs[value])
        return result

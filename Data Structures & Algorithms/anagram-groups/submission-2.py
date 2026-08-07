class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        checker = {}

        for word in strs:
            sorts = "".join(sorted(word))

            if sorts not in checker:
                checker[sorts] = []
                
            checker[sorts].append(word)

        return list(checker.values())     

        
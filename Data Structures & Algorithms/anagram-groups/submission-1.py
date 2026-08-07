class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        checker = {}
        returnable = []

        for word in strs:
            sorts = "".join(sorted(word))

            if sorts not in checker:
                checker[sorts] = []
                
            checker[sorts].append(word)
        
        for keys in checker:
            returnable.append(checker[keys])

        return returnable     

        
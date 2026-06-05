class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        returnable = ""
        minimum = min(len(word1), len(word2))

        if(minimum != len(word1)):
            value = word1
        else:
            value = word2

        for i in range(minimum):
            returnable += word1[i:i+1]
            returnable += word2[i:i+1]       

        print(value)
        returnable += value[minimum::]

        return returnable 
        
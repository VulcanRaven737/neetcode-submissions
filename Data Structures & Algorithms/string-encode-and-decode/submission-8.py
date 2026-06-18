class Solution:

    def encode(self, strs: List[str]) -> str:
        temp = []

        for i in range(len(strs)):
            temp.append(str(len(strs[i])) + "#")
            temp.append(strs[i])
        
        enc = "".join(temp)
        print(enc)
        return enc

    def decode(self, s: str) -> List[str]:
        dec = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            start = j + 1
            end = start + length
            word = s[start:end]

            dec.append(word)

            i = end

        return dec



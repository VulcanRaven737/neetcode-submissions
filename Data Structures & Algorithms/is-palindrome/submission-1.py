import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        text = "".join(s.split()).lower()

        translation_table = str.maketrans('', '', string.punctuation)
        cleaned_text = text.translate(translation_table)

        text_comp = cleaned_text[::-1]



        return cleaned_text == text_comp
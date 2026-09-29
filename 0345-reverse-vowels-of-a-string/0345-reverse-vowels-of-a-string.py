class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel=set("aeiouAEIOU")
        char=list(s)
        l=0
        r=len(s)-1
        while l<=r:
            while l<r and char[l] not in vowel:
                l+=1
            while l<r and char[r] not in vowel:
                r-=1
            char[l],char[r]=char[r],char[l]
            l+=1
            r-=1
        return "".join(char) 
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        count=[]
        for i,word in enumerate(words):
            if x in word:
                count.append(i)
        return count
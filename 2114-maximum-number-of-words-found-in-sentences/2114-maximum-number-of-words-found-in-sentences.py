class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        X=0
        for i in sentences:
            X=max(X,i.count(" ")+1)
        return X
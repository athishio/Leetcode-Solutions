class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        d={"type":0,"color":1,"name":2}
        x=0
        for i in items:
            if i[d[ruleKey]]==ruleValue:
                x+=1
        return x
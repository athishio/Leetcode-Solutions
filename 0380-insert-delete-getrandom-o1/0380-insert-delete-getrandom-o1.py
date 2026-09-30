class RandomizedSet:

    def __init__(self):
        self.d={}
        self.l=[]
    def insert(self, val: int) -> bool:
        if val in self.l:
            return False
        self.d[val]=len(self.l)
        self.l.append(val)

    def remove(self, val: int) -> bool:
        if val not in self.l:
            return False
        i=self.d[val]
        self.d[self.l[-1]]=i
        self.l[i]=self.l[-1]
        self.l.pop()
        self.d.pop(val)
        return True

    def getRandom(self) -> int:
        return choice(self.l)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
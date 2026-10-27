class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid=[["#"]*n for _ in range(m)]
        grid[0]=["."]*n
        for i in range(m):
            grid[i][-1]="."
        return ["".join(row) for row in grid]
class Solution:
    def removeInvalidParentheses(self, s: str):
        left_remove = 0
        right_remove = 0
        for c in s:
            if c == '(':
                left_remove += 1
            elif c == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1
        result = set()
        def dfs(i, left, right, balance, path):
            if i == len(s):
                if left == 0 and right == 0 and balance == 0:
                    result.add("".join(path))
                return
            c = s[i]
            if c == '(' and left > 0:
                dfs(
                    i + 1,
                    left - 1,
                    right,
                    balance,
                    path
                )
            elif c == ')' and right > 0:
                dfs(
                    i + 1,
                    left,
                    right - 1,
                    balance,
                    path
                )
            if c != '(' and c != ')':
                path.append(c)
                dfs(
                    i + 1,
                    left,
                    right,
                    balance,
                    path
                )
                path.pop()
            elif c == '(':
                path.append(c)
                dfs(
                    i + 1,
                    left,
                    right,
                    balance + 1,
                    path
                )
                path.pop()
            elif c == ')' and balance > 0:
                path.append(c)
                dfs(
                    i + 1,
                    left,
                    right,
                    balance - 1,
                    path
                )
                path.pop()
        dfs(0, left_remove, right_remove, 0, [])
        return list(result)
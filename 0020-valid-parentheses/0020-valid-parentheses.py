class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={'(':')', '[':']', '{':'}'}
        for i in s:
            if i in pairs:
                stack.append(pairs[i])
            else:
                if not stack or stack.pop()!=i:
                    return False
        return not stack

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
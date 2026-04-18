class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        output = 0
        current = 0

        for ch in s:
            if ch != " ":
                current += 1
                output = current   # update last word length
            else:
                current = 0

        return output

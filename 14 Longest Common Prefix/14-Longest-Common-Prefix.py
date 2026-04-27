class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str = ""
        strs.sort()

        first = strs[0]
        last = strs[len(strs)-1]
        i = 0
        while i < len(first):
            if first[i] != last[i]:
                break
            else:
                str += first[i]
                i += 1

        return str




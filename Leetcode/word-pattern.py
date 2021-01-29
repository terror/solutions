class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()

        if len(pattern) != len(s):
            return 0
        if len(set(pattern)) != len(set(s)):
            return 0

        prev = pattern[0]
        for i in range(1, len(pattern)):
            if pattern[i] != prev:
                if s[i] == s[i-1]:
                    return 0
            prev = pattern[i]

        return 1

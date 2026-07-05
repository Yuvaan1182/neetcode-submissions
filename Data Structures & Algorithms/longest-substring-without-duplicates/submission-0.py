class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        i, j = 0, 0
        res = 0
        dq = deque()

        while j < len(s):
            while (j < len(s) and s[j] not in hashSet):
                hashSet.add(s[j])
                dq.append(s[j])
                j += 1
            res = max(res, len(dq))
            while (j < len(s) and i < j and s[i] != s[j]):
                x = dq.popleft()
                hashSet.discard(x)
                i += 1
            if j < len(s) and s[i] == s[j]:
                hashSet.discard(dq.popleft())
                i += 1

        return res


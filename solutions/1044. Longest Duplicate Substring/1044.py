class Solution:
  def longestDupSubstring(self, s: str) -> str:
    BASE = 26
    HASH = 1_000_000_007
    bestStart = -1
    l = 1
    r = len(s)

    def val(c: str) -> int:
      return ord(c) - ord('a')

    # k := the length of the substring to be hashed
    def getStart(k: int) -> int | None:
      maxPow = pow(BASE, k - 1, HASH)
      hashToStart = collections.defaultdict(list)
      h = 0

      # Compute the hash value of s[:k].
      for i in range(k):
        h = (h * BASE + val(s[i])) % HASH
      hashToStart[h].append(0)

      # Compute the rolling hash by Rabin Karp.
      for i in range(k, len(s)):
        startIndex = i - k + 1
        h = (h - maxPow * val(s[i - k])) % HASH
        h = (h * BASE + val(s[i])) % HASH
        if h in hashToStart:
          currSub = s[startIndex:startIndex + k]
          for start in hashToStart[h]:
            if s[start:start + k] == currSub:
              return startIndex
        hashToStart[h].append(startIndex)

    while l < r:
      m = (l + r) // 2
      start: int | None = getStart(m)
      if start:
        bestStart = start
        l = m + 1
      else:
        r = m

    if bestStart == -1:
      return ''
    if getStart(l):
      return s[bestStart:bestStart + l]
    return s[bestStart:bestStart + l - 1]

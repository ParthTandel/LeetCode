class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        k = len(s)
        arr = [[0 for i in range(k)] for i in range(k)]
        for i in range(k):
            arr[i][i] = 1

        max_len = 0
        start = 0
        end = 0

        for i in range(1,k):
            if s[i] == s[i-1]:
                arr[i-1][i] = 1
                if max_len < 2:
                    max_len = 2
                    start = i-1
                    end = i

        for i in range(3,k + 1 ):
            for j in range(0, k - i + 1):
                x = j
                y = j + i - 1
                if arr[x + 1][y -1] == 1 and s[x] == s[y]:
                    arr[x][y] = 1
                    if i > max_len:
                        max_len = i
                        start = x
                        end = y
        return s[start:end+1]


s = Solution()

print(s.longestPalindrome("ccc"))
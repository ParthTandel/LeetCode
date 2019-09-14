class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        k = len(s)
        for i in range((2*k)-1):
            center = float(i)/2
            if (center - int(center)) > 0:
                s = 0
            else:
                s = 1
            print("center", center)
            for j in range(s, int(center)):
                if (int(center) - j < 0) or (int(center) + j) > k:
                    break
                print( int(center) - j , int(center) + j)


s = Solution()

print(s.longestPalindrome("ccccccc"))

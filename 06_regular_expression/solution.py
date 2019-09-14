class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        arr = [[0 for cols in range(len(p) + 1)] for rows in range(len(s) + 1)]
        arr[0][0] = 1

        for i in range(len(s)):
            arr[i+1][0] = 0

        s = " " + s
        p = " " + p

        for j in range(2,len(p)):
            if p[j] == "*" and arr[0][j-2] == 1:
                arr[0][j] = 1

        for i in range(1,len(s)):
            for j in range(1,len(p)):
                if s[i] == p[j] or p[j] == ".":
                    arr[i][j] = arr[i-1][j-1]
                elif p[j] == '*':
                    if arr[i][j-2] == 1:
                        arr[i][j] = 1
                    elif arr[i-1][j] == 1 and (s[i] == p[j-1] or p[j-1] == "."):
                        arr[i][j] = 1
        return arr[len(s) - 1][len(p) - 1]

def main():
    s = Solution()
    print(s.isMatch("aa", "a*"))


if __name__ == "__main__":
    main()
    pass

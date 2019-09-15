class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        
        if len(chars) == 0:
            return 0

        count = 0
        current = chars[0]
        index = 0
        for c in chars:
            if c == current:
                count = count + 1
            else:
                chars[index] = current
                index = index + 1
                if count > 1:
                    for data in str(count):
                        chars[index] = data
                        index = index + 1
                count = 1
                current = c

        chars[index] = current
        index = index + 1
        if count > 1:
            for data in str(count):
                chars[index] = data
                index = index + 1

        return index
                
        
                
if __name__ == "__main__":
    s = Solution()
    print(s.compress(["a"]))
    pass
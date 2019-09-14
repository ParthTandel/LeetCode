class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_hash = {}
        max_len = 0
        curr_len = 0
        curr_start = 0
        start = 0
        end = 0
        
        index = 0
        for index, i in enumerate(s):
            if i not in  char_hash:
                curr_len = curr_len + 1
            else:
                if char_hash[i] < curr_start:
                    curr_len = curr_len + 1
                else:
                    curr_start = char_hash[i] + 1
                    curr_len = index - curr_start + 1
            if curr_len > max_len:
                max_len = curr_len
                start = curr_start
                end = index + 1
            char_hash[i] = index
        return max_len
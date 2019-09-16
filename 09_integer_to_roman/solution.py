class Solution(object):

    @staticmethod
    def covert(num, i):
        denom = {
            1 : "I",
            5 : "V",
            10 : "X",
            50 : "L",
            100 : "C",
            500 : "D",
            1000 : "M"
        }

        s = ""
        val = num / i

        if val < 4:
            for _ in range(val):
                s = s + denom[i]
        elif val == 4 or val == 9:
            s = s + denom[i] + denom[i * (val+1)] 
        elif val == 5 :
            s = s + denom[i*5]
        elif val > 5 :
            s = s + denom[i*5]
            for _ in range(val-5):
                s = s + denom[i]
        return s


    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        i = 10
        x = ""
        while i <= num:
            val = num % i
            num = num - val
            x = Solution.covert(val, i/10) + x
            i = i*10

        x = Solution.covert(num, i/10) + x
        return x
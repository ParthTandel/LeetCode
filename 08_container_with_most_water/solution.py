class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        index_start = 0
        index_end = len(height) - 1

        max_area = 0

        while(index_end > index_start):
            if height[index_end] > height[index_start]:
                area = height[index_start] * (index_end - index_start)
                index_start = index_start + 1
            else:
                area = height[index_end] * (index_end - index_start)
                index_end = index_end - 1
            
            max_area = max(area, max_area)

        return max_area
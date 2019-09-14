class Solution(object):        

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """ 
        a_len = len(nums1)
        b_len = len(nums2)
        partition = int(a_len + b_len + 1) 

        if a_len < b_len:
            nums1, nums2 , a_len, b_len= nums1, nums2, a_len, b_len
        else:
            nums1, nums2 , a_len, b_len= nums2, nums1, b_len, a_len
        

        start = 0
        end = a_len


        if a_len == 0:
            index = (b_len + 1) /2
            if b_len % 2 == 0:
                return float(nums2[index - 1] + nums2[index]) / 2 
            else:
                return float(nums2[index - 1])

        half_parition = int(partition / 2)
        while start <= end:

            partition_a = (start + end) / 2
            partition_b = half_parition - partition_a

            a_left = float("-inf") if partition_a == 0 else nums1[partition_a - 1]
            b_left = float("-inf") if partition_b == 0 else nums2[partition_b - 1]

            a_right = float("inf") if partition_a == a_len else nums1[partition_a]
            b_right = float("inf") if partition_b == b_len else nums2[partition_b]

            if a_left <= b_right  and b_left <= a_right:
                break
            
            if a_left > b_right:
                end = end - 1
            else:
                start = partition_a + 1


        if (partition - 1) % 2 == 0:
            return float(max(a_left,b_left) + min(a_right, b_right) )/ 2
        else:
            return float(max(a_left,b_left))
        






def main():
    arr1 = []
    arr2 = [1,2,3,4,5, 6]
    s = Solution()
    print(s.findMedianSortedArrays(arr1, arr2))


    arr1 = [8]
    arr2 = [8,9,10,11,12,13]
    s = Solution()
    print(s.findMedianSortedArrays(arr1, arr2))


if __name__ == "__main__":
    main()

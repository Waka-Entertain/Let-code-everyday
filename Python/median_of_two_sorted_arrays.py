"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        total_len = m + n
        half_pos = total_len>>1
        concat_sorted = []
        while len(concat_sorted) <= half_pos:
            if nums1 == [] or nums2 == []:
                concat_sorted = (concat_sorted + nums2 + nums1)[:half_pos + 1]
            elif nums1[0] <= nums2[0]:
                concat_sorted.append(nums1.pop(0))
            else:
                concat_sorted.append(nums2.pop(0))
        return concat_sorted[-1] if total_len % 2 else (concat_sorted[-1] + concat_sorted[-2]) / 2


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1, 2], [3, 4]))

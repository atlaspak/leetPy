class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if(n == 0):
            return
        if(m == 0):
            for i in range(n):
                nums1[i] = nums2[i]
            return
        total = len(nums1)
        idx1 = m-1
        idx2 = n-1
        for i in reversed(range(total)):
            if(idx1 != -1) and ((nums1[idx1] > nums2[idx2])):
                nums1[i] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[i] = nums2[idx2]
                nums2[idx2] = -sys.maxsize - 1
                idx2 -=1

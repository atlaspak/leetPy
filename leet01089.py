class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        tempArr = []
        for i in arr:
            tempArr.append(i)
            if(i == 0):
                tempArr.append(i)
        for idx,val in enumerate(arr):
            arr[idx] = tempArr[idx]

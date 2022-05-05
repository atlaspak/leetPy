class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key = lambda val: val[0])
        prev = intervals[0]
        
        for i in range(1, len(intervals)):
            if(prev[1] >= intervals[i][0]):
                if(prev[1] < intervals[i][1]):
                    prev[1] = intervals[i][1]
            else:
                result.append(prev[:])
                prev = intervals[i]
        
        result.append(prev[:])
        return result

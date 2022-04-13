class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapify(heap)
        
        for point in points:
            cur = (point[0]**2 + point[1]**2)
            heappush(heap, (cur, point))
        
        ret_val = []
        for i in range(k):
            ret_val.append(heappop(heap)[1])
        return ret_val

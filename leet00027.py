class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        que = deque()
        N = len(nums)
        count = 0
        for i in range(N):
            if(nums[i] == val):
                que.append(i)
            elif(que):
                new_pos = que.popleft()
                nums[new_pos] = nums[i]
                que.append(i)
                count += 1
            else:
                count += 1
        return count

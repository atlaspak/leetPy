class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ctr = Counter(nums)
        return ctr.most_common(1)[0][1] >= 2

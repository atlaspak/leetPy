class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        curr_min = prices[0]
        ret_val = 0
        
        for i in range(1, len(prices)):
            if prices[i] < curr_min:
                curr_min = prices[i]
            cur_price = prices[i] - curr_min
            if  cur_price > ret_val:
                ret_val = cur_price
        return ret_val

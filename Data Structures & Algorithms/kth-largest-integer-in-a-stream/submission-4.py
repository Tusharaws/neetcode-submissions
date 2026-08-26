class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(nums)
        # while len(self.min_heap)>self.k:
        #     heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)

        res = heapq.nlargest(self.k,self.min_heap)  
        
        return res[-1]

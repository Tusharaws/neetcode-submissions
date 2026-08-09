class Solution:
        def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
            if len(nums)<k:
                return []
            q = deque()
            max_arr = []
            for right in range(len(nums)):
                while q and nums[q[-1]]<=nums[right]:
                    q.pop()
                q.append(right)
                if q[0] < right - k + 1 :
                    q.popleft()

                if right>=k-1:
                    max_arr.append(nums[q[0]])  
            return max_arr
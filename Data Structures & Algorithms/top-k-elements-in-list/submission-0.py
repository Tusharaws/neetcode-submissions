class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)<k:
            return []
        count = {}
        for num in nums:
            count[num] = count.get(num,0)+1
        bucket = [[] for _ in range(len(nums)+1)]
        for num, freq in count.items():
            bucket[freq].append(num)
        result = []
        for freq in range(len(bucket)-1,0,-1):
            for num in bucket[freq]:
                result.append(num)
                if len(result) == k:
                    return result            
        
        # for num in nums:
        #     seen[num] +=1
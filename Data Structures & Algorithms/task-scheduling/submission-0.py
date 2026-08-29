class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_heap = [-f for f in freq.values()]
        heapq.heapify(max_heap)
        time = 0
        while max_heap:
            temp = []
            for _ in range(n+1):
                if max_heap:
                    temp.append(heapq.heappop(max_heap)+1)
            for count in temp:
                if count != 0:
                    heapq.heappush(max_heap,count)
            if max_heap:
                time += n+1
            else:
                time += len(temp)
        return time



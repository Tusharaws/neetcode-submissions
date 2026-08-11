class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures)<=1:
            return [0]
        result = [0]*len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp>temperatures[stack[-1]]:
                prev_temp = stack.pop() 
                result[prev_temp] = i - prev_temp 
            
            stack.append(i)
        return result

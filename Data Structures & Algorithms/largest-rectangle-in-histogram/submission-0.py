class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        max_area = 0
        for i, height in enumerate(heights):
            while stack[-1]!=-1 and height<=heights[stack[-1]]:
                h = heights[stack.pop()]
                width = i-stack[-1]-1
                max_area = max(max_area, width*h)
            stack.append(i)
        return(max_area)
        
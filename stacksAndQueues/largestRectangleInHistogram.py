def largestRectangleArea_brute(heights):
    n = len(heights)
    max_area = 0
    for i in range(n):
        h = heights[i]
        left = i
        right = i
        # expand left
        while left > 0 and heights[left - 1] >= h:
            left -= 1
        # expand right
        while right < n - 1 and heights[right + 1] >= h:
            right += 1
        width = right - left + 1
        max_area = max(max_area, h * width)
    return max_area

print(largestRectangleArea_brute([2,1,5,6,2,3]))  # 10
def largestRectangleArea_better(heights):
    n = len(heights)
    left, right = [-1]*n, [n]*n
    stack = []
    
    # Previous Smaller Element (PSE)
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)
    
    stack.clear()
    # Next Smaller Element (NSE)
    for i in range(n-1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)

    max_area = 0
    for i in range(n):
        max_area = max(max_area, heights[i] * (right[i] - left[i] - 1))
    return max_area
print(largestRectangleArea_better([2,1,5,6,2,3]))  # 10

def largestRectangleArea_optimal(heights):
    stack = []  # store indices
    max_area = 0
    heights.append(0)  # sentinel
    
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    heights.pop()  # cleanup
    return max_area
print(largestRectangleArea_optimal([2,1,5,6,2,3]))  # 10
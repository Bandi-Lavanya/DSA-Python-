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


def maximalRectangle(matrix):
    if not matrix:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    heights = [0] * n
    max_area = 0
    
    for i in range(m):
        for j in range(n):
            # Build prefix sum for "histogram heights"
            if matrix[i][j] == 1:
                heights[j] += 1
            else:
                heights[j] = 0
        print(heights)
        # Apply largest rectangle in histogram
        max_area = max(max_area, largestRectangleArea_better(heights))
    
    return max_area


# Example
matrix = [
    [1,0,1,0,1],
    [1,0,1,1,1],
    [1,1,1,1,1],
    [1,0,0,1,0]
]
print(maximalRectangle(matrix))  # Output: 6

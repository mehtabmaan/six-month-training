def largestRectangleArea(heights):
    stack = []
    max_area = 0
    heights.append(0) 

    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)

    heights.pop()
    return max_area


def maximalRectangle(matrix):
    if not matrix:
        return 0

    cols = len(matrix[0])
    heights = [0] * cols
    max_area = 0

    for row in matrix:
        for j in range(cols):
            if row[j] == '1':
                heights[j] += 1
            else:
                heights[j] = 0

        max_area = max(max_area, largestRectangleArea(heights))

    return max_area


n = int(input("Enter rows: "))
m = int(input("Enter cols: "))
print("Enter matrix rows (space-separated, e.g. 1 0 1 1 0):")
matrix = []
for _ in range(n):
    matrix.append(input().split())  

print("Output:", maximalRectangle(matrix))
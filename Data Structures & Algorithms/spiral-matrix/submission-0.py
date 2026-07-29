class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # 1. Move l->r: top row
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            # 2. Move t->b: right col
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # 3. Move r->l: bottom row
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            # 4. Move b->t: left col
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # 1. save t l
                top_left = matrix[top][l + i]

                # 2. move b l -> t l
                matrix[top][l + i] = matrix[bottom - i][l]

                # 3. move b r -> b l
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # 4. move t r -> b r
                matrix[bottom][r - i] = matrix[top + i][r]

                # 5. move t l -> t r
                matrix[top + i][r] = top_left

            r -= 1
            l += 1

        
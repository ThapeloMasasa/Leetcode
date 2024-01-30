# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

# Return the modified image after performing the flood fill.


def floodFill(image, sr, sc, color):
    stack =[(sr,sc)]
    store = set()
    row_len = len(image)
    col_len = len(image[0])
    check_color = image[sr][sc]
    def checkBoundaries(neighbor, len_row, len_col):
        row, col = neighbor[0], neighbor[1]
        if 0 <= row < len_row and 0<= col < len_col:
            return True
        else:
            return False
    while stack:
        row, col = stack.pop()
        image[row][col] = color
        store.add((row,col))
        top = (row - 1, col)
        bottom = (row + 1, col)
        left = (row, col - 1)
        right = (row, col + 1)
        for neighbor in [top, bottom, right, left]:
            if checkBoundaries(neighbor, row_len, col_len):
                if image[neighbor[0]][neighbor[1]] != check_color:
                    store.add((neighbor[0], neighbor[1]))
                else:
                    if (neighbor[0], neighbor[1]) not in store:
                        stack.append((neighbor[0], neighbor[1]))
    return image

#tests
#test1
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1 
sc = 1
color = 2
ans = floodFill(image, sr, sc, color)
print(ans)





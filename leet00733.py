class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        src_color = image[sr][sc]
        row_len = len(image)
        col_len = len(image[0])
        
        if(src_color == newColor):
            return image
        def fill(image, i, j):
            if(image[i][j] == src_color):
                image[i][j] = newColor
                if(j+1 < col_len):
                    fill(image, i, j+1)
                if(j-1 >= 0):
                    fill(image, i, j-1)
                if(i+1 < row_len):
                    fill(image, i+1, j)
                if(i-1 >= 0):
                    fill(image, i-1, j)
        fill(image, sr, sc)
        return image
        
    

#active recall
class Solution:
    #helper function
    def dfs(self, image, m, n, orig_color, new_color):
        if(m<0 or n<0 or m>=len(image) or n>= len(image[0]) or (image[m][n]!=orig_color) or (image[m][n]==new_color)) :
            return
        # if (image[m][n]!=orig_color):
        #     return
        # if (image[m][n]==new_color):
        #     return 
        
        image[m][n]=new_color
        self.dfs(image, m-1, n, orig_color, new_color)
        self.dfs(image, m+1, n, orig_color, new_color)
        self.dfs(image, m, n-1, orig_color, new_color)
        self.dfs(image, m, n+1, orig_color, new_color)

    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        # if (image[sr][sc]==color):
        #     return 
        self.dfs(image, sr, sc, image[sr][sc], color)
        return image


# class Solution(object):
#     def fill(self, image, sr, sc, color, cur):
#         # If sr is less than 0 or greater equals to the length of image...
#         # Or, If sc is less than 0 or greater equals to the length of image[0]...
#         if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]): return;
#         # If image[sr][sc] is not equal to previous color...
#         if cur != image[sr][sc]: return;
#         # Update the image[sr][sc] as a color...
#         image[sr][sc] = color;
#         # Make four recursive calls to the function with (sr-1, sc), (sr+1, sc), (sr, sc-1) and (sr, sc+1)...
#         self.fill(image, sr-1, sc, color, cur);
#         self.fill(image, sr+1, sc, color, cur);
#         self.fill(image, sr, sc-1, color, cur);
#         self.fill(image, sr, sc+1, color, cur);
#     def floodFill(self, image, sr, sc, color):
#         # Avoid infinite loop if the new and old colors are the same...
#         if image[sr][sc] == color: return image;
#         # Run the fill function starting at the position given...
#         self.fill(image, sr, sc, color, image[sr][sc]);
#         return image;


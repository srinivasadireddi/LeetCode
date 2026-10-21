# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Solution2:
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        def preorder(node):
            if(not node):
                return 'N'
            else:
                return '#'+str(node.val)+preorder(node.left)+preorder(node.right)
        
        string_small= preorder(subRoot)          
        string_big= preorder(root)
        return string_small in string_big
# TC=O(n) if python's string_small in string_big search is optimum or O(nm) if it does brute force like search
# SC=O(n) 


#Soln1 (incorrect): 106/185 cases passed by luck!
# class Solution:
#     def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        '''
        mistakes:
        1. string+='N' inside the helper creates a new local striNG, but string_big and string_small stay "". So we end up checking "" in "", which is True. That's why 106 cases passed by luck (expected answer was True).

        2. function can be cleaner

        3. use # at the beginning of every number, ELSE It can pass by mistake. orig code: [12] and [2] becomes 12NN and 2NN, new code: #12#N#N and #2#N#N
        '''

        # def preorder(string, node):
        #     if(not node):
        #         string+='N'
        #         return True
        #     else:
        #         string+=str(node.val)
        #     preorder(string, node.left)
        #     preorder(string, node.right)
        
        # string_big=""
        # string_small=""
        # preorder(string_big, root)          
        # preorder(string_small, subRoot)
        # if string_small in string_big:
        #     return True
        # else:
        #     return False
#TC=O(n) if python's string_small in string_big search is optimum or O(nm) if it does brute force like search
#SC=O(n) 
                  
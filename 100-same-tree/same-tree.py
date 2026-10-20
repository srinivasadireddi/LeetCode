# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        #soln 3:
        def same(p,q): #helper function
            if (not p and not q):
                return True
            if (not p or not q):
                return False
            if (p.val!=q.val):
                return False
            return same(p.left,q.left) and same(p.right,q.right)
            
        return same(p,q)
#TC:O(n+m)=O(n)
#SC:(h_p+ h_q)=O(h)























#         #my soln 2: 56/67 testcases passed
#         if(not p and not q):
#             return True 
#         if(not p or not q):
#             return False 
#         # if(p.val==q.val):
#         #     return True
#         if(p.val!=q.val):
#             return False

#         self.isSameTree(p.left, q.left)
#         if(not p.left or not q.left):
#             return False
#         if(p.left.val!=q.left.val):
#             return False
#         self.isSameTree(p.right, q.right)
#         if(not p.right or not q.right):
#             return False
#         if(p.right.val!=q.right.val):
#             return False
#         return True
# #TC:O(N)
# #SC:O(h)















        #my soln1-> fails cuz datatypes not compatible:
        # if(not p or not q):
        #     return False 
        # if(p.val!=q.val):
        #     return False
        # left_p=self.isSameTree(p.left)
        # left_q=self.isSameTree(q.left)
        # if(not left_p or not left_q):
        #     return False
        # if(left_p!=left_q):
        #     return False
        # right_p=self.isSameTree(p.right)
        # right_q=self.isSameTree(q.right)
        # if(not right_p or not right_q):
        #     return False
        # if(right_p!=right_q):
        #     return False
        
        # return True

        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#BFS does level order
# from collections import dequeue #need to import this in a non-leetcode envt
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        answer=[]
        queue=deque() #watch out for the spelling!!
        queue.append(root)
        while(queue):
            level=[]
            n=len(queue) #trick
            
            for i in range(n):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
            answer.append(level)
        return answer
# TC:O(n)
# SC:O(n). Also note that, at every new level, in the worst case, the number of nodes in that level is 2*the num of nodes in the prev level (eg: 2^30 nodes in level A, 2^31 (huge number) nodes in level A+1). The queue carries all the nodes in a level at a time, so it occupies a space of O(n).

        
        
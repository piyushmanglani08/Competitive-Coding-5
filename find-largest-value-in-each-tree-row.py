"""
Time - O(n)
Space - O(n)
"""
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        res = []
        q.append(root)
        if root == None:
            return []

        while q:
            
            max_element = float("-inf")
            size = len(q)
            
            for i in range(size):
                curr = q.popleft()
                
                max_element = max(curr.val,max_element)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            res.append(max_element)
    
        return res
    
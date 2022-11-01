#Time_Complexity: O(n)
#Space_Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:  
        
         
        #bfs method
        #if the root is not present 
        if not root:
            return []
        
        q=deque()
        #appending the root values  to queue
        q.append(root)
        
        #a new result array for storing result
        result=[]
        while q:
            #to find the each level we ned to find the size
            size=len(q)
            #iterating the node to each level
            for i in range(size):
                #deleting the queue and adding it to node
                node=q.popleft()
                #if the left node is present
                if node.left:
                    #then append it to the queue
                    q.append(node.left)
                if node.right:
                    #if node right is present then append it to queue 
                    q.append(node.right)
                    #adding the node value to result
            result.append(node.val)
        #returning the result
        return result

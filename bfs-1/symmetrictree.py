#Time_Complexity: O(n)
#Space_Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        q=deque()
        #appending the root values  to queue
        q.append(root)
    
        while q:
            #to find the each level we ned to find the size
            size=len(q)
            level=[]
            #iterating the node to each level
            for _ in range(size):
                #deleting the queue and adding it to node
                node=q.popleft()
                if node!=None:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    level.append(node)
            if not (self.ispalindrome(level)):
                return False
        return True
                    
        #finding the palindrome functiuon
    def ispalindrome(self,li):
        #using two pointer variable method
        left=0
        right=len(li)-1
        #if the left value and right are not same 
        while left<=right:
            if li[left]!=li[right]:
                return False
            #increment both the variables 
            left+=1
            right-=1  
        return True
        

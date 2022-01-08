# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#inorder means left -> root  -> right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        listOfNodes = []
        #recursive
        if root is None:
            print("Reached leaf node, nowhere to progress!")
            #return(listOfNodes)
        else:
            #print("currently at :",root.val)
            listOfNodes += self.inorderTraversal(root.left)
            listOfNodes.append(root.val)
            listOfNodes += self.inorderTraversal(root.right)
        return(listOfNodes)
      
   def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        listOfNodes = []
        #iterative
        if root is None:
            print("Nothing to process")
        else:
            traveresedNodeStack = []    #list of nodes to be traversed
            curr_node = root            #initialize to start from root
            
            #while we have nodes to process in stack or current node is not null
            while (len(traveresedNodeStack) > 0 or curr_node is not None) :
                
                if curr_node is not None:
                    #current node is not null, push to stack and traverse down left side of tree
                    #print("pushed ", curr_node.val)
                    traveresedNodeStack.append(curr_node)
                    curr_node = curr_node.left #going towards left side
                else:
                    #current node (.i.e left node of parent) is null, pop parent node and add to result list and move to right side of parent node.
                    curr_node = traveresedNodeStack.pop() #left node is null, pop back parent
                    #print("popped ",curr_node.val)
                    listOfNodes += [curr_node.val]
                    curr_node = curr_node.right #going towards right side
                
                #print("elements in stack: ", traveresedNodeStack, " current node: ", curr_node)
            return(listOfNodes)
      

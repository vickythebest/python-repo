from node import Node
class binaryTree(object):
    def __init__(self,root) -> None:
        self.root=Node(root)
    
    # Helper function to print
    def print_tree(self,travesal_type):
        # print("print tree")
        if travesal_type=="preorder":
            return self.preorder_print(tree.root,"")
        elif travesal_type=="inorder":
            return self.inorder_print(tree.root,"")
        elif travesal_type=="postorder":
            return self.postorder_print(tree.root,"")
        else:
            print("Traersal Type "+str(travesal_type)+"is not suported")

    def preorder_print(self,start,traversal):
        # print("preorder_print tree")
        """Root-->Left-->Right"""
        if start:
            traversal+=(str(start.value)+"-")
            traversal=self.preorder_print(start.left,traversal)
            traversal=self.preorder_print(start.right,traversal)
        return traversal

    def inorder_print(self,start,traversal):
        """Left-->Root-->Left"""
        # print("In Order")
        if start:
            traversal=self.inorder_print(start.left,traversal)
            traversal+=(str(start.value)+"-")
            traversal=self.inorder_print(start.right,traversal)
        return traversal
    
    def postorder_print(self,start,traversal):
        """Left-->Right-->Root"""
        if start:
            traversal=self.inorder_print(start.left,traversal)
            traversal=self.inorder_print(start.right,traversal)
            traversal+=(str(start.value)+"-")
        return traversal

tree = binaryTree(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.right.left=Node(6)
tree.root.right.right=Node(7)
# tree.root.right.right.right=Node(8)

print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
#定義樹節點
class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
#定義樹
class BinaryTree:
    def __init__(self,root_value):
        self.root = TreeNode(root_value)
    #獲取根節點
    def get_root(self):
        return self.root
    #插入節點
    def insert(self,value):
        self._insert_recursive(self.root,value)

    def _insert_recursive(self,current_node,value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self._insert_recursive(current_node.left,value)
        elif value>current_node.value:
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self._insert_recursive(current_node.right,value)
    #搜尋節點
    def search(self,value):
        return self._search_recursive(self.root,value)

    def _search_recursive(self,current_node,value):
        if current_node is None or current_node.value == value:
            return current_node
        if value<current_node.value:
            return self._search_recursive(current_node.left,value)
        return self._search_recursive(current_node.right,value)
    #打印
    def display_tree(self):
        self._display_tree_recursive(self.root,0)

    def _display_tree_recursive(self,node,level):
        if node is not None:
            self._display_tree_recursive(node.left,level+1)
            print(" "*level + str(node.value))
            self._display_tree_recursive(node.right,level+1)


binary_tree = BinaryTree(5)
binary_tree.insert(3)
binary_tree.insert(7)
binary_tree.insert(2)
binary_tree.insert(4)
binary_tree.insert(6)
binary_tree.insert(8)
binary_tree.display_tree()






def insert(value,node):
    if value < node.value:
        
        if node.leftChild is None:
            node.leftChild = TreeNode(value)
        else:
            insert(value,node.leftChild)
        
    elif value > node.value:
        if node.rightChild is Nont:
            node.rightChild = TreeNode(value)
        else:
            insert(value,node.rightChild)
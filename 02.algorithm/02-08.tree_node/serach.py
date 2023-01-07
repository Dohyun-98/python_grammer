def search(searchValue,node):

    if node is None or node.value == searchValue:
        return node
    
    elif searchValue < node.value :
        return search(searchValue,node.leftChild)

    else :
        return  search(searchValue,node.rightChild)
""" utility that create a new Node  
with the given key """


class NewNode:

    # Construct to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Function to find sum of all the element recursivly


def addBT(node):
    if (node == None):
        return 0
    return (node.key + addBT(node.left) +
            addBT(node.right))


# Driver Code
if __name__ == '__main__':
    root = NewNode(15)
    root.left = NewNode(10)
    root.right = NewNode(20)
    root.left.left = NewNode(8)
    root.left.right = NewNode(12)
    root.right.left = NewNode(16)
    root.right.right = NewNode(25)
    root.right.left.right = NewNode(16)

    sum = addBT(root)

    print(f"Sum of all the nodes is: {addBT(root)}")

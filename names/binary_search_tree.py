class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value: 
            if self.left == None: 
                self.left = BinarySearchTree(value)
            else: 
                return self.left.insert(value)
        elif value >= self.value: 
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                return self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True
        if target > self.value:
            if self.right is None:
                return False 
            else: 
                return self.right.contains(target)
        if target < self.value:
            if self.left is None:
                return False 
            else: 
                return self.left.contains(target)
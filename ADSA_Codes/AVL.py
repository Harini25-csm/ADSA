class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        return node.height if node else 0

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    def right_rotate(self, y):
        x, T2 = y.left, y.left.right
        x.right, y.left = y, T2
        y.height, x.height = max(self.height(y.left), self.height(y.right)) + 1, max(self.height(x.left), self.height(x.right)) + 1
        return x

    def left_rotate(self, x):
        y, T2 = x.right, x.right.left
        y.left, x.right = x, T2
        x.height, y.height = max(self.height(x.left), self.height(x.right)) + 1, max(self.height(y.left), self.height(y.right)) + 1
        return y

    def insert(self, node, key):
        if not node:
            return Node(key)

        if key < node.value:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.balance_factor(node)

        # Handling rotations
        if balance > 1 and key < node.left.value:
            return self.right_rotate(node)
        if balance < -1 and key > node.right.value:
            return self.left_rotate(node)
        if balance > 1 and key > node.left.value:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and key < node.right.value:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def delete(self, node, key):
        if not node:
            return node

        if key < node.value:
            node.left = self.delete(node.left, key)
        elif key > node.value:
            node.right = self.delete(node.right, key)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            temp = self.min_value_node(node.right)
            node.value = temp.value
            node.right = self.delete(node.right, temp.value)

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.balance_factor(node)

        # Handling rotations after deletion
        if balance > 1 and self.balance_factor(node.left) >= 0:
            return self.right_rotate(node)
        if balance < -1 and self.balance_factor(node.right) <= 0:
            return self.left_rotate(node)
        if balance > 1 and self.balance_factor(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and self.balance_factor(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def min_value_node(self, node):
        return node if not node.left else self.min_value_node(node.left)

    def inorder(self, node, result):
        if node:
            self.inorder(node.left, result)
            result.append(str(node.value))
            self.inorder(node.right, result)

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    def delete_key(self, key):
        self.root = self.delete(self.root, key)

    def in_order(self):
        result = []
        self.inorder(self.root, result)
        return result

    def print_tree(self):
        if not self.root:
            print("The tree is empty.")
        else:
            print("In-order traversal of the AVL tree:", " ".join(self.in_order()))

def menu():
    tree = AVLTree()
    input_file, output_file = 'input.txt', 'output.txt'

    try:
        with open(input_file, 'r') as file:
            for element in map(int, file.read().split()):
                tree.insert_key(element)
    except FileNotFoundError:
        print("Input file not found. The tree will be empty initially.")

    tree.print_tree()

    while True:
        print("\nAVL Tree Operations Menu:")
        print("1. Insert a new element")
        print("2. Delete an element")
        print("3. Exit and save to file")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            tree.insert_key(int(input("Enter the key to insert: ")))
            tree.print_tree()
        elif choice == '2':
            tree.delete_key(int(input("Enter the key to delete: ")))
            tree.print_tree()
        elif choice == '3':
            with open(output_file, 'w') as file:
                file.write(" ".join(tree.in_order()))
            print("Exiting and saving in-order traversal to output.txt.")
            break
        else:
            print("Invalid choice. Please choose again.")

menu()

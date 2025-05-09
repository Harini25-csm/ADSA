import random

ORDER = 5  # Define the order of the B-Tree

class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    def __init__(self):
        self.root = BTreeNode(True)

    def search(self, k, node=None):
        node = self.root if node is None else node
        i = 0
        while i < len(node.keys) and k > node.keys[i]:
            i += 1
        if i < len(node.keys) and k == node.keys[i]:
            return node, i
        return None if node.leaf else self.search(k, node.children[i])

    def insert(self, k):
        root = self.root
        if len(root.keys) == ORDER - 1:
            temp = BTreeNode()
            self.root = temp
            temp.children.insert(0, root)
            self._split_child(temp, 0)
            self._insert_non_full(temp, k)
        else:
            self._insert_non_full(root, k)

    def _insert_non_full(self, node, k):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(0)
            while i >= 0 and k < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = k
        else:
            while i >= 0 and k < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == ORDER - 1:
                self._split_child(node, i)
                if k > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], k)

    def _split_child(self, parent, i):
        t = ORDER // 2
        y = parent.children[i]
        z = BTreeNode(y.leaf)

        parent.children.insert(i + 1, z)
        parent.keys.insert(i, y.keys[t - 1])

        z.keys = y.keys[t:(ORDER - 1)]
        y.keys = y.keys[:t - 1]

        if not y.leaf:
            z.children = y.children[t:ORDER]
            y.children = y.children[:t]

    def delete(self, k):
        self._delete(self.root, k)
        if len(self.root.keys) == 0 and not self.root.leaf:
            self.root = self.root.children[0]

    def _delete(self, node, k):
        t = ORDER // 2
        i = 0
        while i < len(node.keys) and k > node.keys[i]:
            i += 1

        if i < len(node.keys) and node.keys[i] == k:
            if node.leaf:
                node.keys.pop(i)
            else:
                if len(node.children[i].keys) >= t:
                    pred = self._get_predecessor(node, i)
                    node.keys[i] = pred
                    self._delete(node.children[i], pred)
                elif len(node.children[i + 1].keys) >= t:
                    succ = self._get_successor(node, i)
                    node.keys[i] = succ
                    self._delete(node.children[i + 1], succ)
                else:
                    self._merge(node, i)
                    self._delete(node.children[i], k)
        elif not node.leaf:
            if len(node.children[i].keys) < t:
                self._fill(node, i)
            self._delete(node.children[i if i < len(node.keys) else i - 1], k)

    def _get_predecessor(self, node, i):
        cur = node.children[i]
        while not cur.leaf:
            cur = cur.children[-1]
        return cur.keys[-1]

    def _get_successor(self, node, i):
        cur = node.children[i + 1]
        while not cur.leaf:
            cur = cur.children[0]
        return cur.keys[0]

    def _merge(self, node, i):
        child = node.children[i]
        sibling = node.children[i + 1]
        child.keys.append(node.keys.pop(i))
        child.keys.extend(sibling.keys)
        if not child.leaf:
            child.children.extend(sibling.children)
        node.children.pop(i + 1)

    def _fill(self, node, i):
        if i != 0 and len(node.children[i - 1].keys) >= ORDER // 2:
            self._borrow_from_prev(node, i)
        elif i != len(node.keys) and len(node.children[i + 1].keys) >= ORDER // 2:
            self._borrow_from_next(node, i)
        else:
            self._merge(node, i if i != len(node.keys) else i - 1)

    def _borrow_from_prev(self, node, i):
        child, sibling = node.children[i], node.children[i - 1]
        child.keys.insert(0, node.keys[i - 1])
        if not child.leaf:
            child.children.insert(0, sibling.children.pop())
        node.keys[i - 1] = sibling.keys.pop()

    def _borrow_from_next(self, node, i):
        child, sibling = node.children[i], node.children[i + 1]
        child.keys.append(node.keys[i])
        if not child.leaf:
            child.children.append(sibling.children.pop(0))
        node.keys[i] = sibling.keys.pop(0)

    def print_tree(self, node=None, level=0):
        node = self.root if node is None else node
        print(f"Level {level}: {node.keys}")
        if not node.leaf:
            for child in node.children:
                self.print_tree(child, level + 1)

# --------------------------
# Demo: Insert 100 random elements
tree = BTree()
random_elements = random.sample(range(1, 1000), 100)
for elem in random_elements:
    tree.insert(elem)

print("B-Tree after inserting 100 random elements:")
tree.print_tree()

# Search test
search_key = random_elements[10]
print(f"\nSearching for {search_key}:")
found = tree.search(search_key)
print(f"Key {search_key} {'found' if found else 'not found'}.")

# Deletion test
delete_key = random_elements[20]
print(f"\nDeleting key {delete_key}")
tree.delete(delete_key)
tree.print_tree()

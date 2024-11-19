# Probably better to build N trees- or get this to work (works once; one iteration through all key headings, then won't display last heading).

import copy
import graphviz
from binary_search_tree import BinarySearchTree  # inorder_traversal is not used in this file because this results in skewed trees (ascending order)
from traversal_methods import levelorder_traversal


class N_Node:
    def __init__(self, key, headings: list[str], value=[]):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.next = []
        self.headings = headings
        self.key_heading = None
        for _ in self.headings:
            self.next.append(N_Node.Next())
    
    def add_dimension(self, heading: str, value: any) -> None:
        self.headings.append(heading)
        self.value.append(value)
        self.next.append(N_Node.Next())
    
    def add_value(self, heading: str, value: any) -> None:
        self.value[self.headings.index(heading)] = value
    
    def get_value(self, heading: str) -> any:
        return self.value[self.headings.index(heading)]

    def re_key(self, heading: str) -> bool:
        # manages self.next which saves left and right of previous heading
        self.next[self.headings.index(self.key_heading)].left = self.left
        self.next[self.headings.index(self.key_heading)].right = self.right
        self.key_heading = heading
        self.key = self.value[self.headings.index(heading)]
        self.left = self.next[self.headings.index(heading)].left
        self.right = self.next[self.headings.index(heading)].right

    class Next:
        def __init__(self, left=None, right=None):
            self.left = left
            self.right = right

class NdimBinarySearchTree(BinarySearchTree):
    # Constructor assigns an empty root, and headings (for N data)
    def __init__(self, headings: list[str]=[]):
        super().__init__()
        self.headings = headings
        self.key_heading = headings[0]
        self.headings_roots = dict()
        for h in self.headings:
            self.headings_roots.update({h:None})

    def add_dimension(self, heading: str):  # O(N)
        self._add_dim_rec(heading, self.root)  # recursive
    
    def _add_dim_rec(self, heading, relative_root: N_Node):  # recurses to O(N), N=|{subtree nodes}|
        if relative_root is not None:
            relative_root.add_dimension(heading, None)
    
    def add_value(self, key, heading, value):  # O(logN)
        searched_node = self.search(key)
        if searched_node is not None:
            searched_node.add_value(heading, value)
    
    def insert(self, n_node: N_Node):
        n_node.re_key(self.key_heading)  # keying the actual parameter to the current key of the tree
        super().insert(n_node)
    
    # # remove needs to remove from all current trees, the reference exists in each
    # #   remove from tree as-keyed, then re_key
    # def remove(self, tuple_to_remove: tuple) -> int:
    #     temp_root = copy.deepcopy(self.root)
    #     count = 0
    #     for h, i in zip(self.headings, range(len(self.headings))):
    #         self.root = self.headings_roots.get(h)
    #         super().remove(tuple_to_remove[i])
    #         count += 1
    #     return count

    def re_key(self, heading: str):
        all_nodes = levelorder_traversal(self.root)  # the root node is the same for all trees
        a_root = self.root
        self.headings_roots.update({self.key_heading:copy.deepcopy(a_root)})  # saves current root
        if self.headings_roots.get(heading) is not None:  # dict is initialized with value of None for all keys
            self.root = self.headings_roots.get(heading)
            for each_node in all_nodes:
                each_node.re_key(heading)
        else:
            # creates a new tree (root) that is saved the next time re_key is called
            self.key_heading = heading
            del self.root
            self.root = None
            for each_node in all_nodes:
                self.insert(each_node)  # re keys node

   ## graphviz code provided                                                                # # #
    # # Mac install how-to:
    # #  install graphviz executables to a folder (run installation .pkg),
    # #  add alias of folder to usr/local/bin,
    # #  pip install graphviz.
    def visualize_tree(self):  # O(N)
        """Visualizes the BST using Graphviz."""
        dot = graphviz.Digraph()
        self._add_nodes(dot, self.root)  # recursive
        return dot

    def _add_nodes(self, dot, node: N_Node):  # recurses to O(N)
        """a helper method that recursively adds nodes and edges to the Graphviz object."""
        if node:
            dot.node(str(node.key), f"{node.key_heading}: {node.key:.3f}")  # value is a tuple including key
            if node.left:
                dot.edge(str(node.key), str(node.left.key))
                self._add_nodes(dot, node.left)  # recursion
            # else:
            #     dot.edge(str(node.key), '//')
            if node.right:
                dot.edge(str(node.key), str(node.right.key))
                self._add_nodes(dot, node.right)  # recursion
            # else:
            #     dot.edge(str(node.key), '//')
   ##                                                                                       # # #
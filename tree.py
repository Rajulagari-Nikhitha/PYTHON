class Node:
    def __init__(self,data):
        self.data=data
        self.child=[]

    def add_child(self, child_node):
        self.child.append(child_node)

    def remove_child(self, child_node):
        self.child.remove(child_node)

class M_Ary_Tree:
    def __init__(self,data):
        self.root=Node(data)

    def push_child(self,p,c):
        p_node = self.find(self.root, p)
        if p_node:
            p_node.child.append(Node(c))
        else:
            print(f"Parent node with value {p} not found.")

    def find(self,node,data):
        if node.data == data:
            return node
        for i in node.child:
            f=self.find(i,data)
            if f:
                return f
        return None
    
    def dfs(self, node):
        if node is None:
            return
        print(node.data, end=" ")
        for child in node.child:
            self.dfs(child)

    def findnodeparent(self,value, node=None, parent=None):
        if node is None:
            node = self.root
        if node.data == value:
            return node, parent
        for i in node.child:
            found_node, found_parent = self.findnodeparent(value, i , node)
            if found_node:
                return found_node, found_parent
        return None, None

    def remove(self, val):
        rmvnode, parent = self.findnodeparent(val)
        if rmvnode is None:
            return None
        if parent:
            parent.remove_child(rmvnode)
        elif rmvnode == self.root:
            self.root = None
        return rmvnode
    
    def find_node(self, val, node=None):
        if node is None:
            node = self.root
        if node.data == val:
            return node
        for child in node.child:
            found_node = self.find_node(val, child)
            if found_node:
                return found_node
        return None
    
    def addBnch(self,val,branch):
        parent_node = self.find_node(val)
        if parent_node is None:
            return
        parent_node.add_child(branch)
        

if __name__ == "__main__":
    t = M_Ary_Tree(1)
    t.push_child(1, 2)
    t.push_child(1, 3)
    t.push_child(1, 4)
    t.push_child(1, 5)
    t.push_child(2, 6)
    t.push_child(6, 9)
    t.push_child(6, 10)
    t.push_child(4, 7)
    t.push_child(4, 8)
    t.push_child(7, 11)
    t.push_child(7, 12)
    t.push_child(11, 13)
    t.push_child(11, 14)

    print("DFS Traversal of the N-ary Tree:")
    t.dfs(t.root)

    a=int(input('Root node for removing branch'))
    branch=t.remove(a)
    print("\nRemaining Tree:")
    t.dfs(t.root)


    b=int(input('Node where branch is to be add'))
    t.addBnch(b,branch)
    print("\nResulted Tree:")
    t.dfs(t.root)

    

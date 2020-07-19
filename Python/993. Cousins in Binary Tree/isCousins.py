def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        out = []
        def search(root,depth,parent,looking_for):
            if root:
                if root.val == looking_for:
                    out.append((depth,parent))
                search(root.left,depth+1,root.val,looking_for)
                search(root.right,depth+1,root.val,looking_for)
        search(root,0,None,x)
        search(root,0,None,y)
        print(out)
        return out[0][0] == out[1][0] and out[0][1]!=out[1][1]


#IMPLEMENTAÇÃO DE UMA CLASSE QUE REPRESENTA A ÁRVORE BINÁRIA
class BSTNode (object):
    def __init__(self, key, value = None, left = None, right = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return '%s <- %s -> %s' % (self.left and self.left.key, self.key, self.right and self.right.key)


# IMPLEMENTAÇÃO DA SEGUINTE ÁRVORE NO OBJETO ROOT
#     (8)
#     / \
#   (7) (5)
#   /
# (3)

root = BSTNode(8)
root.left = BSTNode(7)
root.right = BSTNode(5)
root.left.left = BSTNode(3)

#EXIBIÇÃO DOS NÓS QUE ESTÃO LIGADOS COM O NÓ ROOT
print(root)







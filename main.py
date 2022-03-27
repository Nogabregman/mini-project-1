# username - complete info
# id1      - complete info
# name1    - complete info
# id2      - complete info
# name2    - complete info

def find_rank(node, i):
    rank = node.left.size + 1

    if rank == i:
        return node
    elif (i > rank):
        find_rank(node.right, i - rank)

    else:
        find_rank(node.left, i)


"""A class represnting a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type value: str
    @param value: data of your node
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1
        self.size = 0

    def isLeftSon(self):
    #returns true if node is the left son of it's parent, and false otherwise
        if self.parent.left==self:
            return True
        return False

    def switchSon(self, other): # a helper function for delete method
        if self.isLeftSon():
            self.parent.setLeft(other)
        else:  # the node is the right son
            self.parent.setRight(other)

    def retrieveNode(self, i):
        if i > self.size or i<1:
            return None
        if i == self.left.size + 1:
            return self
        if i <= self.left.size:
            return (self.left.retrieveNode(i))
        return (self.right.retrieveNode(i - self.left.size - 1))

    def min_son(self):
        tmp = self
        while (tmp.isRealNode()):
            tmp = tmp.left
        return tmp.parent

    def successor(self):
        if (self.right.isRealNode()):
            return (self.right.min_son())
        tmp = self.parent
        while (tmp!=None and self==tmp.right):
            self = tmp
            tmp = self.parent
        return tmp

    def insertSuccessor(self,new_node):
        if(self.right.isRealNode()==False):
            self.setRight(new_node)
        else:
            succ = self.successor()
            succ.setLeft(new_node)

    def insertFirst(self,new_node):
        node = self
        while(node.left.isRealNode()):
            node = node.left
        node.setLeft(new_node)

    def rotationLR(self):  # -1,2 situation
        father = self
        Lson = father.left
        LRson = Lson.right  # the future root
        # make the right son of LRson the left son of father
        father.left = LRson.right
        father.left.parent = father
        # make the right son of Lson the left son of LRson
        Lson.right = LRson.left
        Lson.right.parent = Lson
        # make LRson's parent the parent of the father. for making LR eventually the father
        LRson.parent = father.parent
        if father.parent != None:  # meaning the father wasn't the root, therefor his father pointer is not none
            if father.parent.left == father:  # meaning the father was a left child
                LRson.parent.left = LRson
            else:
                LRson.parent.right = LRson  # meaning the father was a right child

        # making  father the right son of LRson
        LRson.right = father
        LRson.right.parent = LRson
        # making Lson the left son of LRson
        LRson.left = Lson
        LRson.left.parent = LRson
        # rotation completed,
        # update sizes
        # update the size of Lson
        Lson.size = Lson.left.size + Lson.right.size + 1
        # update the size of father (now the right son of the rotate tree)
        father.size = father.left.size + father.right.size + 1
        # update height of father
        father.height = max(father.left.height, father.right.height) + 1
        # update the size of LRson (now the father after the rotation)
        LRson.size = LRson.left.size + LRson.right.size + 1
        # update the height of LRson
        LRson.height = Lson.height  # height of RLson (new father) does nor change again (because WE HAVE ALREADY UPDATED)  in RL /LR rotation example in the powerpoint lesson three
        Lson.height += -1
        return

    def rotationRL(self):  # 1 -2 situation
        father = self
        Rson = father.right
        RLson = Rson.left  # the future root
        # make the left son of RLson the right son of father
        father.right = RLson.left
        father.right.parent = father
        # make the left son of Rson the right son of RLson
        Rson.left = RLson.right
        Rson.right.parent = Rson
        # make the RLson's parent the parent of the father. for making RL eventually the father
        RLson.parent = father.parent
        if father.parent != None:  # meaning the father wasn't the root, there fore his father pointer is not none
            if father.parent.left == father:  # meaning the father was a left child
                RLson.parent.left = RLson
            else:
                RLson.parent.right = RLson  # meaning the father was a right child

        # making  father the left son of RLson
        RLson.left = father
        RLson.left.parent = RLson
        # making Rson the right son of RLson
        RLson.right = Rson
        RLson.right.parent = RLson
        # rotation completed,
        # update sizes
        # update the size of Lson
        Rson.size = Rson.left.size + Rson.right.size + 1
        # update the size of father (now the right son of the rotate tree)
        father.size = father.left.size + father.right.size + 1
        # update the fathers height
        father.height = max(father.left.height, father.right.height) + 1
        # update the size of RLson (now the father after the rotation)
        RLson.size = RLson.left.size + RLson.right.size + 1
        # update the height of RLson
        RLson.height = Rson.height  # RLson height, (the new father) of the tree does not change again because (WE HAVE ALREADY UPDATED) in RL/LR rotation example in the powerpoint lesson three
        Rson.height += -1

    def rotationRR(self):  # 1 2 situation like in the presentation!!!!
        father = self
        Lson = father.left  # the future father

        # making the father's left son the -  right son of of Lson
        father.left = Lson.right
        father.left.parent = father
        # making father as the right son of Lson
        Lson.right = father
        Lson.parent = father.parent
        if father.parent != None:  ## meaning the father wasn't the root, there fore his father pointer is not none
            if father.parent.left == father:
                Lson.parent.left = Lson
            else:
                Lson.parent.right = Lson
        # making father the right son of Lson
        father.parent = Lson
        # rotation completed!

        # update size of father (ther height didnt change)
        father.size = father.left.size + father.right.size + 1
        # update the height of father
        father.height = max(father.left.height, father.right.height) + 1
        # update the size of Lson (the present father)
        Lson.size = Lson.left.size + Lson.right.size + 1
        # update the height of Lson
        Lson.height = max(Lson.right.height, Lson.left.height) + 1  # not nessesary we could do this another way

    def rotationLL(self):  # 1 2 situation like in the presentation!!!!
        father = self
        Rson = father.right  # the future father

        # making the father's right son the -  left son of of Rson
        father.right = Rson.left
        father.right.parent = father
        # making father as the left son of Rson
        Rson.left = father
        Rson.parent = father.parent
        if father.parent != None:  ## meaning the father wasn't the root, there fore his father pointer is not none
            if father.parent.left == father:
                Rson.parent.left = Rson
            else:
                Rson.parent.right = Rson
        # making father the left son of Rson
        father.parent = Rson
        # rotation completed!

        # update size of father (ther height didnt change)
        father.size = father.left.size + father.right.size + 1
        # update the height of father
        father.height = max(father.left.height, father.right.height) + 1
        # update the size of Lson (the present father)
        Rson.size = Rson.left.size + Rson.right.size + 1
        # update the height of Lson
        Rson.height = max(Rson.right.height, Rson.left.height) + 1  # not nessesary we could do this another way
        return

        """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child
    """

    def getLeft(self):
        if self.height == -1:
            return None
        return self.left

    def create_node(self, val):
        self.value = val
        self.size += 1
        self.height += 1

        self.left = AVLNode(None)  # create 2 virtual nodes
        self.left.parent = self

        self.left.left = AVLNode(None)
        self.left.left.parent = self.left

        self.left.right = AVLNode(None)
        self.left.right.parent = self.left

        self.right = AVLNode(None)
        self.right.parent = self

        self.right.left = AVLNode(None)
        self.right.left.parent = self.right

        self.right.right = AVLNode(None)
        self.right.right.parent = self.right
        return

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child
    """

    def getRight(self):
        if self.height == -1:
            return None
        return self.right

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    def getParent(self):
        if self.height == -1:
            return None
        return self.parent

    """return the value

    @rtype: str
    @returns: the value of self, None if the node is virtual
    """

    def getValue(self):
        if self.height == -1:
            return None
        return self.value

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    def getHeight(self):
        return self.height

    """sets left child

    @type node: AVLNode
    @param node: a node
    """

    def setLeft(self, node):  # note to self: we are not sure what is supposed to be here, see forum
        self.left = node  # making the node as the left son of self
        node.parent = self
        '''node.height = 0
        node.size = 1
        node.right = AVLNode(None) #making node a father of two NONE babies
        node.right.value = None
        node.left = AVLNode(None)
        node.left.value = None'''

    """sets right child

    @type node: AVLNode
    @param node: a node
    """

    def setRight(self, node):
        self.right = node  # making the node as the right son of self
        node.parent = self

    """sets parent

    @type node: AVLNode
    @param node: a node
    """

    def setParent(self, node):
        self.parent = node

    """sets value

    @type value: str
    @param value: data
    """

    def setValue(self, value):
        self.value = value

    """sets the balance factor of the node

    @type h: int
    @param h: the height
    """

    def setHeight(self, h):
        self.height = h

    def balancefactor(self):
        return self.left.getHeight() - self.right.getHeight()

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def isRealNode(self):
        if self.height == -1:
            return False
        return True


"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):
    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):
        self.root = AVLNode(None)
        self.len = 0

    """returns whether the list is empty

    @rtype: bool
    @returns: True if the list is empty, False otherwise
    """

    def empty(self):
        if self.root.height == -1:
            return True
        return False

    """retrieves the value of the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: str
    @returns: the the value of the i'th item in the list
    """

    def retrieve(self, i):
        return self.retrieveNode(i).value

    def retrieveNode(self,i):
        if self.empty():
            return
        return self.root.retrieveNode(i+1)

    """inserts val at position i in the list

    @type i: int
    @pre: 0 <= i <= self.length()
    @param i: The intended index in the list to which we insert val
    @type val: str
    @param val: the value we inserts
    @rtype: list
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def insert(self, i, val):
        if self.empty():  # we the first node to an empty list
            self.root.value = val
            self.root.size += 1
            self.root.height += 1

            self.root.left = AVLNode(None)  # create 2 virtual nodes
            self.root.left.parent = self.root

            self.root.left.left = AVLNode(None)
            self.root.left.left.parent = self.root.left

            self.root.left.right = AVLNode(None)
            self.root.left.right.parent = self.root.left

            self.root.right = AVLNode(None)
            self.root.right.parent = self.root

            self.root.right.left = AVLNode(None)
            self.root.right.left.parent = self.root.right

            self.root.right.right = AVLNode(None)
            self.root.right.right.parent = self.root.right
            return

        else:

            # we are inserting the node as normal bst
            new_node = AVLNode(val)
            new_node.create_node(val)

            if(i>0):
                node = self.retrieveNode(i-1)
                node.insertSuccessor(new_node)
            else:
                self.root.insertFirst(new_node)
            node = new_node.parent
            tmp = new_node
            while (node.parent != None):  # update size and height
                node.size = node.left.size + node.right.size + 1
                node.height = max(node.left.height, node.right.height) + 1
                if node.balancefactor() == 2:
                    if tmp.balancefactor() == 1:  # this is rotation 1 2
                        node.rotationRR()
                        print('RRrotation')
                        node = tmp.parent  # going up
                    else:  # this is rotation -1 2
                        node.rotationLR()
                        print('LRrotaion')
                        tmp = tmp.parent  # going up
                        node = tmp.parent
                elif (node.balancefactor() == -2):
                    if tmp.balancefactor() == -1:  # this is rotation -1 -2
                        node.rotationLL()
                        print('LLrotation')
                        node = tmp.parent  # going up
                    else:
                        node.rotationRL()  # this is rotation 1 -2
                        print('RLrotaion', )
                        tmp = tmp.parent
                        node = tmp.parent

                else:
                    tmp = node
                    node = node.parent
                # print(tmp.value,'tmp',node.value,'node')
            # we have reached the root

            # print('root')
            node.size = node.left.size + node.right.size + 1
            node.height = max(node.left.height, node.right.height) + 1
            # print('node is:',node.value,'size',node.size,'height',node.height,'balancefactor:',node.balancefactor())
            if node.balancefactor() == 2:
                if tmp.balancefactor() == 1:  # this is rotation 1 2
                    node.rotationRR()
                    node = tmp.parent  # going up
                    self.root = tmp
                else:  # this is rotation -1 2
                    node.rotationLR()
                    tmp = tmp.parent  # going up
                    node = tmp.parent
                    self.root = tmp
            elif (node.balancefactor() == -2):
                if tmp.balancefactor() == -1:  # this is rotation -1 -2
                    node.rotationLL()
                    node = tmp.parent  # going up
                    self.root = tmp
                else:
                    node.rotationRL()  # this is rotation 1 -2
                    tmp = tmp.parent
                    node = tmp.parent
                    self.root = tmp
            else:
                tmp = node
                node = node.parent
                # print(tmp.left.height)
                self.root = tmp
            # print('halav')
            return

    """deletes the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list to be deleted
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, i):
        node=self.retrieveNode(i)
        # there are 3 scenarios, the node has no sons, 1 son or 2 sons. we will now face each of them:
        if not node.left.isRealNode() and not node.right.isRealNode(): #the node has no sons
            node.switchSon(AVLNode(None))
            # we still need to fix the sizes and the heights recursively!
            # I was thinking we could make an helper function that would do it and use it both here and in insert
        elif not node.left.isRealNode(): #node only has right son
            node.switchSon(node.right)
        elif not node.right.isRealNode(): #node only had left son
            node.switchSon(node.left)
        else: #node has 2 sons
            successor=node.successor()
            successorparent = successor.getParent()
            successor.switchSon(AVLNode(None))
            node.switchSon(successor)




    """returns the value of the first item in the list

    @rtype: str
    @returns: the value of the first item, None if the list is empty
    """

    def first(self):
        return self.root.min_son().value

    """returns the value of the last item in the list

    @rtype: str
    @returns: the value of the last item, None if the list is empty
    """

    def last(self):
        return None

    """returns an array representing list 

    @rtype: list
    @returns: a list of strings representing the data structure
    """

    def listToArray(self):
        return None

    """returns the size of the list 

    @rtype: int
    @returns: the size of the list
    """

    def length(self):
        return None

    """splits the list at the i'th index

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list according to whom we split
    @rtype: list
    @returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
    right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
    """

    def split(self, i):
        return None

    """concatenates lst to self

    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def concat(self, lst):
        return None

    """searches for a *value* in the list

    @type val: str
    @param val: a value to be searched
    @rtype: int
    @returns: the first index that contains val, -1 if not found.
    """

    def search(self, val):
        return None

    """returns the root of the tree representing the list

    @rtype: AVLNode
    @returns: the root, None if the list is empty
    """


def test2():
    t = AVLTreeList()
    t.insert(0, 3)
    t.insert(1, 2)
    t.insert(0, 4)
    t.insert(1, 5)
    t.insert(1, 7)
    t.insert(3, 9)
    t.insert(0, 13)

    print('root:', 'node:  ', t.root.value, 'node balancefactor', t.root.balancefactor(), 'size', t.root.size)
    print('\n')
    print('root.left', 'node:  ', t.root.left.value, 'node balancefactor', t.root.left.balancefactor(), 'size',
          t.root.left.size)
    print('root.left.left', 'node:  ', t.root.left.left.value, 'node balancefactor', t.root.left.left.balancefactor(),
          'size', t.root.left.left.size)
    print('root.left.right', 'node:  ', t.root.left.right.value, 'node balancefactor',
          t.root.left.right.balancefactor(), 'size', t.root.left.right.size)
    print('\n')
    print('root.right', 'node:  ', t.root.right.value, 'node balancefactor', t.root.right.balancefactor(), 'size',
          t.root.right.size)
    print('root.right.left', 'node:  ', t.root.right.left.value, 'node balancefactor',
          t.root.right.left.balancefactor(), 'size', t.root.right.left.size)
    print('root.right.right', 'node:  ', t.root.right.right.value, 'node balancefactor',
          t.root.right.right.balancefactor(), 'size', t.root.right.right.size)


def test():
    t = AVLTreeList()
    t.insert(0, 3)
    t.insert(1, 2)
    t.insert(0, 4)
    t.insert(1, 5)
    t.insert(2, 7)

    # tree before:

    # 3
    # 4                #2
    # 5

    # 7

    # tree after:

    # 3
    # 5              #2

    # 4          #7

    print('node:  ', t.root.value, 'node balancefactor', t.root.balancefactor(), 'size', t.root.size)
    print('node:  ', t.root.left.value, 'node balancefactor', t.root.left.balancefactor(), 'size', t.root.left.size)
    print('node:  ', t.root.right.value, 'node balancefactor', t.root.right.balancefactor(), 'size', t.root.right.size)
    print('node:  ', t.root.left.left.value, 'node balancefactor', t.root.left.left.balancefactor(), 'size',
          t.root.left.left.size)
    print('node:  ', t.root.left.right.value, 'node balancefactor', t.root.left.right.balancefactor(), 'size',
          t.root.left.right.size)


# test()
test2()
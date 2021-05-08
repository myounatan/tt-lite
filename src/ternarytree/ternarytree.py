
from collections import defaultdict
import time

# toggle to see Minimize output process to the console
DEBUG = False
 
class TTNode:
    '''
    Ternary Tree class
    '''

    def __init__(self, bitlevel=0):
        '''
        the ternary tree is represented as follows:
        
        leaf: []
        tree: [left (lo), centre (dc), right (hi)]
        '''
        self.lo = None
        self.dc = None
        self.hi = None
        
        self.val = ''
        
        self.bitlevel = bitlevel
        
    def insert(self, term, level=0):
        c = term[level]
        n = len(term) - 1
        
        '''
        c is either '0', '-', '1'
        '''
        
        if c == '0':
            if self.lo == None:
                self.lo = TTNode(bitlevel=level)
                self.lo.val = c
            if level < n:
                level += 1
                self.lo.insert(term, level=level)
        elif c == '-':
            if self.dc == None:
                self.dc = TTNode(bitlevel=level)
                self.dc.val = c
            if level < n:
                level += 1
                self.dc.insert(term, level=level)
        elif c == '1':
            if self.hi == None:
                self.hi = TTNode(bitlevel=level)
                self.hi.val = c
            if level < n:
                level += 1
                self.hi.insert(term, level=level)
                
    def is_leaf(self):
        return (self.lo == None and self.dc == None and self.hi == None)
    
    def show(self, level=1, max=1):
        if level == 1:
            print('\nTREE:')
            
        if self.lo != None:
            print('   '*(max-level) + 'lo: 0')
            self.lo.show(level=level+1, max=max)
        if self.dc != None:
            print('   '*(max-level) + 'dc: -')
            self.dc.show(level=level+1, max=max)
        if self.hi != None:
            print('   '*(max-level) + 'hi: 1')
            self.hi.show(level=level+1, max=max)
    


def CreateTernaryTree(filename=None, a=None):
    '''
    Accepts file where each line is a term
    first line is the number of variables
    ex:

    3
    001
    01-
    111
    '''

    tree = TTNode()
    iterations = 0
    
    if filename:
        with open(filename, 'r') as input_file:
            lines = [line for line in input_file.read().strip().split('\n')]
            iterations = int(lines[0])
            
            lines = lines[1::]
            for line in lines:
                tree.insert(line)
    else:
        iterations = len(a[0])
        
        for line in a:
            tree.insert(line)
    
    return tree, iterations

   
def MergeLeaves(node):
    if node.is_leaf():
        return
    
    if (node.lo != None and node.dc == None and node.hi != None) and (node.lo.is_leaf() and node.hi.is_leaf()):
        oldlevel = node.hi.bitlevel
        node.lo = None
        node.hi = None
        node.dc = TTNode(bitlevel=oldlevel)
    else:
        if node.lo != None:
            MergeLeaves(node=node.lo)
        if node.dc != None:
            MergeLeaves(node=node.dc)
        if node.hi != None:
            MergeLeaves(node=node.hi)

   
def AppendAll(c, node, originallevel):
    if node == None:
        return
    
    if node.is_leaf():
        if c == '0':
            node.lo = TTNode(bitlevel=originallevel)
        elif c == '-':
            node.dc = TTNode(bitlevel=originallevel)
        elif c == '1':
            node.hi = TTNode(bitlevel=originallevel)
        return
    
    if node.lo != None:
        AppendAll(c, node.lo, originallevel)
    if node.dc != None:
        AppendAll(c, node.dc, originallevel)
    if node.hi != None:
        AppendAll(c, node.hi, originallevel)


def MergeTrees(t1, t2):
    if t1 == None:
        return t2
    if t2 == None:
        return t1
    
    t1.lo = MergeTrees(t1.lo, t2.lo)
    t1.dc = MergeTrees(t1.dc, t2.dc)
    t1.hi = MergeTrees(t1.hi, t2.hi)
    
    return t1
           
def Rotate(tree):
    lo_node = tree.lo
    dc_node = tree.dc
    hi_node = tree.hi
    
    if lo_node != None:
        AppendAll('0', lo_node, lo_node.bitlevel)
        
    if dc_node != None:
        AppendAll('-', dc_node, dc_node.bitlevel)
        
    if hi_node != None:
        AppendAll('1', hi_node, hi_node.bitlevel)
    
    return MergeTrees(lo_node, MergeTrees(dc_node, hi_node))
    


def traverse(tree, a, s=defaultdict(str), ch=''):
    if tree == None:
        return
    
    s[tree.bitlevel] = ch
    
    if tree.is_leaf():
        state = ''
        for _, c in s.items():
            state += c
        a.append(state)
        
    if tree.lo:
        traverse(tree.lo, a, s, '0')
    if tree.dc:
        traverse(tree.dc, a, s, '-')
    if tree.hi:
        traverse(tree.hi, a, s, '1')
       
           
def Minimize(filename=None, a=None):
    tick = time.time()
    tree, iterations = CreateTernaryTree(filename=filename, a=a)
    
    for _ in range(0,iterations+2):
        if DEBUG:
            tree.show(max=iterations)

        MergeLeaves(tree)

        if DEBUG:
            tree.show(max=iterations)

        newtree = Rotate(tree)
        tree = None
        tree = newtree
    
    states = []
    traverse(tree, states)
    
    return states, time.time() - tick

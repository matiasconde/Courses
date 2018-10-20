from drawtree2 import draw_level_order, draw_bst


def get_sample_struct(n):
    return map(lambda i: str(i), range(n - 1))

def struct(nums):
    data = '{%s}' % (','.join(nums))
    draw_level_order(data)

import math

# depth of the node on the tree, given the index known as the position on the BinaryHeap

def depth(i):
        return int(math.log(i + 1, 2))

    # x_depth represents the horizontal shift on the current node's depth level
def x_depth(i):
        return int(i - math.pow(2, depth(i)) + 1)

    # n_depth refers to the amount of nodes per depth level, for example at level 0, n_depth=1 (the root)
def n_depth(i):
        return pow(2, depth(i))

    # x_rel_depth refers to a float number between 0 and 1, representing how close to the left (0) or right (1) it is.
def x_rel_depth(i):
        return x_depth(i) / float(n_depth(i))

    # i_parent is the parent's index of the given node index (this formula can be found in Wikipedia)
def i_parent(i):
        return (i - 1) / 2

import pandas as pd

dataframe = pd.DataFrame(columns=('i', 'num', 'depth', 'n by depth', 'x depth', 'x rel depth', 'i parent'))

for i in range(0, 31):
    num = draw_bst[i]
    dataframe.loc[i] = [i, num, depth(i), n_depth(i), x_depth(i), x_rel_depth(i), i_parent(i)]



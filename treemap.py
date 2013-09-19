import heapq
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import random

random.seed(17315113)


class TreeMap(object):

    def __init__(self):
        pass

    def build(self, dictinput):
        value_sum = float(sum(dictinput.values()))
        trees = [(v / value_sum, k) for k, v in dictinput.iteritems()]
        heapq.heapify(trees)
        while len(trees) > 1:
            left = heapq.heappop(trees)
            right = heapq.heappop(trees)
            heapq.heappush(trees, (right[0] + left[0], right, left))
        self.trees = trees[0]

    @classmethod
    def is_leaf(cls, node):
        return len(node) == 2

    def plan(self, width=1.0, height=1.0):
        plan_map = []
        self._plan(self.trees, (0.0, 0.0), width, height, plan_map)
        return plan_map

    @classmethod
    def _plan(cls, trees, lower, width, height, plan_map):
        if cls.is_leaf(trees):
            plan_map.append((trees, lower, width, height))
        else:
            r1, r2 = trees[1][0] / (trees[1][0] + trees[2][0]), trees[2][0] / (trees[1][0] + trees[2][0])
            if width >= height:
                lower1 = lower
                lower2 = (lower[0] + width * r1, lower[1])
                width1, height1 = width * r1, height
                width2, height2 = width * r2, height
            else:
                lower2 = lower
                lower1 = (lower[0], lower[1] + height * r2)
                width1, height1 = width, height * r1
                width2, height2 = width, height * r2

            cls._plan(trees[1], lower1, width1, height1, plan_map)
            cls._plan(trees[2], lower2, width2, height2, plan_map)


if __name__ == '__main__':
    data = {'a': 40, 'b': 80, 'c': 10, 'd': 30, 'e': 20, 'f': 25, 'g': 15}
    treeMap = TreeMap()
    treeMap.build(data)
    plan_map = treeMap.plan()

    ax = plt.subplot(111, aspect='equal')
    for node, lower, width, height in plan_map:
#         print node, lower, width, height
        r = Rectangle(lower, width, height, edgecolor='k', facecolor=
                      ((random.random(),random.random(),random.random())))
        ax.add_patch(r)

    plt.show()

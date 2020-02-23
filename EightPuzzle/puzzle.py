import random
import numpy as np

class Node:
    def __init__(self, node_no, data, parent, act, cost):
        self.data = data
        self.parent = parent
        self.act = act
        self.node_no = node_no
        self.cost = cost


def generatePuzzle():
    randArray = random.sample(range(0,9),9)
    if (check_solvable(randArray) == False):
        return generatePuzzle()
    return randArray
    
    

    
def check_solvable(g):
    arr = np.reshape(g, 9)
    counter_states = 0
    for i in range(9):
        if not arr[i] == 0:
            check_elem = arr[i]
            for x in range(i + 1, 9):
                if check_elem < arr[x] or arr[x] == 0:
                    continue
                else:
                    counter_states += 1
    check = counter_states % 2 == 0
    return check

for i in range(3):
    k = generatePuzzle()
    print(k)
    print(type(k))
    #root = Node(0, k, None, None, 0)

    



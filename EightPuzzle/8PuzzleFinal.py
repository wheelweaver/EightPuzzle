""" 8 Puzzle BFS algorithm
 Input the unsolved puzzle and the program
 solves it and creates 3 txt files with solutions"""

import random
import numpy as np
import time

goal_node = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])  # GOAL STATE

""" NODE CLASS
Holds Node information that will be used by A* and BFS algorithm
"""

class Node:
    """Initlializes node variables including node number, node data, parent, action,
        cost, level, and final value from heuristic function"""
    
    def __init__(self, node_no, data, parent, act, cost, level, fval):
        self.data = data
        self.parent = parent
        self.act = act
        self.node_no = node_no
        self.cost = cost
        self.level = level
        self.fval = fval
        
    """ Generate child nodes from the current node by chaging the 0 either
            of four directions [down,up,left,right] """
    def aStarChild(self):
        x, y = find_index(self.data)
        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]] # Represents possible moves
        children = []
        for i in val_list:
            child = self.changePositionAStar(self.data,x,y,i[0],i[1]) # Positions are moved for each node if move is possible
            if child is not None:
                child_node = Node(0,child,0,0,0,self.level+1,0)
                children.append(child_node)
        return children

    """ Exchanges 0 position for all possible moves for a*"""
    def changePositionAStar(self,puz,x1,y1,x2,y2):
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None
        """Copies matrix"""
    def copy(self,root):
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp
		
"""Looks for the 0 in matrix"""
def find_index(puzzle):
    puzzle = np.asarray(puzzle)
    result= np.where(puzzle == 0)
    return result[0][0], result[1][0]

"""Prints the final solution"""
def print_states(list_final): 
    print("BFS\n")
    for l in list_final:
        print("\n" + str(l.data))

"""Finds the correct path for BFS """

def path(node):  
    correctPath = []  # Empty list
    correctPath.append(node)
    parent_node = node.parent
    while parent_node is not None:
        correctPath.append(parent_node)
        parent_node = parent_node.parent
    return list(reversed(correctPath))

""" Exchanges 0 position for all possible moves for BFS"""
def shuffle(data,x1,y1,x2,y2):
        if x2 >= 0 and x2 < len(data) and y2 >= 0 and y2 < len(data):
            temp_puz = []
            temp_puz = np.copy(data)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp

            return temp_puz
        else:
            return None

"""BFS For each possible move starting from root  node,we find the avaliable position,
as we do so we put the current node at the end of a quene. Then we read the quene to make
furthuer children nodes"""

def bfsSearch(node):
    print("BFS SEARCH: ")
    actions = ["down", "up", "left", "right"] # All possible moves
    node_q = [node]
    final_nodes = []
    visited = []
    final_nodes.append(node_q[0].data.tolist())  # Only writing data of nodes in seen
    node_counter = 0  # To define a unique ID to all the nodes formed

    while node_q:
        current_root = node_q.pop(0)  # Pop the element 0 from the list
        if current_root.data.tolist() == goal_node.tolist():
            return current_root, final_nodes, visited
        x, y = find_index(current_root.data)
        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]   # 2 3 1 3

        #for move in actions:
        for i in val_list:
            #temp_data = move_tile(move, current_root.data)
            temp_data = shuffle(current_root.data,x,y,i[0],i[1])
            if temp_data is not None:
                node_counter += 1
                child_node = Node(node_counter, np.array(temp_data), current_root, i, 0, current_root.level+1, 0)  # Create a child node

                if child_node.data.tolist() not in final_nodes:  # Add the child node data in final node list
                    node_q.append(child_node)
                    final_nodes.append(child_node.data.tolist())
                    visited.append(child_node)
                    if child_node.data.tolist() == goal_node.tolist():
                        return child_node, final_nodes, visited
    return None, None, None  # return statement if the goal node is not reached

""" Generates Solvable Matrix"""
def generatePuzzle():
    n = 3
    
    k = np.array(final)
    if (check_solvable(randArray) == False):
        return generatePuzzle()
    randArray = random.sample(range(0,9),9)
    final = [randArray[i * n:(i + 1) * n] for i in range((len(randArray) + n - 1) // n )]
    return final

""" Checks whether generated input is sovable """
def check_solvable(g):
    array = np.reshape(g, 9)
    counter_states = 0
    for i in range(9):
        if not array[i] == 0:
            check_elem = array[i]
            for x in range(i + 1, 9):
                if check_elem < array[x] or array[x] == 0:
                    continue
                else:
                    counter_states += 1
    if counter_states % 2 == 0:
        print("This is solveable")
    else:
        print("The puzzle is not sovable (sad face).")
        

"""Holds the start of program. We take the generated node to run either a* or BFS.
Contains logic behind a* and calls the logic of BFS algo"""

class Algo(object):
    def __init__(self,size):
        self.size = size

    def tempInput(self):        
        my_list = [1, 8, 2, 0, 4, 3, 7, 6, 5]
        #my_list = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        n = 3
        final = [my_list[i * n:(i + 1) * n] for i in range((len(my_list) + n - 1) // n )]
        k = np.array(final)
        check_solvable(k)
        return k
    """Calculates the hueristic value by adding the nodes level and huerisitc function"""
    
    def g(self,start,goal):
        return self.h(start.data,goal)+start.level
    
    """Compares the start and final states to calcuate number of displaced tiles"""
    def h(self,start, goal):
        temp = 0
        for i in range(0,self.size):
            for j in range(0,self.size):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp

    """For each node we calcualted the heurisitic total. The one with lowest score we create
        children nodes of"""    
    def aStar(self):
        print("A* SEARCH: ")
        openn = []
        closed = []
        k = self.getFromUser()
        root = Node(0,k, None, None, 0, 0, 0)
        root.fval = self.g(root,goal_node)
        openn.append(root)
        while True:
            cur = openn[0]
            print("")
            for i in cur.data:
                for j in i:
                    print(j,end=" ")
                print("")
            if(self.h(cur.data,goal_node) == 0):
                break
            for i in cur.aStarChild(): #for each new child node thats generated
                i.fval = self.g(i,goal_node)
                openn.append(i)
            closed.append(cur)
            del openn[0]    

            openn.sort(key = lambda x:x.fval,reverse=False)

    """BFS start. We take the root node and pass into logic function for BFS"""
    def BFS(self):
        """
        count = 1
        for i in range(3):
            print(count + ") BFS")
            k = generatePuzzle()
            count = count + 1
        """
        #k = generatePuzzle()
        k = self.getFromUser() # GET THE ARRAY INPUT
        root = Node(0, k, None, None, 0, 0, 0) #PASS IN INITAL ROOT INFO
        
        # BFS implementation where we pass root
        goal, s, v = bfsSearch(root)
        """
        if goal is None and s is None and v is None:
            print("No solution")
        else:
            # Print and write the final output
        """
        print_states(path(goal))
        
    """Menu. Pick BFS or A* """

    """ GET INPUT FROM USER """
    def getFromUser(self):
        print("Please enter unique numbers between 0-8 followed by space")
        a = [int(x) for x in input().split()]
        n = 3
        final = [a[i * n:(i + 1) * n] for i in range((len(a) + n - 1) // n )]
        k = np.array(final)
        check_solvable(k)
        return k
        
        
              
    def menu(self):
        print("""
                    ************MAIN MENU**************                          
                          """)
        choice = input("""
                          A: Breadth First Search
                          B: A* Search
                          
                          Please enter your choice: """)
        if choice == "A" or choice == "a":
            self.BFS()
        if choice == "B" or choice == "b":
            self.aStar()
            
algo = Algo(3)
algo.menu()


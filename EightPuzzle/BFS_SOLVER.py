""" 8 Puzzle BFS algorithm
 Input the unsolved puzzle and the program
 solves it and creates 3 txt files with solutions"""

import numpy as np  # Used to store the digits in an array

import os  # Used to delete the file created by previous running of the program

goal_node = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])


class Node:
    def __init__(self, node_no, data, parent, act, cost,level,fval):
        self.data = data
        self.parent = parent
        self.act = act
        self.node_no = node_no
        self.cost = cost
        self.level = level
        self.fval = fval

def find_index(puzzle):
    print("MY BENEFIT")
    print(puzzle)
    result= np.where(puzzle == 0)
    #i = int(i)
    #j = int(j)
    return result[0][0], result[1][0]

'''
def move_left(data):
    i, j = find_index(data)
    if j == 0:
        return None
    else:
        temp_arr = np.copy(data)
        temp = temp_arr[i, j - 1]
        temp_arr[i, j] = temp
        temp_arr[i, j - 1] = 0
        print("move_left")
        return temp_arr
def move_right(data):
    i, j = find_index(data)
    if j == 2:
        return None
    else:
        temp_arr = np.copy(data)
        temp = temp_arr[i, j + 1]
        temp_arr[i, j] = temp
        temp_arr[i, j + 1] = 0
        print("move_right")
        return temp_arr
def move_up(data):
    i, j = find_index(data)
    if i == 0:
        return None
    else:
        temp_arr = np.copy(data)
        temp = temp_arr[i - 1, j]
        temp_arr[i, j] = temp
        temp_arr[i - 1, j] = 0
        print("move_up")
        return temp_arr
def move_down(data):
    i, j = find_index(data)
    if i == 2:
        return None
    else:
        temp_arr = np.copy(data)
        temp = temp_arr[i + 1, j]
        temp_arr[i, j] = temp
        temp_arr[i + 1, j] = 0
        print("move_down")
        print(type(temp_arr))
        print(temp_arr)
        print("DP DONE")
        return temp_arr
def move_tile(action, data):
    if action == 'up':
        return move_up(data)
    if action == 'down':
        return move_down(data)
    if action == 'left':
        return move_left(data)
    if action == 'right':
        return move_right(data)
    else:
        return None
'''

def print_states(list_final):  # To print the final states on the console
    print("printing final solution")
    for l in list_final:
        print("Move : " + str(l.act) + "\n" + "Result : " + "\n" + str(l.data) + "\t" + "node number:" + str(l.node_no))

def path(node):  # To find the path from the goal node to the starting node
    p = []  # Empty list
    p.append(node)
    parent_node = node.parent
    while parent_node is not None:
        p.append(parent_node)
        parent_node = parent_node.parent
    return list(reversed(p))
        
def shuffle(data,x1,y1,x2,y2):
        """ Move the blank space in the given direction and if the position value are out
            of limits the return None """
        if x2 >= 0 and x2 < len(data) and y2 >= 0 and y2 < len(data):
            temp_puz = []
            temp_puz = np.copy(data)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            #print("CHANGED")
            #print(temp_puz)
            #print("TYPE")
            #temp_puz = np.asarray(temp_puz)
            #print(type(temp_puz))
            return temp_puz
        else:
            return None
'''
def copy(root):
        """ Copy function to create a similar matrix of the given node"""
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp          
'''

def bfsNode(node):
    print("Exploring Nodes")
    actions = ["down", "up", "left", "right"]
    node_q = [node]
    final_nodes = []
    visited = []
    final_nodes.append(node_q[0].data.tolist())  # Only writing data of nodes in seen
    node_counter = 0  # To define a unique ID to all the nodes formed

    while node_q:
        current_root = node_q.pop(0)  # Pop the element 0 from the list
        if current_root.data.tolist() == goal_node.tolist():
            print("Goal reached")
            return current_root, final_nodes, visited
        #print("CURRENT NODE DATA")
        #print(current_root.data)
        #print("\n")

        x, y = find_index(current_root.data)
        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]   # 2 3 1 3

        #for move in actions:
        for i in val_list:
            #temp_data = move_tile(move, current_root.data)
            temp_data = shuffle(current_root.data,x,y,i[0],i[1])
            #print("TEMP_DATA")
            #print(temp_data)
            #print(type(temp_data))
            #print("\n")
            if temp_data is not None:
                node_counter += 1
                child_node = Node(node_counter, np.array(temp_data), current_root, i, 0, current_root.level + 1, 0)  # Create a child node
                #print("LEVEL")
                #print(current_root.level)
                #print("CHILD NODE CREATED")
                #print(child_node.data)
                if child_node.data.tolist() not in final_nodes:  # Add the child node data in final node list
                    node_q.append(child_node)
                    final_nodes.append(child_node.data.tolist())
                    visited.append(child_node)
                    if child_node.data.tolist() == goal_node.tolist():
                        print("Goal_reached")
                        return child_node, final_nodes, visited
    return None, None, None  # return statement if the goal node is not reached

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
    if counter_states % 2 == 0:
        print("The puzzle is solvable, generating path")
    else:
        print("The puzzle is insolvable, still creating nodes")


def BFS():  
    '''
    my_list = [1, 8, 2, 0, 4, 3, 7, 6, 5]
    #my_list = [0,4,7,5,1,8,6,2,3]
    n = 3
    final = [my_list[i * n:(i + 1) * n] for i in range((len(my_list) + n - 1) // n )]
    k = np.array(final)
    #k = [1, 2, 5, 3, 4, 0, 7, 8, 6]
    

    #check_correct_input(k)
    check_solvable(k)
    '''
    k = tempInput()
    root = Node(0, k, None, None, 0, 0, 0)

    # BFS implementation call
    goal, s, v = bfsNode(root)

    if goal is None and s is None and v is None:
        print("Goal State could not be reached, Sorry")
    else:
        # Print and write the final output
        print_states(path(goal))

def tempInput():
   # my_list = [1, 8, 2, 0, 4, 3, 7, 6, 5]
    my_list = [1, 2, 3, 4, 5, 6, 8, 0, 7]

    n = 3
    final = [my_list[i * n:(i + 1) * n] for i in range((len(my_list) + n - 1) // n )]
    k = np.array(final)
    #k = final
    check_solvable(k)
    return k

    
    
def f(start,goal):
    """ Heuristic Function to calculate hueristic value f(x) = h(x) + g(x) """
    return h(start.data,goal)+start.level

def h(start, goal):
    """ Calculates the different between the given puzzles """
    '''
    temp = 0
    startZero = np.argwhere(start == 0) # gives index of 0 in start 
    goalZero = np.argwhere(goal == 0) # gives index of 0 in goal

    if startZero == goalZero:
        temp = np.count_nonzero(start != goal)
        temp = temp - 1
        print("WITH ZERO")
    else:
        temp = np.count_nonzero(start != goal and start)
        print("WITHOUT ZERO")
    '''
    temp = np.count_nonzero(start != goal)
    
    return temp
'''
    for i in range(0,3):
        for j in range(0,3):
            if start[i][j] != goal[i][j] and start[i][j] != 0:
                temp += 1
                print("DISPLACED TILES")
                print(temp)
                return temp
'''

def generate(self):
    print(self.data)
    x, y = find_index(current_root.data)
    val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]   # 2 3 1 3
    children = []
    for i in val_list:
        child = shuffle(current_root.data,x,y,i[0],i[1])
        if child is not None:
            child_node = Node(0,child,0,0,0,current_root.level+1,0)
        return children

def aStar():
    open = []
    closed = []
    k = tempInput()
    root = Node(0,k, None, None, 0, 0, 0)
    root.fval = f(root,goal_node) # get final value heruistic
    print("F-VALUE")
    print(root.fval)
    open.append(root)    
    while True:
        current = open[0]
        for i in current.data:
            for j in i:
                print(j, end=" ")
                print("")
        # If the diff btwn current node and final node is 0, we're done
        if (h(current.data,goal_node) == 0):
            break
        for i in current.generate():
            i.fval = f(i,goal_node)
            open.append(i)
        closed.append(current)
        del open[0]

        open.sort(key = lambda x:x.fval,reverse=False)

def astarNode(node):
    pass


def main():
    menu()
    
def menu():

    print("""
                ************MAIN MENU**************
                      
                      """)
    choice = input("""
                      A: Breadth First Search
                      B: A* Search
                      
                      Please enter your choice: """)
    if choice == "A" or choice == "a":
        BFS()
    if choice == "B" or choice == "b":
        aStar()
main()

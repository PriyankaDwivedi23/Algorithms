"""
CSCI-665-01 Homework-4(pathInMaze.py)
Author: Priyanka Dwivedi(pd6741@rit.edu)
        Srikant Lakshminarayan (sxl8819@rit.edu)

The program takes input as maze and displays length of the shortest path.
Usage:python3 pathInMaze.py
row column
maze
"""


class Node:
    """
    The Node class stores the value its row index, column index and parent node
    """

    __slots__ = 'value','row_index','column_index','parent_node'

    def __init__(self, value , row , column , parent = None):
        self.value = value
        self.column_index = column
        self.row_index = row
        self.parent_node = parent


def isWay(row_index,column_index , rows , columns, maze):
    '''
    The function return true if there is a way or it has reached destination
    and false if there is wall
    :param row_index: row index to be checked
    :param column_index: column index to be checked
    :param rows: number of rows in maze
    :param columns:  number of column in maze
    :param maze: maze
    :return: true if there is way or reached destination and false if wall
    Complexity : O(1)
    '''
    if (row_index >= 0 and row_index < rows) and (column_index >= 0 and column_index < columns) :
        if (maze[row_index][column_index] == 0 or maze[row_index][column_index] == 3):
            return True

    return False


def getPath(maze,rows, columns):
    '''
    The function forms the path traversed in maze using Breadth First Traversal.
    :param maze: maze
    :param rows: rows in maze
    :param columns:column in maze
    :return: end vertex at which maze stopped
    Complexity : O(mn)
    '''
    #get start location i.e. 2
    start_location = getLocation(maze, 2)
    #initialise row and col to start location
    row, col = start_location
    #create root node
    root = Node(2,row,col, None)
    #queue will store nodes to be visited
    queue = []
    #start which root node
    queue.append(root)
    #initialise current certex
    current_vertex = 0
    #keep track of visited nodes
    visited = [[ 0 for col in range(columns) ]for row in range(rows)]
    #mark root node as visited
    visited[row][col] = 1
    #This loop will run until queue is empty
    while(len(queue) > 0):
        #pop current vertex from queue
        current_vertex = queue.pop(0)
        #Base Case if reached destination break the loop
        if current_vertex.value == 3:
            break

        if isWay(current_vertex.row_index, current_vertex.column_index + 1, rows, columns, maze) and \
                        visited[current_vertex.row_index][current_vertex.column_index + 1] == 0:

            visited[current_vertex.row_index][current_vertex.column_index + 1] = 1
            # new node
            node = Node(maze[current_vertex.row_index][current_vertex.column_index + 1], current_vertex.row_index,
                        current_vertex.column_index + 1, current_vertex)
            # append to queue
            queue.append(node)

        # check west of current vertex if it is not visited then append it to queue by creating node
        if isWay(current_vertex.row_index, current_vertex.column_index - 1, rows, columns, maze) and \
                        visited[current_vertex.row_index][current_vertex.column_index - 1] == 0:
            # mark it as visited
            visited[current_vertex.row_index][current_vertex.column_index - 1] = 1
            # new node
            node = Node(maze[current_vertex.row_index][current_vertex.column_index - 1], current_vertex.row_index,
                        current_vertex.column_index - 1, current_vertex)
            # append to queue
            queue.append(node)

        # check north of current vertex if it is not visited then append it to queue by creating node
        if isWay(current_vertex.row_index + 1, current_vertex.column_index, rows, columns, maze) and \
                        visited[current_vertex.row_index + 1][current_vertex.column_index] == 0:
            # mark it as visited
            visited[current_vertex.row_index + 1][current_vertex.column_index] = 1
            # new node
            node = Node(maze[current_vertex.row_index + 1][current_vertex.column_index], current_vertex.row_index + 1,
                        current_vertex.column_index, current_vertex)
            # append to queue
            queue.append(node)

        # check south of current vertex if it is not visited then append it to queue by creating node
        if isWay(current_vertex.row_index - 1, current_vertex.column_index, rows, columns, maze) and \
                        visited[current_vertex.row_index - 1][current_vertex.column_index] == 0:
            # mark it as visited
            visited[current_vertex.row_index - 1][current_vertex.column_index] = 1
            # new node
            node = Node(maze[current_vertex.row_index - 1][current_vertex.column_index], current_vertex.row_index - 1,
                        current_vertex.column_index, current_vertex)
            # append to queue
            queue.append(node)
    #last vertex will be retuned
    return current_vertex


def backtrack(vertex):
    '''
    The function will return the length of shortest path by backtracking
    from last vertex till parent is not None
    :param vertex: last vertex
    :return: length of shortest path
    Complexity  : O(m+n)
    '''
    current_parent = vertex.parent_node
    count = 0
    while current_parent != None:
        current_parent = current_parent.parent_node
        count +=1
    return count

def getLocation(maze,value):
    '''
    The function returns the
    :param maze: maze
    :param value: value to be found in maze
    :return: location at which value is located
    '''
    locate_start_row = [x for x in maze if value in x][0]
    start_location = [maze.index(locate_start_row), locate_start_row.index(value)]
    return start_location

def main():
    '''
    The main function will take input from user the maze and get path and backtrack
    to get length of shortest path.
    '''
    rows, columns = [int(x) for x in input().split(" ")]
    maze = []
    for row in range(rows):
        col = [int(x) for x in input().split(" ")]
        maze.append(col)
    #get last vertex
    last_vertex  = getPath(maze,rows, columns)
    #if last vertex is not 3 then we didnt reach destination return -1
    if last_vertex.value != 3:
        print(-1)
    #backtrack to get length of shortest path
    else:
        print(backtrack(last_vertex))

if __name__ == '__main__':
    main()
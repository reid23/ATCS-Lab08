import random

# Function that performs DFS starting at room (i, j) in an array with dimensions n by m
def DFS(i, j, n, m, array):
    # Mark (i, j) as visited with a 1
    array[i][j] = 1
    # Create a list of the room's neighbors, as long as they exist within the bounds of the array
    neighbors = []
    if i-2 >= 1:
        neighbors.append([i-2, j])
    if i+2 <= 2*n-1:
        neighbors.append([i+2, j])
    if j-2 >= 1:
        neighbors.append([i, j-2])
    if j+2 <= 2*m-1:
        neighbors.append([i, j+2])
    # Create an array that will hold the shuffled order of the rooms and the indices in the final ordering that are still empty
    finalOrder = []
    indices = []
    # At the start, all len(neighbors) indices in the final order are available and the finalOrder is empty
    for x in range(len(neighbors)):
        indices.append(x)
        finalOrder.append([])
    # For every neighbor, grab a random value from the list of available indices and put the neighbor in that slot in the finalOrder
    for x in range(len(neighbors)):
        randOrder = random.randint(0, len(indices)-1)
        finalOrder[indices[randOrder]] = neighbors[x]
        # Remove the now-occupied index from the indices list
        indices.pop(randOrder)
    # Iterate through all the neighbors in their new order
    for x in range(len(finalOrder)):
        # The neighbor is not visited (is marked with a 0)
        if array[finalOrder[x][0]][finalOrder[x][1]] == 0:
            # Mark the corridor (the cell between the original room and the neighbor) with a 2
            array[(finalOrder[x][0]+i)//2][(finalOrder[x][1]+j)//2] = 2
            # Call DFS on the neighbor
            DFS(finalOrder[x][0], finalOrder[x][1], n, m, array)
        # The neighbor is visited (marked with a 1) and the corridor is not visited (marked with a 0)
        elif array[finalOrder[x][0]][finalOrder[x][1]] == 1 and array[(finalOrder[x][0]+i)//2][(finalOrder[x][1]+j)//2] == 0:
            # Label the corridor as a wall (with a 3)
            array[(finalOrder[x][0]+i)//2][(finalOrder[x][1]+j)//2] = 3

# Function that generates an array containing maze of size N by M
def makeMazeArray(N, M):
    # reates a 2N+1 by 2M+1 array to store the rooms and corridors/walls
    mazeArray = []
    for a in range(2*N+1):
        mazeArray.append([])
    # Initializes all values as unmarked with a 0
    for a in range(2*N+1):
        for b in range(2*M+1):
            mazeArray[a].append(0)
    # Boundary cells are all walls (marked with a 3)
    for a in range(2*N+1):
        mazeArray[a][0] = 3
        mazeArray[a][2*M] = 3
    for b in range(2*M+1):
        mazeArray[0][b] = 3
        mazeArray[2*N][b] = 3
    # All cells with 2 even indices are neither cells or corridors, so just mark them as walls
    for a in range(N+1):
        for b in range(M+1):
            mazeArray[2*a][2*b] = 3
    # Call DFS on the top left room
    DFS(1, 1, N, M, mazeArray)
    # Return the finished maze
    return(mazeArray)

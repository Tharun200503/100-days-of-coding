# Function to check if the current position is valid (not out of bounds)
def is_valid_move(x, y, maze):
    if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]):
        return False
    if maze[x][y] == 1:  # 1 indicates a wall
        return False
    return True

# Function to escape the maze using a simple strategy
def escape_maze(maze, start_x, start_y):
    x, y = start_x, start_y
    steps = 0
    # Directions: Right, Down, Left, Up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while True:
        # Check if we've reached the exit (bottom-right corner)
        if x == len(maze) - 1 and y == len(maze[0]) - 1:
            print(f"Escaped the maze in {steps} steps!")
            break
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(new_x, new_y, maze):
                x, y = new_x, new_y
                steps += 1
                print(f"Moved to ({x}, {y})")
                break

# Maze representation (0 = open path, 1 = wall)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
]

# Starting position (top-left corner)
start_x, start_y = 0, 0

# Call the function to escape the maze
escape_maze(maze, start_x, start_y)

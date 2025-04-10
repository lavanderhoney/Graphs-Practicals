from collections import deque

def bfs_maze_solver(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    queue = deque([start])
    visited = set([start])
    parent = {start: None}
    
    while queue:
        current = queue.popleft()
        
        if current == end:
            # Reconstruct the path from end to start using the parent dictionary
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]  # Return reversed path
        
        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy
            
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))
                parent[(nx, ny)] = current
    
    return None  # No path found


maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)
end = (4, 4)

path = bfs_maze_solver(maze, start, end)
if path:
    print("Path found:", path)
else:
    print("No path found.")

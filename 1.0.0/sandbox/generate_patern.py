import random
import tkinter as tk

# Constants
CANVAS_WIDTH = 350  # Fixed canvas width
CANVAS_HEIGHT = 800  # Fixed canvas height
GRID_WIDTH = 7  # Number of rooms in the width (horizontal)
GRID_HEIGHT = 12  # Number of rooms in the height (vertical)
ROOM_WIDTH = 90  # Width of each room
ROOM_HEIGHT = 90  # Height of each room
FUSION_CHANCE = 85  # Probability of fusing adjacent rooms

# Define a list of colors to choose from for room clusters
COLORS = ["lightblue", "lightgreen", "lightcoral", "lightyellow"]

class Room:
    """Class to represent a room with position, geometry, and color."""
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color  # Store color as a property of the room

def draw_room(room, canvas):
    """Draw a room on the canvas with only its border, no color."""
    # Remove 'fill' parameter to only display the outline (border)
    canvas.create_rectangle(room.x, room.y, room.x + room.width, room.y + room.height,
                            outline="black")  # Only black outline for clarity

def get_adjacent_rooms(room, rooms):
    """Find all rooms that are adjacent to the given room."""
    adjacent_rooms = []
    for other in rooms:
        if (abs(room.x - other.x) == ROOM_WIDTH and room.y == other.y) or (abs(room.y - other.y) == ROOM_HEIGHT and room.x == other.x):
            adjacent_rooms.append(other)
    return adjacent_rooms

def is_connected(rooms):
    """Check if all rooms are connected using a DFS (Depth-First Search) approach."""
    if not rooms:
        return True

    # Start DFS from the first room
    visited = set()
    stack = [rooms[0]]

    while stack:
        current_room = stack.pop()
        if current_room not in visited:
            visited.add(current_room)
            # Add all adjacent, non-visited rooms to the stack
            for adjacent in get_adjacent_rooms(current_room, rooms):
                if adjacent not in visited:
                    stack.append(adjacent)

    # If all rooms were visited, the dungeon is connected
    return len(visited) == len(rooms)

def fuse_rooms(rooms):
    """Fuse adjacent rooms of the same color to create larger rooms and assign colors to clusters."""
    fused_rooms = []
    visited = set()  # Keep track of visited rooms

    # Create a dictionary to group rooms by color
    color_groups = {}
    for room in rooms:
        if room.color not in color_groups:
            color_groups[room.color] = []
        color_groups[room.color].append(room)

    # Fuse rooms by color and neighbors
    for color, group in color_groups.items():
        for room in group:
            if room in visited:
                continue  # Skip already visited rooms
            
            # Start a new cluster with the current room
            to_fuse = []
            queue = [room]  # Start with the current room
            while queue:
                current = queue.pop(0)
                if current in visited:
                    continue
                visited.add(current)  # Mark the current room as visited
                to_fuse.append(current)

                # Check for adjacent rooms of the same color
                for other in group:
                    if other in visited:
                        continue
                    # Check if 'other' is adjacent to 'current' and has the same color
                    if other in get_adjacent_rooms(current, rooms):
                        if random.random() < FUSION_CHANCE:  # Check fusion chance
                            queue.append(other)

            # Create a new room only if we have rooms to fuse
            if to_fuse:
                # Calculate the bounds for the new fused room
                min_x = min(r.x for r in to_fuse)
                min_y = min(r.y for r in to_fuse)
                max_x = max(r.x + r.width for r in to_fuse)
                max_y = max(r.y + r.height for r in to_fuse)

                # Create the new room and add it to fused_rooms
                new_room = Room(min_x, min_y, max_x - min_x, max_y - min_y, color)
                fused_rooms.append(new_room)

    return fused_rooms

def generate_dungeon(canvas):
    """Generate a dungeon layout with a rectangular grid of rooms and fuse them."""
    rooms = []

    # Create rooms in a grid
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            x = col * ROOM_WIDTH
            y = row * ROOM_HEIGHT
            color = random.choice(COLORS)  # Randomly assign a color to each room
            room = Room(x, y, ROOM_WIDTH, ROOM_HEIGHT, color)
            rooms.append(room)

    # Fuse neighboring rooms by color
    fused_rooms = fuse_rooms(rooms)

    # Draw the rooms with their colors
    for room in fused_rooms:
        draw_room(room, canvas)  # Draw the room

    # Draw a border around the entire canvas
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, outline="black", width=2)

def main():
    """Main function to create the Tkinter window and run the dungeon generator."""
    root = tk.Tk()
    root.title("Clustered Room Dungeon Generator")

    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas.pack()

    generate_dungeon(canvas)

    root.mainloop()

if __name__ == "__main__":
    main()

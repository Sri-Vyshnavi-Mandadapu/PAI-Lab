import heapq

GOAL_STATE = ((1, 2, 3),
              (4, 5, 6),
              (7, 8, 0))


class PuzzleNode:
    def __init__(self, state, parent=None, move="", g=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.g = g
        self.h = self.manhattan_distance()
        self.f = self.g + self.h

    def manhattan_distance(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                value = self.state[i][j]
                if value != 0:
                    goal_x = (value - 1) // 3
                    goal_y = (value - 1) % 3
                    distance += abs(goal_x - i) + abs(goal_y - j)
        return distance

    def __lt__(self, other):
        return self.f < other.f


def print_board(state):
    print("-------------")
    for row in state:
        print("|", end=" ")
        for val in row:
            if val == 0:
                print(" ", end=" | ")
            else:
                print(val, end=" | ")
        print("\n-------------")
    print()


def get_neighbors(state):
    neighbors = []
    directions = [("Up", (-1, 0)),
                  ("Down", (1, 0)),
                  ("Left", (0, -1)),
                  ("Right", (0, 1))]

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j

    for move, (dx, dy) in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append((move, tuple(tuple(row) for row in new_state)))

    return neighbors


def a_star(start_state):
    open_list = []
    closed_set = set()

    start_node = PuzzleNode(start_state)
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.state == GOAL_STATE:
            return current_node

        closed_set.add(current_node.state)

        for move, neighbor in get_neighbors(current_node.state):
            if neighbor in closed_set:
                continue

            neighbor_node = PuzzleNode(neighbor, current_node, move, current_node.g + 1)
            heapq.heappush(open_list, neighbor_node)

    return None


def reconstruct_path(goal_node):
    path = []
    current = goal_node
    while current:
        path.append((current.move, current.state))
        current = current.parent
    return path[::-1]


# ----------- MAIN PROGRAM -------------

if __name__ == "__main__":
    start = ((1, 2, 3),
             (4, 0, 6),
             (7, 5, 8))

    print("\nInitial State:")
    print_board(start)

    goal_node = a_star(start)

    if goal_node:
        solution_path = reconstruct_path(goal_node)

        print("Solution Steps:\n")

        for step, (move, state) in enumerate(solution_path):
            if step == 0:
                print("Step 0 (Initial State)")
            else:
                print(f"Step {step} (Move: {move})")
            print_board(state)

        print("Goal Reached!")
        print("Total Moves:", len(solution_path) - 1)

    else:
        print("No solution found.")

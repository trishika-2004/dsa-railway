from collections import deque, defaultdict
import heapq

# ----------------------------
# 1. Graph: Railway Network
# ----------------------------
class RailwayGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_track(self, station1, station2, distance):
        self.graph[station1].append((station2, distance))
        self.graph[station2].append((station1, distance))

    def shortest_path(self, start, end):
        distances = {station: float('inf') for station in self.graph}
        distances[start] = 0
        pq = [(0, start)]
        while pq:
            current_distance, current_station = heapq.heappop(pq)
            if current_station == end:
                return current_distance
            for neighbor, weight in self.graph[current_station]:
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(pq, (new_distance, neighbor))
        return float('inf')


# ----------------------------
# 2. Linked List: Train Route
# ----------------------------
class TrackSegment:
    def __init__(self, name):
        self.name = name
        self.next = None

class TrainRoute:
    def __init__(self):
        self.head = None

    def add_segment(self, name):
        new_segment = TrackSegment(name)
        if not self.head:
            self.head = new_segment
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_segment

    def print_route(self):
        current = self.head
        while current:
            print(current.name, end=" -> ")
            current = current.next
        print("END")


# ----------------------------
# 3. Array: Track Layout
# ----------------------------
class TrackLayout:
    def __init__(self, layout):
        self.layout = layout  # e.g., ['straight', 'curve', 'bridge']

    def search(self, section_type):
        for i, section in enumerate(self.layout):
            if section == section_type:
                return i
        return -1


# ----------------------------
# 4. Tree: Track Hierarchy
# ----------------------------
class TrackNode:
    def __init__(self, segment):
        self.segment = segment
        self.children = []

    def add_branch(self, child_node):
        self.children.append(child_node)

    def print_tree(self, level=0):
        print(" " * level * 2 + f"- {self.segment}")
        for child in self.children:
            child.print_tree(level + 1)


# ----------------------------
# 5. Stack and Queue: Train Scheduling
# ----------------------------
class TrainScheduler:
    def __init__(self):
        self.stack = []  # LIFO
        self.queue = deque()  # FIFO

    def arrive_train(self, train_id):
        self.stack.append(train_id)
        self.queue.append(train_id)

    def depart_stack(self):
        if self.stack:
            return self.stack.pop()
        return None

    def depart_queue(self):
        if self.queue:
            return self.queue.popleft()
        return None


# ----------------------------
# Demonstration
# ----------------------------
if __name__ == "__main__":
    print("=== Railway Graph ===")
    rg = RailwayGraph()
    rg.add_track("A", "B", 5)
    rg.add_track("B", "C", 4)
    rg.add_track("A", "C", 10)
    print(f"Shortest path A to C: {rg.shortest_path('A', 'C')}")

    print("\n=== Train Route (Linked List) ===")
    route = TrainRoute()
    for segment in ["Segment1", "Segment2", "Segment3"]:
        route.add_segment(segment)
    route.print_route()

    print("\n=== Track Layout (Array) ===")
    layout = TrackLayout(['straight', 'curve', 'bridge'])
    idx = layout.search('curve')
    print(f"'curve' found at index: {idx}")

    print("\n=== Track Hierarchy (Tree) ===")
    root = TrackNode("MainTrack")
    branch1 = TrackNode("Branch1")
    branch2 = TrackNode("Branch2")
    subbranch1 = TrackNode("SubBranch1")
    branch1.add_branch(subbranch1)
    root.add_branch(branch1)
    root.add_branch(branch2)
    root.print_tree()

    print("\n=== Train Scheduler (Stack and Queue) ===")
    scheduler = TrainScheduler()
    for train_id in ["TrainA", "TrainB", "TrainC"]:
        scheduler.arrive_train(train_id)

    print("LIFO Departure (Stack):", scheduler.depart_stack())
    print("FIFO Departure (Queue):", scheduler.depart_queue())

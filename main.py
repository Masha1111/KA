class Node:
    def __init__(self, name):
        self.name = name
        self.color = -1
        self.neighbors = set()
        self.change = False

    def tie(self, node):
        self.neighbors.add(node)
        node.neighbors.add(self)


class Part:
    def __init__(self):
        self.elements = []

    def add(self, node):
        self.elements.append(node)


class Graph:
    def __init__(self):
        self.nodes = []

    def append(self, node):
        self.nodes.append(node)


def make_graph(graph):
    visited = []
    graph.nodes[0].color = 0
    graph.nodes[0].change = True
    color = 1
    stack = [graph.nodes[0]]
    while len(stack) != 0:
        current = stack.pop()
        if current in visited:
            continue
        visited.append(current)
        for neighbor in current.neighbors:
            if neighbor.color == - 1 and neighbor.change == False:
                neighbor.color = color
                neighbor.change = True
            stack.append(neighbor)
        if color == 1:
            color -= 1
        else:
            color += 1


def check_part(part):
    for el in part.elements:
        for e in part.elements:
            if e in el.neighbors:
                return False
    return True


def get_parts(graph):
    part1 = Part()
    part2 = Part()
    for el in graph.nodes:
        if el.color == 0:
            part1.add(el)
        else:
            part2.add(el)
    return ((part1, part2))


def sort_by_name(node):
    return node.name


with open("in.txt", 'r') as file:
    graph = Graph()
    first_string = file.readline().strip()
    count = int(first_string)
    data = file.readlines()
    for i in range(1, count + 1):
        node = Node(i)
        graph.append(node)
    for i in range(count):
        current_node = graph.nodes[i]
        arr = data[i].split(" ")[:-1]
        for j in range(len(arr)):
            if int(arr[j]) != 0:
                current_node.tie(graph.nodes[int(arr[j]) - 1])
    make_graph(graph)
    for element in graph.nodes:
        if element.color == -1 and element.change == True:
            element.color = 0
            element.change = True
    parts = get_parts(graph)
    if not check_part(parts[0]) or not check_part(parts[1]):
        with open("out.txt", 'w') as file:
            file.write("N")
    else:
        for i in range(2):
            parts[i].elements.sort(key=sort_by_name)
            with open("out.txt", 'a') as file:
                for node in parts[i].elements:
                    file.write(str(node.name) + " ")
                file.write(str(0) + '\n')

class Graph:
    class Node:
        def __init__(self, data: str = "", edges: dict = None, fathers: dict = None) -> None:
            self.data = data
            self.edges = edges
            self.fathers = fathers
    
        def __str__(self) -> str:
            string = ""
            string += "data: " + str(self.data) + "\n"
            string += "edges: "
            if self.edges is not None:
                for edge in self.edges:
                    string += "(" + str(self.edges[edge]) + "->" + str(edge.data) + ") "
                string += "\n"
            else: string += "None\n"
            string += "fathers: "
            if self.fathers is not None:
                for father in self.fathers:
                    string += "(" + str(self.fathers[father][0]) + " " + str(father.data) + " -> " +  str(self.fathers[father][1]) + " " + str(self.data) + ") "
                string += "\n"
            else: string += "None"
            string += "\n"
            return string
    
        def add_edge(self, node, weight: int = 1, num_prod: int = 1) -> None:
            if self.edges is None:
                self.edges = {}
            if node not in self.edges:
                if node.fathers is None:
                    node.fathers = {}
                node.fathers[self] = (weight, num_prod)
                self.edges[node] = weight
    
    def __init__(self, vertices: list = None) -> None:
        self.vertices = vertices
        self.values = {}
        self.end_result = 0
        self.loops = 0
    
    def __str__(self) -> str:
        string = ""
        if self.vertices is None:
            return "None"
        for vertex in self.vertices:
            string += str(vertex) + "\n"
        return string
    
    def add_vertex(self, node) -> Node:
        if self.vertices is None:
            self.vertices = []
        if node not in self.vertices:
            self.vertices.append(node)
            return node
        return None
    
    def add_and_construct_vertex(self, data: str = "", edges: dict = None, fathers: list = None) -> Node:
        if self.vertices is None:
            self.vertices = []
        for vertex in self.vertices:
            if vertex.data == data:
                return vertex
        new_node = self.Node(data, edges, fathers)
        self.vertices.append(new_node)
        return new_node
    
    def add_edge_node1_to_node2(self, node1, node2, weight: int = 1, num_prod: int = 1) -> None:
        self.vertices[self.vertices.index(node1)].add_edge(node2, weight, num_prod)
    
    def find_node(self, data: str = "") -> Node:
        for vertex in self.vertices:
            if vertex.data == data:
                return vertex
        return None
        
    def hydrogen_to_gold(self, node=None) -> int:
        self.loops += 1
        if node is None: # default node is hidrogenio
            node = self.find_node("hidrogenio")
            if node is None: # if there is no hidrogenio node, return invalid value
                return -1
        if node.edges is None: # if node has no edges, then it is the ouro node
            return 1
        
        if node not in self.values: # check if node is in values
            self.values[node] = 0
        if self.values[node] != 0: # if node has already been calculated, return its value
            return self.values[node]
        
        # node not in values, so it hasn't been calculated yet, so let's calculate it
        hidro = 0
        for edge in node.edges: # for each edge, add the number of products to the total
            hidro += node.edges[edge] * self.hydrogen_to_gold(edge) # multiply by weight (number of catalysts) eg. if 2 hidrogenio makes 1 iron, and 5 iron makes 1 ouro, then 10 hidrogenio (2 * 5) makes 1 ouro
        if hidro == 0:
            self.values[node] = 1 # if hidro is 0, then it means that the node is ouro, so it has 1 product
            return 1
        self.values[node] = hidro # set the value of the node to hidro
        return hidro
    
    def assess(self):
        if self.find_node("ouro") is None:
            return "[!] Critical error: no node with data \"ouro\" found, check your input file"
        result = self.hydrogen_to_gold()
        if result == self.end_result:
            return "[o] " + str(result) + " | loops: " + str(self.loops) # checkmark symbol
        elif result == -1:
            return "[!] Critical error: hydrogen_to_gold returned -1 (it found no node with data \"hidrogenio\"), check your input file"
        else:
            return "[x] " + str(result) + " [Expected result: " + str(self.end_result) + "]"
        
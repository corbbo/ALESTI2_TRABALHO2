import graph as g

def read_data(filename) -> g.Graph:
    graph = g.Graph()
    file = open(filename, "r")
    for line in file:
        line = line.strip("\n").split(" ")
        if line[0] == "#": # final line
            graph.end_result = int(line[1])
            if graph.end_result == 0: # error checking
                print("Error: end_result == 0\n\tLine: " + str(line))
                file.close()
                return None
        catalysts = []
        weights = []
        product = ""
        result = 0
        CatProd = 0
        
        # Read split line
        for string in line:
            if CatProd == 0: # catalysts
                if string == "->":
                    CatProd = 1 # -> indicates next strings are products
                    continue
                if string.isnumeric(): # weight
                    weights.append(int(string))
                    continue
                catalysts.append(string)
            else: # products
                if string.isnumeric():
                    result = int(string)
                    continue
                product = string
                
        # Error checking
        if len(catalysts) != len(weights):
            print("Error: len(catalysts) != len(weights)\n\tcatalysts: " + str(catalysts) + "\n\tweights: " + str(weights) + "\n\tLine: " + str(line))
            file.close()
            return None
        if result == 0 and graph.end_result == 0:
            print("Error: result == 0\n\tLine: " + str(line))
            file.close()
            return None
        if len(catalysts) == 0 or len(weights) == 0:
            print("Error: len(catalysts) == 0 or len(weights) == 0\n\tcataysts: " + str(catalysts) + "\n\tweights: " + str(weights) + "\n\tLine: " + str(line))
            file.close()
            return None
        
        # Add nodes and edges to graph
        product_node = graph.add_and_construct_vertex(product)
        # While there are catalysts left   
        while len(catalysts) > 0:
            catalyst = catalysts.pop(0) # get catalyst
            weight = weights.pop(0) # get corresponding weight
            catalyst_node = graph.add_and_construct_vertex(catalyst) # try to add catalyst to graph
            graph.add_edge_node1_to_node2(catalyst_node, product_node, weight, result) # add edge from catalyst to product
            

    file.close()

    return graph
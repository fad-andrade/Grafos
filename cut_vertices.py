import matplotlib.pyplot as plt
import networkx as nx

time = 0
def findCutVertices(G, root, T):
    # Define time variable as global
    global time

    # For each node, initialize visited, time and low state
    G._node[root]["visited"] = True
    G._node[root]["time"] = time
    G._node[root]["low"] = time

    # Increment global time var
    time += 1
    
    # Add current node to our digraph tree
    T.add_node(root)

    # For each current node neighbor
    for item in list(G.neighbors(root)):

        # Recursive call only for non-visited neighbors
        if(G._node[item]["visited"] == False):
            findCutVertices(G, item, T)
            
            # Add a 'child' edge between current node and it neighbor
            T.add_edge(root, item)

            # Update current node low value
            G._node[root]["low"] = min(G._node[root]["low"], G._node[item]["low"])

            # Cut-node conditition for a root node
            if(G._node[root]["tree_root"] and len(list(T.successors(root))) > 1):
                G._node[root]["cut"] = True
            
            #Cut-node condidition for any other kind of nodes
            elif(not(G._node[root]["tree_root"]) and G._node[item]["low"] >= G._node[root]["time"]):
                G._node[root]["cut"] = True

        # Update current node low value           
        else:
            G._node[root]["low"] = min(G._node[root]["low"], G._node[item]["time"])

def main():
    # Initialize the G graph
    G = nx.Graph()

    # Set number of nodes
    num_nodes = 19

    # Adding all nodes with initial attributes
    node_list = []
    for i in range(num_nodes):
        new_tuple = (i, {"tree_root": False, "visited": False, "cut": False, "time": 0, "low": 0})
        node_list.append(new_tuple)
    G.add_nodes_from(node_list)
    
    # Adding edges to G
    G.add_edge(0, 1)
    G.add_edge(1, 2)
    G.add_edge(2, 3)
    G.add_edge(5, 6)
    G.add_edge(7, 8)
    G.add_edge(8, 9)
    G.add_edge(8, 10)
    G.add_edge(10, 11)
    G.add_edge(10, 12)
    G.add_edge(13, 14)
    G.add_edge(14, 15)
    G.add_edge(14, 16)
    G.add_edge(16, 17)
    G.add_edge(16, 18)
    G.add_edge(17, 18)

    # Create a T digraph tree
    T = nx.DiGraph()

    # Call DFS function for each node not yet visited, preventing forgot disconnected components
    for node in list(G.nodes()):
        if(G._node[node]["visited"] == False):
            G._node[node]["tree_root"] = True
            findCutVertices(G, node, T)

    # Coloring cut-nodes
    color_map = []
    for node in list(G.nodes()):
        # Cut-nodes are red
        if(G._node[node]["cut"] == True):
            color_map.append('red')
        # All the others nodes are black
        else:
            color_map.append('black')
    
    # Drawing spawned DFS tree
    plt.figure("Spawned DFS Tree")
    pos = nx.nx_agraph.graphviz_layout(T, prog="dot")
    nx.draw(T, pos, with_labels = True, node_color = color_map, font_color = 'white', font_weight = 'bold')
    
    # Drawing original graph
    plt.figure("Original Graph With Bold Cut-Nodes")
    nx.draw(G, with_labels = True, node_color = color_map, font_color = 'white', font_weight = 'bold')
    plt.show()

main()
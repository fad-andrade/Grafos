import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations
from networkx.algorithms.tree.recognition import is_forest

def findBestEdge(G, F):
    edges = []

    # For each edge in original graph
    for edge in G.edges(data=True):
        u = edge[0]
        v = edge[1]

        # Take that ones that isnt in F yet and, if choosed, keeps the forest properties
        if(not(F.has_edge(u, v))):
            new = F.copy()
            new.add_edge(u, v)
            if(is_forest(new)):
                edges.append(edge)

    #Sort the edge list and take the first one
    if(len(edges) > 0):
        edges = sorted(edges, key=lambda i: i[2].get('weight'))
        return edges[0]
    return None
     
def Kruskal(G):
    # Initialize an empty forest
    F = nx.Graph()

    while(True):
        #Finds an edge that have the lowest weight and keep F an forest
        edge = findBestEdge(G, F)
        
        # If there is such edge
        if(edge != None):
            u = edge[0]
            v = edge[1]
            w = edge[2].get('weight')

            # Add that edge to the forest
            F.add_edge(u, v, weight=w)
        
        #If there is no edge left
        else:
            break
    
    #Return the final forest, now a minimum tree
    return F.size(weight='weight')

def allEdgesComb(G):
    n = G.number_of_nodes()

    #Return all edges combinations of (n-1) elements
    return list(combinations(list(G.edges(data=True)), n - 1))

def findAllMSTs(comb, min_weight):
    MSTs = []

    #For each edge combination
    for each in comb:
        T = nx.Graph()
        T.add_edges_from(list(each))

        #Verify if its a tree and have the mininum total weight
        if(nx.is_tree(T) and T.size(weight='weight') == min_weight):
            MSTs.append(T)
    
    return MSTs

def main():
    # Initialize the G graph
    G = nx.Graph()

    # Set number of nodes
    num_nodes = 10

    # Adding all nodes
    G.add_nodes_from(list(range(num_nodes)))

    # Adding edges to G
    G.add_edge(0, 1, weight=4, color='grey')
    G.add_edge(0, 3, weight=3, color='grey')
    G.add_edge(0, 6, weight=6, color='grey')
    G.add_edge(1, 2, weight=5, color='grey')
    G.add_edge(1, 3, weight=5, color='grey')
    G.add_edge(1, 4, weight=2, color='grey')
    G.add_edge(1, 5, weight=3, color='grey')
    G.add_edge(2, 4, weight=2, color='grey')
    G.add_edge(2, 9, weight=4, color='grey')
    G.add_edge(3, 6, weight=4, color='grey')
    G.add_edge(3, 7, weight=2, color='grey')
    G.add_edge(4, 5, weight=2, color='grey')
    G.add_edge(4, 9, weight=5, color='grey')
    G.add_edge(5, 7, weight=6, color='grey')
    G.add_edge(5, 8, weight=4, color='grey')
    G.add_edge(6, 7, weight=3, color='grey')
    G.add_edge(7, 8, weight=5, color='grey')
    G.add_edge(8, 9, weight=3, color='grey')

    # Discover minimum weight
    min_weight = Kruskal(G)

    # Discover all edges combinations
    comb = allEdgesComb(G)

    # Discover if it is an MST
    MSTs = findAllMSTs(comb, min_weight)

    #Printing MSTs
    cont = 0
    for each in MSTs:
        tree = each.edges(data=True)
        new = G.copy()
        
        for edge in tree:
            u = edge[0]
            v = edge[1]
            w = edge[2].get('weight')
            new.add_edge(u, v, weight=w, color='red')

        cont += 1
        plt.figure("MST #" + str(cont) + " - Weight " + str(min_weight))
        edge_labels = nx.get_edge_attributes(new, 'weight')
        colors = nx.get_edge_attributes(new, 'color').values()
        nx.draw_planar(new, with_labels = True, node_color = 'black', edge_color=colors, font_color = 'white', font_weight = 'bold', width=3)
        nx.draw_networkx_edge_labels(new, nx.planar_layout(new), edge_labels = edge_labels)
    plt.show()

main()
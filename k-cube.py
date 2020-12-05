import itertools
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def main():
    G = nx.Graph()
    dimension = 3

    prod = itertools.product([0, 1], repeat=dimension)

    for p in prod:
        G.add_node(''.join(map(str,list(p))))
    
    for label1 in G.nodes():
        for label2 in G.nodes():
            if(label1 != label2):
                    cont = 0
                    for i in range(len(label1)):
                        if(label1[i] != label2[i]):
                            cont += 1
                    if(cont == 1):
                        print(label1, label2)
                        G.add_edge(label1, label2)

    nx.draw(G, with_labels=True, node_color="black", font_color = 'white', font_weight = 'bold', node_size = 600)
    plt.show()
main()
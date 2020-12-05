import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def main():
    n = 4 

    G = nx.complete_graph(n)
    L = nx.line_graph(G)

    plt.figure(1)
    nx.draw(G, with_labels=True, node_color="black", font_color = 'white', font_weight = 'bold', node_size = 600)
    plt.figure(2)
    nx.draw(L, with_labels=True, node_color="black", font_color = 'white', font_weight = 'bold', node_size = 600)
    plt.show()
main()
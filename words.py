import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def main():
    G = nx.Graph()

    G.add_node("caiado")
    G.add_node("ramo")
    G.add_node("vaiado")
    G.add_node("cavado")
    G.add_node("rata")
    G.add_node("varado")
    G.add_node("cavalo")
    G.add_node("rato")
    G.add_node("virada")
    G.add_node("girafa")
    G.add_node("remo")
    G.add_node("virado")
    G.add_node("girava")
    G.add_node("reta")
    G.add_node("virava")
    G.add_node("ralo")
    G.add_node("rota")

    for label1 in G.nodes():
        for label2 in G.nodes():
            if(label1 != label2):
                if(len(label1) == len(label2)):
                    cont = 0
                    for i in range(len(label1)):
                        if(label1[i] != label2[i]):
                            cont += 1
                    if(cont == 1):
                        print(label1, label2)
                        G.add_edge(label1, label2)

    nx.draw(G, with_labels=True, node_color="black", font_color = 'white', node_size = 1500)
    plt.show()
main()
from threading import Thread
import networkx as nx

class Labeler(Thread):

    def __init__(self, G):
        Thread.__init__(self)

        self.G = G
        self.returned_value = None
    
    def run(self):
        new_labels = []

        # Visiting all the vertices
        for v in self.G.nodes():

            neighborhood_degree = []
            # Visiting all the neighborhood
            for n in self.G.neighbors(v):
                neighborhood_degree.append(self.G.degree(n))

            #Sorting the neighborhood degree list
            neighborhood_degree.sort()
            
            # New label for the v vertice
            str_current_label = str(self.G._node[v]['label'])
            str_neighborhood_degree = ''.join(str(x) for x in neighborhood_degree)

            str_new_label = str_current_label + ',' + str_neighborhood_degree
            
            #Applying hash function to the new label
            new_labels.append(hash(str_new_label))
        
        # Assigning new labels to the graph
        for v, label in zip(self.G.nodes(), new_labels):
            self.G._node[v]['label'] = label

        # Returning the 'canonical form'
        new_labels.sort()
        self.returned_value = new_labels

def main():
    # Creating graphs
    G = nx.petersen_graph()

    H = nx.Graph()
    H.add_node('A')
    H.add_node('B')
    H.add_node('C')
    H.add_node('D')
    H.add_node('E')
    H.add_node('F')
    H.add_node('G')
    H.add_node('H')
    H.add_node('I')
    H.add_node('J')
    H.add_edge('A','B')
    H.add_edge('A','F')
    H.add_edge('A','E')
    H.add_edge('B','C')
    H.add_edge('B','G')
    H.add_edge('C','D')
    H.add_edge('C','H')
    H.add_edge('D','E')
    H.add_edge('D','I')
    H.add_edge('E','J')
    H.add_edge('F','G')
    H.add_edge('F','J')
    H.add_edge('G','H')
    H.add_edge('H','I')
    H.add_edge('I','J')

    # Max number of iterations
    k = 30

    # Verifying the number of nodes and edges
    if((G.number_of_nodes() != H.number_of_nodes()) or
       (G.number_of_edges() != H.number_of_edges())):
       print("False")
       return

    # Initializing labels with nodes degrees
    for g, h in zip(G.nodes(), H.nodes()):
        G._node[g]['label'] = G.degree(g)
        H._node[h]['label'] = H.degree(h)

    for _ in range(k):
        # Creating threads
        thread1 = Labeler(G)
        thread2 = Labeler(H)

        # Starting threads
        thread1.start()
        thread2.start()

        # Joining threads
        thread1.join()
        thread2.join()

        if(thread1.returned_value == thread2.returned_value):
            print("True")
            return

    print("False")
main()
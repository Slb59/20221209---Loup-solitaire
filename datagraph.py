import networkx as nx
import matplotlib.pyplot as plt


class DataGraph:
    def __init__(self):
        self.visual = []

    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()

    def dataToGraph(self, data):
        for i in range(1,len(data.rowList)):
            self.addEdge(data.rowList[i][0], data.rowList[i][3])
            dest = data.rowList[i][5]
            self.addEdge(data.rowList[i][0], dest)
            dest = data.rowList[i][7]
            self.addEdge(data.rowList[i][0], dest)
            dest = data.rowList[i][9]
            self.addEdge(data.rowList[i][0], dest)




from dataload import DataLoad
from datagraph import DataGraph

data = DataLoad()

graph = DataGraph()
graph.dataToGraph(data)
graph.visualize()


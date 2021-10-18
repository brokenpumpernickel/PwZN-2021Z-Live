from ascii_graph import Pyasciigraph
from random import randint

graph = Pyasciigraph()

data = [(f'Label {i}', randint(0, 10)) for i in range(10)]

# def sorter(e):
#     return e[1]

# data.sort(key = sorter, reverse = True)

x = lambda e: e[1]
print(x((1, 2)))

data.sort(key = lambda e: e[1], reverse = True)

for line in graph.graph('Moj zajsuper histogram', data):
    print(line)
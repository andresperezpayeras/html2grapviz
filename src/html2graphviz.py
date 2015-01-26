import networkx as nx
from lxml import html
import matplotlib.pyplot as plt
import sys

raw = ""

#for line in sys.stdin:
#    raw = raw + line

#raw = stdin.read();


raw = '<!doctype html><html><head><meta charset="utf-8"><title>Ejercicio opcional arbol</title></head><body><header>    <img src="logotipo.jpg" alt="Firefox Logo" width="100"height="100"></header><nav>     <ul> <li>Menu 1</li> <li>Menu 2</li> <li>Menu 3</li>     </ul></nav><article>     <h1>Titular de nivel 1</h1>     <p>Contenido de la pagina</p></article><footer>Pie de pagina</footer></body></html>'

def traverse(parent, graph, labels):
    labels[parent] = parent.tag
    for node in parent.getchildren():
        graph.add_edge(parent, node)
        traverse(node, graph, labels)

G = nx.DiGraph()
labels = {}     # needed to map from node to tag
html_tag = html.document_fromstring(raw)
traverse(html_tag, G, labels)

pos = nx.graphviz_layout(G, prog='dot')

label_props = {'size': 9,
               'color': 'black',
               'weight': 'bold',
               'horizontalalignment': 'center',
               'verticalalignment': 'center',
               'clip_on': True}
bbox_props = {'boxstyle': "round, pad=0.2",
              'fc': "grey",
              'ec': "b",
              'lw': 1.5}

nx.draw_networkx_edges(G, pos, arrows=False)
ax = plt.gca()

for node, label in labels.items():
        x, y = pos[node]
        ax.text(x, y, label,
                bbox=bbox_props,
                **label_props)

ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
plt.show()

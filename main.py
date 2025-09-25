import utils
import graph

graph1 = {"A": ["B"],
          "B": [],
          "C": ["A", "B"],
          "D": ["C"],
          "E": ["C", "D"]}

graph1 = graph.ajouter_noeud(graph1, "F")
graph1 = graph.ajouter_noeud(graph1, "F")

graph1 = graph.ajouter_arete(graph1, "E", "F")
graph1 = graph.ajouter_arete(graph1, "E", "G")

utils.display_graph_from_dict(graph1)
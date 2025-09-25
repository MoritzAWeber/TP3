def ajouter_noeud(graph, noeud):
    """
    Add a node to a directed graph

    Args:
        graph (dict[str list[str]]): The Graph.
        noeud (str): The node to add.

    Returns:
        dict[str list[str]]: The graph with the added node (if it did not yet exist).
    """
    if noeud in graph:
        print("Node exists already. Nothing added.")
        return graph
    graph[noeud] = []

    return graph

def ajouter_arete(graph, noeud1, noeud2):
    """
    Add an edge to a directed graph

    Args:
        graph (dict[str, list[str]]): The graph.
        noeud1 (str): The starting node of the edge.
        noeud2 (str): The end node of the edge.

    Returns:
        dict[str, list[str]]: The graph with the added edge (if it did not yet exist and both nodes exist).
    """
    n1_inGraph = False
    n2_inGraph = False
    if noeud1 in graph:
        n1_inGraph = True
    if noeud2 in graph:
        n2_inGraph = True
    if not n1_inGraph or not n2_inGraph:
        print("One of the nodes does not exist in the graph.")
        return graph
    if noeud2 in graph[noeud1]:
        print("Edge exists already. Nothing added.")
        return graph
    graph[noeud1].append(noeud2)

    return graph
        
        
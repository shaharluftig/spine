import networkx as nx

default_dag_style = {
    "node_color": "tab:blue", "alpha": 0.8, "width": 2, "font_size": 12,
    "font_color": "black", "font_weight": "bold", "arrows": True,
    "arrowsize": 25, "bbox": dict(facecolor="skyblue", boxstyle="round", ec="silver", pad=0.3),
}


def topological_pos(graph: nx.DiGraph):
    """Display in topological order, with simple offsetting for legibility"""
    pos_dict = {}
    for i, node_list in enumerate(nx.topological_generations(graph)):
        x_offset = len(node_list) / 2
        y_offset = 0.1
        for j, name in enumerate(node_list):
            pos_dict[name] = (j - x_offset, -i + j * y_offset)

    return pos_dict

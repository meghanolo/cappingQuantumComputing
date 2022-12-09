# This code is part of Qiskit.
#
# (C) Copyright IBM 2021, 2022.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Code has been altered from the original"""

from typing import Optional

import numpy as np
import networkx as nx
from docplex.mp.model import Model
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import pyplot as plt

from qiskit_optimization import QuadraticProgram
from qiskit_optimization.translators import from_docplex_mp


def get_random_maxcut_docplex_model(
    *,
    draw: bool = False,
) -> Model:
    x=5
    n = 14 # Number of nodes in graph
    G = nx.Graph()
    G.add_nodes_from(np.arange(0, n, 1))
    elist=[(0,1,5),(0,2,5),(0,3,5),(0,4,1),(0,5,1),(0,6,5),(0,7,5),(0,8,5),(0,9,5),(0,10,5),(0,11,5),(0,12,1),(0,13,1),(1,6,5),(1,10,5),(2,7,5),(3,8,5),(3,9,5),(3,11,5),(4,12,1),(5,13,1)]
    
    G.add_weighted_edges_from(elist)
    edges = np.zeros([n, n])

    w = np.zeros([n, n])
    for i in range(n):
        for j in range(n):
            temp = G.get_edge_data(i, j, default=0)
            if temp != 0:
                w[i, j] = w[j, i] = temp["weight"]
    print(w)
    
    mod = Model("maxcut")
    nodes = list(range(n))
    var = [mod.binary_var(name="x" + str(i)) for i in nodes]
    mod.maximize(
        mod.sum(
            w[i, j] * (var[i] + var[j] - 2 * var[i] * var[j])
            for i in nodes
            for j in nodes
        )
    )
    
    colors = ['r' for node in G.nodes()]
    pos = nx.spring_layout(G)

    def draw_graph(G, colors, pos):
        default_axes = plt.axes(frameon=True)
        nx.draw_networkx(G, node_color=colors, node_size=600, alpha=.8, ax=default_axes, pos=pos)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels)
    
    if draw:  # pragma: no cover (tested by treon)
        draw_graph(G, colors, pos)
        #nx.draw(G, with_labels=True, font_color="whitesmoke")

    return mod


def get_random_maxcut_qp(*args, **kwargs) -> QuadraticProgram:
    """Prepare a random max-cut `QuadraticProgram`"""
    
    mod = get_random_maxcut_docplex_model(*args, **kwargs)
    return from_docplex_mp(mod)
    
    
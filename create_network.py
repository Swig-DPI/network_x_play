'''
Creator: Scott Wigle
         Qubify Labs
Date: 03/08/19
Purpose:
This script is to build a social newtork graph using networkx.
'''

import numpy as np
import pandas as pd
import networkx as nx
from itertools import count

import matplotlib.pyplot as plt
import collections
# from mpl_toolkits.basemap import Basemap as Basemap

from network_data_fill import fill

class network_create(object):
    def __init__(self,):
        self.G = nx.Graph()


    def build(self,df):
        user = list(df['users'])
        wo = df.drop(columns = ['users'])
        print('Adding nodes...')
        for i, idx in enumerate(user):
            self.G.add_node(i, loc = wo.iloc[i]['loc'])


        count = 0
        print('Adding edges...')
        for i in range(len(user)):
            user_a = user[i]
            count = 0
            for j in range(len(user[i+1:])):
                user_b = user[i+1+j]
                # create edge if worked on 112 or more projects together. The average should be 100 projects
                # This number will need to change with real WO data.  I am guessing 3-5 WO together wouldbe great.
                if sum(wo.iloc[i]==wo.iloc[i+1+j]) > 112:
                    self.G.add_edge(user_a, user_b)
                    count = count + 1

    def plot_graph(self):
        # get unique groups
        loc = set(nx.get_node_attributes(self.G,'loc').values())
        mapping = dict(zip(sorted(loc),count()))
        nodes = self.G.nodes()
        colors = [mapping[self.G.nodes[n]['loc']] for n in nodes]

        # drawing nodes and edges separately so we can capture collection for colobar
        pos = nx.spring_layout(self.G)
        ec = nx.draw_networkx_edges(self.G, pos, alpha=0.2)
        nc = nx.draw_networkx_nodes(self.G, pos, nodelist=nodes, node_color=colors,
                                    with_labels=True, node_size=100, cmap=plt.cm.jet)
        plt.colorbar(nc)
        plt.axis('off')
        plt.show()

        # spring_pos = nx.spring_layout(self.G)
        # betCent = nx.betweenness_centrality(self.G, normalized=True, endpoints=True)
        # nx.draw_networkx(self.G, pos = spring_pos, with_labels = False, node_size= 35)
        # plt.show()


    def plot_degree_graph(self):
            degree_sequence = sorted([d for n, d in self.G.degree()], reverse=True)  # degree sequence
            # print "Degree sequence", degree_sequence
            degreeCount = collections.Counter(degree_sequence)
            deg, cnt = zip(*degreeCount.items())

            fig, ax = plt.subplots()
            plt.bar(deg, cnt, width=0.80, color='b')

            plt.title("Degree Histogram")
            plt.ylabel("Count")
            plt.xlabel("Degree")
            ax.set_xticks([d + 0.4 for d in deg])
            ax.set_xticklabels(deg)

            # draw graph in inset
            plt.axes([0.4, 0.4, 0.5, 0.5])
            Gcc = sorted(nx.connected_components(self.G), key=len, reverse=True)[0]
            pos = nx.spring_layout(self.G)
            plt.axis('off')
            nx.draw_networkx_nodes(self.G, pos, node_size=20)
            nx.draw_networkx_edges(self.G, pos, alpha=0.4)

            plt.show()

    def sort_by_degree(self):
        return sorted(self.G.degree, key=lambda x: x[1], reverse=True)


if __name__ == '__main__':

    fi = fill(50,200,51)
    fi.make()
    df = fi.df

    nc = network_create()
    print('Program Running...')
    nc.build(df)
    print('Network built.  \n In ipython: \n  Type: nc.G.number_of_edges() to get edge count \n  Type: nc.G.number_of_nodes() to get node count')


    print("plotting")
    nc.plot_graph()
    nc.plot_degree_graph()
    sorted_list = nc.sort_by_degree()

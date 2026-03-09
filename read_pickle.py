"""Reads the pickle file and prints the parameters for every network."""

import pickle
import pandas

def main():
    # load the data
    with open('./data/CommunityFitNet_updated.pickle', 'rb') as infile:
        df = pickle.load(infile)
        df_edgelists = df['edges_id']

        # Print parameters for every network
        for index, row in df.iterrows():
            print(f"Index: {row['network_index']}, Nodes: {row['number_nodes']}, Edges: {row['number_edges']}, Score: {row['B_HKK_SBM_score']}, Name: {row['network_name']}")

"""
DF HAS this
Index(['network_index', 'network_name', 'title', 'description',
       'networkDomain', 'subDomain', 'citation', 'sourceUrl', 'hostedBy',
       'graphProperties', 'nodeType', 'edgeType', 'nodes_id', 'edges_id',
       'number_nodes', 'number_edges', 'ave_degree', 'labels_Q', 'labels_Q_MR',
       'labels_Q_MP', 'labels_Q_GMP', 'labels_B_NR_SBM', 'labels_B_NR_DCSBM',
       'labels_B_HKK_SBM', 'labels_cICL_HKK_SBM', 'labels_Infomap',
       'labels_MDL_SBM', 'labels_MDL_DCSBM', 'labels_S_NB', 'labels_S_cBHm',
       'labels_S_cBHa', 'labels_AMOS', 'labels_AMOS_reliablity',
       'labels_LRT_WB_DCSBM', 'Q_score', 'Q_MR_score', 'Q_MP_score',
       'Q_GMP_score', 'B_NR_SBM_score', 'B_NR_DCSBM_score', 'B_HKK_SBM_score',
       'cICL_HKK_SBM_score', 'Infomap_score', 'MDL_SBM_score',
       'MDL_DCSBM_score', 'S_NB_score', 'S_cBHm_score', 'S_cBHa_score',
       'AMOS_score', 'LRT_WB_DCSBM_score'],
      dtype='object')
"""


if __name__ == "__main__":
    main()

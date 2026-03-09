"""Reads the json file and prints the parameters for every network."""

import json
import pandas as pd


def main():
    # load the data
    with open('./data/CommunityFitNet_updated.json', 'r', encoding='utf-8') as infile:
        data = json.load(infile)

        # Print parameters for every network
        for row in data:
            print(f"Index: {row['network_index']}, Nodes: {row['number_nodes']}, Edges: {row['number_edges']}, Score: {row['B_HKK_SBM_score']}, Name: {row['network_name']}")

if __name__ == "__main__":
    main()

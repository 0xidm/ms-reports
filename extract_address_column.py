import csv
import json
import argparse

import pandas as pd


def extract_address_column(path):
    df = pd.read_csv(path)
    addresses = df['address'].tolist()

    with open('addresses.txt', 'w') as f:
        for address in addresses:
            f.write(f"{address}\n")

if __name__ == "__main__":
    # Create the parser
    my_parser = argparse.ArgumentParser(description='Extract the address column from a CSV file')

    # Add the arguments
    my_parser.add_argument('Path',
                           metavar='path',
                           type=str,
                           help='the path to the CSV file')

    # Execute the parse_args() method
    args = my_parser.parse_args()

    # Print the results
    extract_address_column(args.Path)

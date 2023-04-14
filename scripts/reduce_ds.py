import argparse
import numpy as np
import os
import pandas as pd

def reduce_dataset(args):
    sensor_list = pd.read_csv(args.sensor_list_filename).columns

    df = pd.read_hdf(args.traffic_df_filename)

    if args.n_timesteps is None:
        dfs = df[sensor_list]
    else:
        dfs = df[sensor_list].iloc[:args.n_timesteps] 

    store = pd.HDFStore(args.output_filename)
    store.put('d1', dfs, format='table', data_columns=True)
    store.close()

def main(args):
    print("Reducing dataset")
    reduce_dataset(args)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output_filename", type=str, default="data/metr-la-reduced.h5", help="Output file."
    )
    parser.add_argument(
        "--traffic_df_filename",
        type=str,
        default="data/metr-la.h5",
        help="Raw traffic readings.",
    )
    parser.add_argument(
        "--sensor_list_filename",
        type=str,
        help="Sensor ids.",
    )
    parser.add_argument(
        "--n_timesteps",
        default=None,
        type=int,
        help="Amount of timesteps.",
    )
    args = parser.parse_args()
    main(args)
import os
import pandas as pd


def load_data(iscx_path, phish_storm_path):

    if not os.path.exists(iscx_path):
        raise FileNotFoundError(f"ISCX file not found: {iscx_path}")

    if not os.path.exists(phish_storm_path):
        raise FileNotFoundError(f"PhishStorm file not found: {phish_storm_path}")

    iscx_data = pd.read_csv(iscx_path)
    phish_storm_data = pd.read_csv(phish_storm_path)

    combined_data = pd.concat(
        [iscx_data, phish_storm_data],
        ignore_index=True
    )

    combined_data = combined_data[['url', 'label']]
    combined_data.dropna(inplace=True)

    return combined_data
import pandas as pd
import numpy as np
import os


COLUMNS_TO_CHECK = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']


def load_data():
    base_path = os.path.dirname(os.path.abspath(__file__))
    datasets = {
        "Benin": pd.read_csv(os.path.join(base_path, '../data/benin-malanville.csv')),
        "Togo": pd.read_csv(os.path.join(base_path, '../data/togo-dapaong_qc.csv')),
        "Sierra Leone": pd.read_csv(os.path.join(base_path, '../data/sierraleone-bumbuna.csv'))
    }
    return datasets

def clean_data(df):
    df = df[(df[COLUMNS_TO_CHECK] >= 0).all(axis=1)]
    z_scores = np.abs((df[COLUMNS_TO_CHECK] - df[COLUMNS_TO_CHECK].mean()) / df[COLUMNS_TO_CHECK].std())
    df = df[(z_scores < 3).all(axis=1)]
    return df

def clean_and_prepare_data(df):
    df_cleaned = clean_data(df)
    df_cleaned['Timestamp'] = pd.to_datetime(df_cleaned['Timestamp'])
    df_cleaned.set_index('Timestamp', inplace=True)
    return df_cleaned

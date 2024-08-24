import pandas as pd
import numpy as np

def data_quality_check(df):
    COLUMNS_TO_CHECK = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']
    data_quality = {
        "Column": COLUMNS_TO_CHECK,
        "Missing Values": df[COLUMNS_TO_CHECK].isnull().sum().values,
        "Outliers": (np.abs((df[COLUMNS_TO_CHECK] - df[COLUMNS_TO_CHECK].mean()) / df[COLUMNS_TO_CHECK].std()) > 3).sum().values,
        "Incorrect Entries": (df[COLUMNS_TO_CHECK] < 0).sum().values
    }
    return pd.DataFrame(data_quality)

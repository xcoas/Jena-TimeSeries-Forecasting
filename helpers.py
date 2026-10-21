import pandas as pd
import numpy as np

def prep_df(filename):
    df = pd.read_csv(filename)

    df['Date Time'] = pd.to_datetime(df['Date Time'], format='%d.%m.%Y %H:%M:%S')

    hours_and_minutes = df['Date Time'].dt.hour + (df['Date Time'].dt.minute / 60.0)

    df['hour_sin'] = np.sin(hours_and_minutes * (2 * np.pi / 24))
    df['hour_cos'] = np.cos(hours_and_minutes * (2 * np.pi / 24))

    df['Temp_Diff'] = df['T (degC)'].diff()

    columns_to_drop = [
        'Tpot (K)', 'VPmax (mbar)', 'Tdew (degC)', 'VPact (mbar)', 'VPdef (mbar)',
        'sh (g/kg)', 'H2OC (mmol/mol)', 'rho (g/m**3)', 'max. wv (m/s)', 'Date Time'
    ]
    df_clean = df.drop(columns=columns_to_drop)

    return df_clean
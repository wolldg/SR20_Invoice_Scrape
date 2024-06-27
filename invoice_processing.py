import pandas as pd
from invoice_reader import relay_reader
from invoice_reader import light_reader

# This is just a visually easy way for me to preprocess this
def df_processor (df):
    df['cost'] = df['cost'].str.replace(",", "")
    df['cost'] = df['cost'].astype("float64")

    df['tach_time'] = df['tach_time'].astype("float64")
    df['total_time'] = df['total_time'].astype("float64")

    df['start'] = df['start'].astype("datetime64")
    df['stop'] = df['stop'].astype("datetime64")

    df['on_gnd'] = df['stop'] - df['start']
    df['on_gnd'] = df['on_gnd'].apply(lambda x: x.days)
    #df.set_index("tail", inplace=True)
    return df

def df_processor_deux (df):
    df['cost'] = df['cost'].str.replace(",", "")
    df['cost'] = df['cost'].astype("float64")

    df['tach_time'] = df['tach_time'].astype("float64")
    df['total_time'] = df['total_time'].astype("float64")

    df['start'] = df['start'].astype("datetime64")
    df['stop'] = df['stop'].astype("datetime64")

    df['on_gnd'] = df['stop'] - df['start']
    df['on_gnd'] = df['on_gnd'].apply(lambda x: x.days)
    #df.set_index("tail", inplace=True)
    return df
import pandas as pd
from PIL import Image
import h5py

def load_hdf5(destination_path):
    return h5py.File(destination_path, 'r')

def load_image(destination_path):
    return Image.open(destination_path)

def load_csv(destination_path):
    return pd.read_csv(destination_path)

def load_tsv(destination_path):
    return pd.read_csv(destination_path, sep='\t')

def load_json(destination_path):
    return pd.read_json(destination_path)

def load_text(destination_path):
    with open(destination_path, 'r') as file:
        return file.read()

def load_parquet(destination_path):
    return pd.read_parquet(destination_path)

def load_excel(destination_path):
    return pd.read_excel(destination_path)


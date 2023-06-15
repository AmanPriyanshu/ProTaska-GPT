from .data.data_utils import *
from PIL import Image

def load_image(destination_path):
    img = Image.open(destination_path)
    return img

def file_loader(destination_path):
    extension = os.path.splitext(destination_path)[1].lower()

    if extension in ['.jpg', '.jpeg', '.png', '.gif']:
        return "img", load_image(destination_path)
    elif extension == '.csv':
        return "txt", load_csv(destination_path)
    elif extension == '.tsv':
        return "txt", load_tsv(destination_path)
    elif extension == '.json':
        return "txt", load_json(destination_path)
    elif extension in ['.txt', '.md']:
        return "txt", load_text(destination_path)
    elif extension == '.parquet':
        return "txt", load_parquet(destination_path)
    elif extension == '.xlsx':
        return "txt", load_excel(destination_path)
    else:
        return "Cannot Read Yet"
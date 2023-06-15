import json
from datasets.arrow_dataset import Dataset
import pandas as pd
from PIL import Image
import os

def load_json(destination_path):
    with open(destination_path, 'r') as file:
        json_data = json.load(file)
    meta_data = map_json_types(json_data)
    data_sample = map_json_examples(json_data)
    json_data = str(data_sample)+'\n```\nMeta Data:\n```\n'+str(meta_data)+'\n```\n'
    return json_data

def file_loader(destination_path):
    extension = os.path.splitext(destination_path)[1].lower()

    if extension in ['.jpg', '.jpeg', '.png', '.gif']:
        return load_image(destination_path)
    elif extension == '.csv':
        return load_csv(destination_path)
    elif extension == '.tsv':
        return load_tsv(destination_path)
    elif extension == '.json':
        return load_json(destination_path)
    elif extension in ['.txt', '.md']:
        return load_text(destination_path)
    elif extension == '.parquet':
        return load_parquet(destination_path)
    elif extension == '.xlsx':
        return load_excel(destination_path)
    else:
        return "Cannot Read Yet"

def load_image(destination_path):
    try:
        img = Image.open(destination_path)
        return "Image Format Correct"
    except:
        return "Not an Image"

def load_csv(destination_path):
    data = pd.read_csv(destination_path)
    # Limit to 5 rows
    data = data.head(5)
    return data.to_dict()

def load_tsv(destination_path):
    data = pd.read_csv(destination_path, sep='\t')
    # Limit to 5 rows
    data = data.head(5)
    return data.to_dict()

def load_text(destination_path):
    with open(destination_path, 'r') as file:
        # Limit to the first 500 characters
        data = file.read(500)
    return data

def load_parquet(destination_path):
    data = pd.read_parquet(destination_path)
    # Limit to 5 rows
    data = data.head(5)
    return data.to_dict()

def load_excel(destination_path):
    data = pd.read_excel(destination_path)
    # Limit to 5 rows
    data = data.head(5)
    return data.to_dict()

def map_json_types(json_input, threshold=10):
    if isinstance(json_input, dict):
        result = {}
        if len(list(json_input.keys()))<threshold:
            for key, value in json_input.items():
                result[key] = map_json_types(value)
            return result
        else:
            return "<Dict\{with lots of keys and items>\}"
    elif isinstance(json_input, list):
        if len(json_input) > 0:
            first_element = json_input[0]
            if isinstance(first_element, list) or isinstance(first_element, dict):
                return f"<List[{map_json_types(first_element)}]>"
            else:
                return f"<List[{type(first_element).__name__}]>"
        else:
            return json_input
    elif isinstance(json_input, Dataset):
        return '<```\n'+json_input.__repr__()+'\n```\n>'
    else:
        return type(json_input).__name__

def map_json_examples(json_input, threshold=10):
    if isinstance(json_input, dict):
        result = {}
        if len(list(json_input.keys()))<threshold:
            for key, value in json_input.items():
                result[key] = map_json_examples(value)
            return result
        else:
            return "<Dict\{with lots of keys and items>\}"
    elif isinstance(json_input, list):
        if len(json_input) > 0:
            first_element = json_input[0]
            if isinstance(first_element, list) or isinstance(first_element, dict):
                return f"<List[{map_json_examples(first_element)}]>"
            else:
                return f"<List[{str([str(v)[:100] for v in json_input[:3]])}]>"
        else:
            return json_input
    elif isinstance(json_input, Dataset):
        json_input = json_input.to_dict()
        return map_json_examples(json_input)
    else:
        return str(json_input)[:100]

# if __name__ == '__main__':
#     parsed_json = {"data": {"train": [["aa", "bb"], ["aa", "bb"]], "test": 0, "val": {"a": 100, "b": "c", "d": [1], "e": 4}}}
#     result = map_json_types(parsed_json)
#     output = json.dumps(result, indent=4)
#     print(output)
#     result = map_json_examples(parsed_json)
#     output = json.dumps(result, indent=4)
#     print(output)
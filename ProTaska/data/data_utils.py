import json
from datasets.arrow_dataset import Dataset

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
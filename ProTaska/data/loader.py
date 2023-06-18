'''
This script handles the ingestion process, allowing users to import datasets from various sources and preprocess them for further analysis.
'''

import os
import sys
from .ingestion import IngestionChain
from .data_utils import file_loader, map_json_types, map_json_examples
import colorama

colorama.init()

class LocalDatasetImporter:
    def __init__(self):
        self.prompt_prefix = "Data Importer: Local\n\n"
        self.superficial_meta_data = {}

    def get_meta_data(self, dataset):
        for i in range(len(dataset)):
            dictionary = dataset[i]
            absolute_path = dictionary['absolute_path']
            file = file_loader(absolute_path)
            dictionary['example'] = str(file)
            dataset[i] = dictionary
        return dataset

    def reformat_dataset(self, dataset):
        string_dataset = []
        for dictionary in dataset:
            dictionary.pop('absolute_path', None)
            dictionary_string = ""
            for key, value in dictionary.items():
                dictionary_string += str(key) + " : " + str(value)[:500] + "\n"
            string_dataset.append(dictionary_string)
        return string_dataset
            
    def walk_dataset(self, directory_path):
        self.superficial_meta_data.update({"directory_path": directory_path, "storage": "Local"})
        dataset = []
        for root, dirs, files in os.walk(directory_path):
            dirs = dirs[:5]  # Limit the dirs list to the first 5 elements
            files = files[:5]  # Limit the files list to the first 5 elements
            
            for file in files:
                # Perform actions on the file
                relative_path = os.path.relpath(os.path.join(root, file), directory_path)
                absolute_path = os.path.abspath(os.path.join(root, file))
                memory_size = os.path.getsize(absolute_path) / (1024 * 1024)  # in megabytes
                dataset.append({
                    'relative_path': relative_path,
                    'absolute_path': absolute_path,
                    'memory_size': str(round(memory_size, 4))+"mb"
                })
        dataset = self.get_meta_data(dataset)
        dataset = self.reformat_dataset(dataset)
        self.dataset = "\n\n".join(dataset)

    def ingest(self, llm, chunk_size=500, verbose=False):
        details = self.dataset
        if verbose:
            print(colorama.Fore.BLUE+"Going to summarize:\n"+colorama.Fore.RESET,colorama.Fore.GREEN+str(details)+colorama.Fore.RESET)
        llm_chain = IngestionChain(llm=llm)
        out = None
        while len(details) > 0:
            chunk = details[:chunk_size]
            details = details[chunk_size:]
            if out is None:
                out = llm_chain.run(self.prompt_prefix+chunk)
            else:
                out = llm_chain.run("Previously Summarized:\n"+out+"\n\n"+self.prompt_prefix+chunk)
        return out

class KaggleDatasetImporter(LocalDatasetImporter):
    def __init__(self):
        super().__init__()
        self.prompt_prefix = "Data Importer: Kaggle"
        try:
            import kaggle
            self.kaggle = kaggle
        except ImportError as e:
            raise Exception(e)
    
    def import_dataset(self, dataset_name, destination_path):
        self.superficial_meta_data.update({"destination_path": destination_path, "dataset_name": dataset_name, "main_class": "Kaggle"})
        # Create a directory to store the dataset
        os.makedirs(destination_path, exist_ok=True)
        # Adding the data-source to the ingestion prompt
        self.prompt_prefix += ' ('+dataset_name+')\n\n'
        # Download the dataset using Kaggle API
        self.kaggle.api.dataset_download_files(dataset_name, path=destination_path, unzip=True)
        self.walk_dataset(destination_path)

class HuggingFaceDatasetImporter(LocalDatasetImporter):
    def __init__(self):
        super().__init__()
        self.prompt_prefix = "Data Importer: HuggingFace"
        try:
            from datasets import load_dataset
            self.load_dataset = load_dataset
        except ImportError as e:
            raise Exception(e)
    
    def import_dataset(self, dataset_name, destination_path):
        self.superficial_meta_data.update({"destination_path": destination_path, "dataset_name": dataset_name, "main_class": "HuggingFace"})
        # Load the dataset using the Hugging Face datasets library
        dataset = self.load_dataset(dataset_name)
        # Adding the data-source to the ingestion prompt
        self.prompt_prefix += ' ('+dataset_name+')\n\n'
        # Save the dataset files to the specified save_path
        dataset.save_to_disk(destination_path)
        # saving the dataset as a variable since its already parsable
        self.huggingface_dataset = dataset

    def walk_dataset(self, directory_path):
        dataset = []
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                relative_path = os.path.relpath(os.path.join(root, file), directory_path)
                absolute_path = os.path.abspath(os.path.join(root, file))
                memory_size = os.path.getsize(absolute_path) / (1024 * 1024)  # in megabytes
                dataset.append({
                    'relative_path': relative_path,
                    'memory_size': str(round(memory_size, 4))+"mb"
                })
        meta_data = map_json_types(self.huggingface_dataset)
        data_sample = map_json_examples(self.huggingface_dataset)
        dataset = str(data_sample)+'\n```\nMeta Data:\n```\n'+str(meta_data)+'\n```\n'
        self.dataset = dataset
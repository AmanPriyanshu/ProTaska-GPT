'''
This script handles the ingestion process, allowing users to import datasets from various sources and preprocess them for further analysis.
'''

import os
import sys
from .ingestion import IngestionChain

class LocalDatasetImporter:
    def __init__(self):
        self.prompt_prefix = "Data Importer: Local\n\n"
    
    def walk_dataset(self, directory_path):
        dataset = []
        
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                relative_path = os.path.relpath(os.path.join(root, file), directory_path)
                absolute_path = os.path.abspath(os.path.join(root, file))
                memory_size = os.path.getsize(absolute_path) / (1024 * 1024)  # in megabytes
                
                dataset.append({
                    'relative_path': relative_path,
                    'memory_size': memory_size
                })
        return dataset

    def ingest(self, details, llm):
        print(self.prompt_prefix)
        llm_chain = IngestionChain(llm=llm)
        out = llm_chain.run(self.prompt_prefix+details)
        return out


class KaggleDatasetImporter(LocalDatasetImporter):
    def __init__(self):
        super().__init__()
        self.prompt_prefix = "Data Importer: Kaggle\n\n"
        try:
            import kaggle
            self.kaggle = kaggle
        except ImportError as e:
            raise Exception(e)
    
    def import_dataset(self, dataset_name, destination_path):
        # Create a directory to store the dataset
        os.makedirs(destination_path, exist_ok=True)
        # Download the dataset using Kaggle API
        self.kaggle.api.dataset_download_files(dataset_name, path=destination_path, unzip=True)

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
        # Load the dataset using the Hugging Face datasets library
        dataset = self.load_dataset(dataset_name)
        # Adding the data-source to the ingestion prompt
        self.prompt_prefix += ' ('+dataset_name+')\n\n'
        # Save the dataset files to the specified save_path
        dataset.save_to_disk(destination_path)
        # saving the dataset as a variable since its already parsable
        self.huggingface_dataset = dataset
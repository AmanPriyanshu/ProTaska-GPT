import argparse
from data.loader import HuggingFaceDatasetImporter, LocalDatasetImporter, KaggleDatasetImporter
from chat_models import ChatOpenAI

def describe_dataset(openai_key, importer_type, destination_path, dataset_key=None):
    """
    Generate a description of the dataset based on the selected importer type.

    Args:
        openai_key (str): OpenAI API key.
        importer_type (str): Type of dataset importer.
        destination_path (str): Destination path for the dataset.
        dataset_key (str, optional): Dataset key for Hugging Face or Kaggle dataset importers. Defaults to None.

    Returns:
        tuple: A tuple containing the dataset description and the data_ingestor object.
    """
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_key, temperature=0)
    
    if importer_type == "HuggingFaceDatasetImporter":
        data_ingestor = HuggingFaceDatasetImporter()
    elif importer_type == "KaggleDatasetImporter":
        data_ingestor = KaggleDatasetImporter()
    elif importer_type == "LocalDatasetImporter":
        data_ingestor = LocalDatasetImporter()
    else:
        raise ValueError("Invalid importer_type. Please select one of 'HuggingFaceDatasetImporter', 'KaggleDatasetImporter', or 'LocalDatasetImporter'.")

    if dataset_key:
        data_ingestor.import_dataset(dataset_key, destination_path)
    data_ingestor.walk_dataset(destination_path)
    out = data_ingestor.ingest(llm=llm)
    return f"Description: {out}", data_ingestor


def main():
    """
    Main function for processing input and generating dataset descriptions.
    """
    parser = argparse.ArgumentParser(description="Menu options for processing input.")
    parser.add_argument("openai_key", type=str, help="OpenAI Key")
    parser.add_argument("importer_type", type=str, choices=["HuggingFaceDatasetImporter", "KaggleDatasetImporter", "LocalDatasetImporter"], help="Importer Type")
    parser.add_argument("--dataset_key", type=str, help="Dataset Key (Optional)")
    parser.add_argument("destination_path", type=str, help="Destination Path")
    args = parser.parse_args()

    try:
        output = describe_dataset(args.openai_key, args.importer_type, args.destination_path, args.dataset_key)
        print("Output:", output)
    except ValueError as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()

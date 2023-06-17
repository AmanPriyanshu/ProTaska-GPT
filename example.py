from ProTaska.describer import describe_dataset
from ProTaska.ideate import main as chatbot

if __name__ == '__main__':
	openai_key = input("Enter key:\t")
	importer_type = "HuggingFaceDatasetImporter"
	dataset_key = 'mteb/tweet_sentiment_extraction'
	destination_path = './downloaded_data/'
	description = describe_dataset(openai_key, importer_type, destination_path, dataset_key)
	print()
	print(description)
	print()
	chatbot(openai_key, description)
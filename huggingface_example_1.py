from ProTaska.data.loader import HuggingFaceDatasetImporter

if __name__ == '__main__':
	data_ingestor = HuggingFaceDatasetImporter()
	data_ingestor.import_dataset('mteb/tweet_sentiment_extraction', './downloaded_data/')
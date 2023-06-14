from ProTaska.data.loader import HuggingFaceDatasetImporter
from ProTaska.data.ingestion import IngestionChain
from ProTaska.data.data_utils import map_json_types, map_json_examples
from langchain.chat_models import ChatOpenAI

with open(".secrets", "r") as f:
	openai_key = f.read()
	llm = ChatOpenAI(model_name="gpt-3.5-turbo",openai_api_key=openai_key,temperature=0)

if __name__ == '__main__':
	data_ingestor = HuggingFaceDatasetImporter()
	data_ingestor.import_dataset('mteb/tweet_sentiment_extraction', './downloaded_data/')
	directory = data_ingestor.walk_dataset('./downloaded_data/')
	meta_data = map_json_types(data_ingestor.huggingface_dataset)
	data_sample = map_json_examples(data_ingestor.huggingface_dataset)
	details=str(data_sample)+'\n```\nMeta Data:\n```\n'+str(meta_data)+'\n```\n'
	out = data_ingestor.ingest(details=details, llm=llm)
	print(out)
	
from ProTaska.data.loader import LocalDatasetImporter
from ProTaska.data.data_utils import map_json_types, map_json_examples
from langchain.chat_models import ChatOpenAI

with open(".secrets", "r") as f:
	openai_key = f.read()
	llm = ChatOpenAI(model_name="gpt-3.5-turbo",openai_api_key=openai_key,temperature=0)

if __name__ == '__main__':
	data_ingestor = LocalDatasetImporter()
	data_ingestor.walk_dataset('./downloaded_data/')
	out = data_ingestor.ingest(llm=llm)
	print(out)
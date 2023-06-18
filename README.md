# 🧑‍🎓 ProTaska-GPT

**Your AI-powered data companion 🤖**


ProTaska-GPT is an AI-powered tool designed to assist users in their data science journey. It provides a range of features and functionalities to accelerate the process of understanding and working with datasets, making it ideal for beginners in the field of data science.

## 🖊️ Key Features:

1. **Dataset Ingestion:** ProTaska-GPT seamlessly integrates with dataset sources like Kaggle and Hugging Face, allowing users to easily import and work with diverse datasets.
2. **Task Recommendations:** Leveraging its GPT backbone, ProTaska-GPT generates a customized set of tasks tailored to each dataset. These recommendations provide users with valuable project ideas and challenges to explore.
3. **Algorithm Suggestions:** Leveraging its GPT backbone, ProTaska-GPT generates a customized set of tasks tailored to each dataset. These recommendations provide users with valuable project ideas and challenges to explore.
4. **Conversational Chatbot:** ProTaska-GPT includes a conversational chatbot that allows users to discuss different techniques and scrape information from Wikipedia to provide relevant responses.

## 🔎 Objectives:
1. **Beginner-Friendly Tutorials**: ProTaska-GPT aims to automate the generation of a collection of beginner-friendly tutorials. These tutorials guide users through common data science workflows, step-by-step, fostering practical learning and skill development.

## 👨‍🏫 Tutorials:
We provide a variety of tutorials to help you get started with our AI-powered data companion.
1. [Tweet Sentiment Analysis](/Tutorials/Tweet_Sentiment_Analysis_Example.ipynb)
2. [Image Classification](/Tutorials/Image_Classification_Example.ipynb)
3. [Housing Data](/Tutorials/Housing_data_Example.ipynb)


## 📈 Installation:

`pip install ProTaska-GPT --upgrade`

## 🚀 Usage:

Importing base descriptors and ideation bot:
```
from protaska.describer import describe_dataset
from protaska.ideate import main as chatbot
```

Providing meta-data about the dataset to be used:
```
openai_key = '**open-ai-secret-key**'
importer_type = "HuggingFaceDatasetImporter"
dataset_key = 'mteb/tweet_sentiment_extraction'
destination_path = './downloaded_data/'
```

Getting automated data descriptions:
```
description, dataloader_obj = describe_dataset(openai_key, importer_type, destination_path, dataset_key)
description
```

Running an interactive ChatBot for ideation and base-code building:
```
chatbot(openai_key, description, dataloader_obj.superficial_meta_data, agent_verbose=False)
```

## 💁 Contributing

ProTaska-GPT is an open-source project, and we welcome contributions from the community. We appreciate any contributions that can help improve and enhance the tool.

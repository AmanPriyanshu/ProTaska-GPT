# 🧑‍🎓 ProTaska-GPT

**Your AI-powered data companion 🤖**


Specify your dataset of choice, and ProTaska-GPT will understand the dataset with tasks, tutorials, and actionable insights for it. Accelerate your data science journey with ease and efficiency! (Meant for people starting their journey into Data Science.)

## 🖊️ Key Features:

1. **Dataset Ingestion:** ProTaska-GPT seamlessly integrates with dataset sources like Kaggle and Hugging Face (_for now_), allowing users to easily import and work with diverse datasets.
2. **Task Recommendations:** Leveraging its GPT-backbone, it generates a customized set of tasks tailored to each dataset, providing users with valuable project ideas and challenges.
3. **Algorithm Suggestions:** Based on the dataset characteristics, it suggests suitable machine learning algorithms, enabling users to make informed decisions during their project journey.
4. **Conversational Chatbot:** Allow user to discuss about different techniques and scrape information from Wikipedia to give relevant responses.

## 🔎 Objectives:
1. **Beginner-Friendly Tutorials**: ProTaska-GPT aims to offer automated generation of a collection of beginner-friendly tutorials that guide users through common data science workflows, step-by-step, fostering practical learning and skill development.

## 👨‍🏫 Tutorials:
We have a multitude of tutorials to help get you started on using our AI-powered data companion.
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

This is an open-source project and we would be really grateful to any contributions.

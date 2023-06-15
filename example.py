#from ProTaska import describer
from ProTaska.ideate import main as chatbot

if __name__ == '__main__':
	openai_key = input("Enter key:\t")
	description = "This dataset contains tweets with sentiment labels (neutral, negative, positive) for training and testing purposes. The data is in the form of lists of tweet IDs, text, labels, and label text. The task for this dataset would be sentiment analysis, and it belongs to the field of natural language processing. The dataset has 27481 rows for training and 3534 rows for testing. The features include 'id', 'text', 'label', and 'label_text'."
	chatbot(openai_key, description)
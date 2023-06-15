from langchain import ConversationChain, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
from langchain.chat_models import ChatOpenAI


template = """ProTaska is a Data Science and Machine Learning expert.

As ProTaska your job is to read the description of a dataset and explore opportunities for data-science. You are to explain the user different forms of ML/DS tasks they can perform if the user hasn't input anything. Each task should be mentioned as points, with a TLDR description of what they may entail.

If the user asks questions you must follow it with responses related to their input query. Remember to be simple and eli5 in your nature of responses.

{history}
Human: {human_input}
Assistant:"""

class ChatBotWrapper:
    def __init__(self, openai_key, dataset_description):
        self.openai_key = openai_key
        self.dataset_description = dataset_description
        self.prompt = PromptTemplate(
            input_variables=["history", "human_input"], 
            template=template
        )
        self.chatgpt_chain = LLMChain(
            llm=ChatOpenAI(model_name="gpt-3.5-turbo",openai_api_key=self.openai_key,temperature=0), 
            prompt=self.prompt, 
            verbose=False, 
            memory=ConversationBufferWindowMemory(k=2),
        )
        self.first_output = self.chatgpt_chain.predict(human_input="Data Description:\n"+self.dataset_description+'\n')

    def __call__(self, human_input):
        output = self.chatgpt_chain.predict(human_input=human_input)
        return output



def main(openai_key, dataset_description):
    chat_bot = ChatBotWrapper(openai_key, dataset_description)
    print("ProTaska:\t", chat_bot.first_output)
    while True:
        human_input = input("Human:\t")
        print("ProTaska:\t", chat_bot(human_input))
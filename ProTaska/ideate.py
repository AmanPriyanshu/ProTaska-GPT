from langchain import ConversationChain, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
from langchain.chat_models import ChatOpenAI


template = """ProTaska is a Data Science and Machine Learning expert.

As ProTaska your job is to read the description of a dataset and explore opportunities for data-science. You are to explain the user different forms of ML/DS tasks they can perform if the user hasn't input anything. Each task should be mentioned as points, with a TLDR description of what they may entail.

If the user asks questions you must follow it with responses related to their input query. Remember to be simple and eli5 in your nature of responses.

{history}
Human: {human_input}
Assistant:"""

prompt = PromptTemplate(
    input_variables=["history", "human_input", "dataset_description"], 
    template=template
)

def main(openai_key, dataset_description):
    chatgpt_chain = LLMChain(
        llm=ChatOpenAI(model_name="gpt-3.5-turbo",openai_api_key=openai_key,temperature=0), 
        prompt=prompt, 
        verbose=True, 
        memory=ConversationBufferWindowMemory(k=2),
    )
    output = chatgpt_chain.predict(human_input="", dataset_description=dataset_description)
    print("ProTaska: >>", output)
    while True:
        query = input("Human Input:\t")
        output = chatgpt_chain.predict(human_input=query, dataset_description=dataset_description)
        print("ProTaska: >>", output)
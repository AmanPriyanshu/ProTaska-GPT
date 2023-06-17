from langchain import ConversationChain, LLMChain, PromptTemplate
from langchain.memory import ConversationSummaryBufferMemory 
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType
from langchain.agents import initialize_agent
from langchain.utilities import WikipediaAPIWrapper
from langchain.tools import Tool

wikipedia = WikipediaAPIWrapper()
wikipedia.doc_content_chars_max = 3000

template = """ProTaska is a Data Science and Machine Learning expert.

As ProTaska your job is to read the description of a dataset and explore opportunities for data-science. You are to explain the user different forms of ML/DS tasks they can perform if the user hasn't input anything. Each task should be mentioned as points, with a TLDR description of what they may entail.

If the user asks questions you must follow it with responses related to their input query. Remember to be simple and eli5 in your nature of responses.

Human: {human_input}
Assistant:"""

class ChatBotWrapper:
    def __init__(self, openai_key, dataset_description, agent_verbose=True):
        self.openai_key = openai_key
        self.dataset_description = dataset_description
        self.prompt = PromptTemplate(
            input_variables=["human_input"], 
            template=template
        )
        self.llm = ChatOpenAI(model_name="gpt-3.5-turbo",openai_api_key=self.openai_key,temperature=0)
        self.chatgpt_chain = LLMChain(
            llm=self.llm,
            prompt=self.prompt, 
            verbose=False, 
        )
        self.first_output = self.chatgpt_chain.predict(human_input="Data Description:\n"+self.dataset_description+'\n')
        input_string = template.format(human_input="Data Description:\n"+self.dataset_description+'\n')
        self.memory = ConversationSummaryBufferMemory(llm=self.llm, max_token_limit=200)
        self.memory.save_context({"input": input_string}, {"output": self.first_output})
        tools = Tool.from_function(
            func=wikipedia.run,
            name="Wikipedia",
            description="useful for when you need information and sources from Wikipedia!"
        ),
        self.agent_chain = initialize_agent(tools=tools, 
            llm=self.llm, 
            agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, 
            memory=self.memory,
            verbose=agent_verbose
        )
        self.second_output = self.agent_chain.run(self.first_output+"\n\nFind relevant sources from Wikipedia from the above techniques and advances. Also include some TLDRs in front of those links. Be specific to the ML techniques previously mentioned.")

    def __call__(self, human_input):
        output = self.agent_chain.run(human_input)
        return output

def main(openai_key, dataset_description):
    chat_bot = ChatBotWrapper(openai_key, dataset_description)
    print("ProTaska:\t", chat_bot.first_output)
    print("ProTaska-Source:\t", chat_bot.second_output)
    print()
    while True:
        human_input = input("Human:\t")
        print("ProTaska:\t", chat_bot(human_input))
        print()
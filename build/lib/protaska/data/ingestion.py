"""
Using GPT to ingest meta data and some samples to understand the dataset.
"""

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.base_language import BaseLanguageModel
from typing import List, Any, Dict

UNDERSTAND_SINGLE_DIR_OR_FILE = """\
You are a data science expert, whose task is to understand and ingest meta-data and sample data of a single file. \
Following this you are to summarize and describe the dataset within 5 lines. Your job in the future would be to run ML jobs on these files \
so please summarize from data from that perspective. Thoroughly ingest and understand features and columns based on the different attributes present. \
Even if its just a series of file names and directory walks, your job is to understand and create a summarization of what this dataset could mean. \
You can use the variable names, keys, references, folder names, and file names to understand what this dataset is.

Note: If you recieve example inputs, attempt to understand what may be the text type or while field/sector it may belong to. Basically beyond understanding \
the basic task also attempt to understand some intricate detail about it. However, if you've only been passed a deeper file's summary, attempt to carry \
it forward, as it may help the user define appropriate tasks based on it. For example: "Classification" can "Sentiment Analysis" or "Cat vs Dog" or \
"Fraud or Normal". So basically define data type (text, audio, image, files, scripts, chats, Q&A, etc.) and the appropriate task \
(classification, regression, reinforcement learning, anomaly detection, clustering, smoothening, etc.) and finally the field/topic it may belong to.

File/Directory Details:
```
{details}
```

Summary:

"""

class IngestionChain(LLMChain):
    prompt: PromptTemplate = PromptTemplate(
        input_variables=["details"],
        template=UNDERSTAND_SINGLE_DIR_OR_FILE,
    )
    llm: BaseLanguageModel

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _call(self, inputs: Dict[str, Any], *args, **kwargs) -> None:
        response = super()._call(inputs, *args, **kwargs)
        return response

    @property
    def _chain_type(self) -> str:
        return "IngestionChain"
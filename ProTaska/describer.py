from .visualize import file_loader
from .data.loader import HuggingFaceDatasetImporter, LocalDatasetImporter, KaggleDatasetImporter
from langchain.chat_models import ChatOpenAI
import gradio as gr

def process_input(openai_key, importer_type, dataset_key=None, destination_path=None):
    # Process input based on the selected importer
    llm = ChatOpenAI(model_name="gpt-3.5-turbo",openai_api_key=openai_key,temperature=0)
    if importer_type == "HuggingFaceDatasetImporter":
        data_ingestor = HuggingFaceDatasetImporter()
        data_ingestor.import_dataset(dataset_key, destination_path)
        data_ingestor.walk_dataset(destination_path)
        out = data_ingestor.ingest(llm=llm)
        return f"Description: {out}"
    elif importer_type == "KaggleDatasetImporter":
        data_ingestor = KaggleDatasetImporter()
        data_ingestor.import_dataset(dataset_key, destination_path)
        data_ingestor.walk_dataset(destination_path)
        out = data_ingestor.ingest(llm=llm)
        return f"Description: {out}"
    elif importer_type == "LocalDatasetImporter":
        data_ingestor = LocalDatasetImporter()
        data_ingestor.walk_dataset(destination_path)
        out = data_ingestor.ingest(llm=llm)
        return f"Description: {out}"
    else:
        return "Invalid selection"

iface = gr.Interface(
    fn=process_input,
    inputs=[
        gr.inputs.Textbox(label="OpenAI Key", lines=1),
        gr.inputs.Dropdown(
            label="Importer Type",
            choices=["HuggingFaceDatasetImporter", "KaggleDatasetImporter", "LocalDatasetImporter"]
        ),
        gr.inputs.Textbox(label="Dataset Key (Optional)", lines=1),
        gr.inputs.Textbox(label="Destination Path", lines=1)
    ],
    outputs=gr.outputs.Textbox(label="Output")
)

iface.launch()

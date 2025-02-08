from zenml import pipeline
from steps.ingest_data import ingest_df, DataFrameOutput
from steps.clean_data import clean_df
from steps.model_train import train_model
from steps.evaluation import evaluation_model

@pipeline
def train_pipeline(data_path: str):
    df_output = ingest_df(data_path)
    df = clean_df(df)
    df = train_model(df)
    evaluation_model(df)

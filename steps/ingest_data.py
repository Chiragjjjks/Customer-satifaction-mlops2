import logging
import pandas as pd
from zenml import step
from pydantic import BaseModel, ConfigDict

class DataFrameOutput(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)  # ✅ Allow arbitrary types
    df: pd.DataFrame

class IngestData:
    """Data ingestion class which ingests data from the source and returns a DataFrame."""

    def __init__(self, data_path: str) -> None:
        self.data_path = data_path

    def get_data(self) -> pd.DataFrame:
        df = pd.read_csv(self.data_path)
        return df

@step
def ingest_df(data_path: str) -> DataFrameOutput:
    """
    Ingest data from the given file path.

    Args:
        data_path (str): Path to the dataset.

    Returns:
        DataFrameOutput: Loaded DataFrame wrapped in Pydantic model.
    """
    try:
        ingest_data = IngestData(data_path)
        df = ingest_data.get_data()
        return DataFrameOutput(df=df)  # ✅ Wrap DataFrame in Pydantic model
    except Exception as e:
        logging.error(e)
        raise e

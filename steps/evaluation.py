import logging
import pandas as pd 
from zenml import step


@step
def evaluation_model(df:pd.DataFrame) -> None:
    """
    Evaluation of model on the ingested data.
    """
    pass
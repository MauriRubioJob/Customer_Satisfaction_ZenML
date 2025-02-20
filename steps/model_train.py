import logging
import pandas as pd
from zenml import step

@step
def train_model(df: pd.DataFrame) -> None:
    """
    Trains the model from cleaned ingested data

        Args: 
            pd.DataFrame: the ingested data
        Return:
            None
    """
    pass
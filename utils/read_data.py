from multiprocessing import Pool
from pathlib import Path
from typing import Dict, Literal

import pandas as pd

from schemes.inputs import InputScheme

from config import settings


DATAFRAME_NAME = Literal["input"]


def read_input() -> pd.DataFrame:
    df_input = pd.read_csv(Path(settings.raw_data_base_path, settings.input_file))
    return InputScheme.validate(df_input, lazy=True)


def read_all_data() -> Dict[DATAFRAME_NAME, pd.DataFrame]:
    with Pool() as p:
        result_pool = {"input": p.apply_async(read_input)}

    dataframes = {}
    completed = dict([dfname, False] for dfname in result_pool.keys())
    while True:
        for dfname, result in result_pool.items():
            if not completed[dfname] and result.ready():
                print(f"{dfname} is ready")
                dataframes[dfname] = result.get()
                completed[dfname] = True
        if all(completed.values()):
            break

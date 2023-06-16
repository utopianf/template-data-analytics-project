import pandera as pa
from pandera.typing import Series


class OutputScheme(pa.DataFrameSchema):
    dcf_account_code: Series[str]

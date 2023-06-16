import pandera as pa
from pandera.typing import Series


class InputScheme(pa.DataFrameSchema):
    dcf_account_code: Series[str]

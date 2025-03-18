# %%
import pandas as pd

df = pd.read_csv('rides.csv')
df
# %%
# Find out all the rows that have bad values
# - Missing values are not allowed
# - A plate must be a combination of at least 3 upper case letters or digits
# - Distance much be bigger than 0

import pandera as pa

#schema
schema = pa.DataFrameSchema({
    'name': pa.Column(pa.String, nullable=False),
    'plate': pa.Column(
        pa.String,
        checks=pa.Check.str_matches(r'^[A-Z0-9]{3,}$')
    ),
    'distance': pa.Column(
        pa.Float,
        checks=pa.Check(lambda v: v > 0, 
                        element_wise=True),
        element_wise=True,
    ),
})

df
# %%

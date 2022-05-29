#%%
import pandas as pd
import numpy as np
import sqlite3


import sqlite3
import pandas as pd
# Create your connection.
cnx = sqlite3.connect('du_lieu_dt.db')

df = pd.read_sql_query("SELECT * FROM dtTheoDanhGia", cnx)

print(type(df))
# %%

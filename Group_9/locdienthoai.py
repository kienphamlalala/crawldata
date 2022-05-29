#%%
import pandas as pd
import numpy as np
import sqlite3


# Create your connection.

def loc(tensql,tenbang,giadau,giacuoi,danhgia,brand):
    cnx = sqlite3.connect(tensql)

    df2 = pd.read_sql_query("SELECT * FROM "+tenbang, cnx)
    #cast df['dangia'] to int
    df2['danhgia'] = df2['danhgia'].astype(float)
    if (brand!=""):
        df2_tmp=df2.loc[(df2['price']<giacuoi)&(df2['price']>giadau)&(df2['danhgia']>=danhgia)&(df2['brand']==brand)]
    else:
        df2_tmp=df2.loc[(df2['price']<giacuoi)&(df2['price']>giadau)&(df2['danhgia']>=danhgia)]
    # most_brn=df2_tmp.loc[:,['Name','Brand','Gia','Danhgia','SoLuong','Tenhang','Link']]

    df2_tmp
    data = df2_tmp
    data
    conn = sqlite3.connect(tensql)
    cur = conn.cursor()
    cur.execute('''DROP TABLE IF EXISTS datadaloc''')
    data.to_sql('datadaloc', conn, if_exists='replace', index=False) # - writes the pd.df to SQLIte DB
    pd.read_sql('select * from datadaloc', conn)
    conn.commit()
    conn.close()

# %%

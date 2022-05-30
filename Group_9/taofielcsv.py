import pandas as pd
import numpy as np
import sqlite3


# Create your connection.

def taofilecsv(tenfile,tensql,tenbang):
    cnx = sqlite3.connect(tensql)
    
    df2 = pd.read_sql_query("SELECT * FROM "+tenbang, cnx)
    df2.to_csv(tenfile+".csv",index=False,encoding='utf-8-sig')
    cnx.close()
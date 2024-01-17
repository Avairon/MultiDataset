import pprint
from random import randint
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import pandas as pd

if __name__ == "__main__":
    ptd1 = pd.read_csv('part_01.csv')
    ptd2 = pd.read_csv('part_02.csv')
    ptd3 = pd.read_csv('part_03.csv')
    ptd4 = pd.read_csv('part_04.csv')
    ptd5 = pd.read_csv('part_05.csv')
    ptd6 = pd.read_csv('part_06.csv')
    ptd7 = pd.read_csv('part_07.csv')
    ptd8 = pd.read_csv('part_08.csv')
    ptd9 = pd.read_csv('part_09.csv')
    ptd10 = pd.read_csv('part_10.csv')
    ptd11 = pd.read_csv('part_11.csv')
    ptd12 = pd.read_csv('part_12.csv')

    ptds = [ptd1, ptd2, ptd3, ptd4, ptd5, ptd6, ptd7, ptd8, ptd9, ptd10, ptd11, ptd12]

    # shapes = [ptd1.shape[1], ptd2.shape[1], ptd3.shape[1], ptd4.shape[1], ptd5.shape[1], ptd6.shape[1], ptd7.shape[1], ptd8.shape[1], ptd9.shape[1], ptd10.shape[1], ptd11.shape[1], ptd12.shape[1]]
    
    db1 = pd.concat([ptd1, ptd9], ignore_index=True)
    db2 = pd.concat([ptd2, ptd11], ignore_index=True)
    db3 = pd.concat([ptd4, ptd7], ignore_index=True)
    db4 = pd.concat([ptd5, ptd12], ignore_index=True)
    db5 = pd.concat([ptd6, ptd10], ignore_index=True)
    db6 = pd.concat([ptd3, ptd8], ignore_index=True)

    dbraw = [db1, db2, db3, db4, db5, db6]

    db = db1

    for i in range(1, len(dbraw)):
      db = db.merge(dbraw[i], left_on='ID', right_on='ID')
    
    db.drop_duplicates()

    db.APP_COMP_TYPE.where(db.APP_COMP_TYPE.str.replace(' ','').str.isalpha(), np.nan, inplace=True) 

    #dupcol = db.columns[db.columns.duplicated()]
    db = db.T.drop_duplicates().T
    
    # db_out = db.loc[:,~db.columns.duplicated()] # удаляем дубликаты 115 cols

    print(db)

    #db = pd.concat(dbraw, ignore_index=True)

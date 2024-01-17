import pprint
from random import randint
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import pandas as pd

if __name__ == "__main__":
    ptd1 = pd.read_csv('/home/avairon/CodePython/MultiDataset/part_01.csv')
    ptd2 = pd.read_csv('/home/avairon/CodePython/MultiDataset/part_02.csv')
    ptd3 = pd.read_csv('/home/avairon/CodePython/MultiDataset/part_03.csv')
    ptd4 = pd.read_csv('/home/avairon/CodePython/MultiDataset/part_04.csv')
    ptd5 = pd.read_csv('/home/avairon/CodePython/MultiDataset/part_05.csv')
    ptd6 = pd.read_csv('/home/avairon/CodePython/MultiDataset/part_06.csv')
    ptd7 = pd.read_csv('/home/avairon/CodePython/MultiDataset/part_07.csv')
    ptd8 = pd.read_csv('/home/avairon/CodePython/MultiDataset/part_08.csv')
    ptd9 = pd.read_csv('/home/avairon/CodePython/MultiDataset/part_09.csv')
    ptd10 = pd.read_csv('/home/avairon/CodePython/MultiDataset/part_10.csv')
    ptd11 = pd.read_csv('/home/avairon/CodePython/MultiDataset/part_11.csv')
    ptd12 = pd.read_csv('/home/avairon/CodePython/MultiDataset/part_12.csv')

    ptds = [ptd1, ptd2, ptd3, ptd4, ptd5, ptd6, ptd7, ptd8, ptd9, ptd10, ptd11, ptd12]

    db = pd.concat(ptds, ignore_index = True)

    db.sort_values(by = 'ID')
    #db.info(verbose=True)
    #db.APP_COMP_TYPE.replace(500900, 228, inplace=True)

    #df5.APP_COMP_TYPE = df5.APP_COMP_TYPE.str.lower()
    #spisok = [x for x in list(db.APP_COMP_TYPE.unique()) if x == x]
    #spisok.sort()
    
    #db.APP_COMP_TYPE.where(db.APP_COMP_TYPE.str.replace(' ','').str.isalpha(), np.nan, inplace=True) 

    db.drop_duplicates()
    db =  db.loc[:, ~db.columns_duplicated()]


    print(db.head(10))
    #print(spisok)
    print(f"rows:{db.shape[0]}", f"cols:{db.shape[1]}")

    print("dublicates:", db.duplicated().any())
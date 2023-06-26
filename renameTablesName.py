from pathlib import Path;
import os
# from openpyxl import Workbook;
import pandas as pd;
# dataMsSQL = pd.read_excel('C:\excelSolution\Tablitsy-SootvetstviaImen.xlsx', sheet_name='Таблицы-Соответствия' , usecols='D');
dataPostgre = pd.read_excel('C:\excelSolution\Tablitsy-SootvetstviaImen.xlsx', sheet_name='Таблицы-Соответствия' , usecols='D , E');
p = Path("C:\excelSolution\models")
for x in p.rglob("*"):
    open_file = open(x,'r')
    read_file = open_file.read()
    print(read_file)
    # for idx , row in dataPostgre.iterrows():
    #     rowMSSQL = row['Таблица MS SQL'];
    #     rowPostgreSQL = row['Таблица PostgreSQL']
    #     print(rowPostgreSQL)
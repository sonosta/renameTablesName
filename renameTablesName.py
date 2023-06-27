from pathlib import Path;
import pandas as pd;
import re;
dataExcel = pd.read_excel('C:\excelSolution\Tablitsy-SootvetstviaImen.xlsx', sheet_name='Таблицы-Соответствия' , usecols='D , E');
p = Path("C:\excelSolution\models")
for x in p.rglob("*"):
    try:
        f = open (x , 'r' , encoding='utf-8')
        old_data = f.read()
        for idx , row in dataExcel.iterrows():
            rowMSSQL = row['Таблица MS SQL']
            rowPostgreSQL = row['Таблица PostgreSQL']
            haveTableName = old_data.find(rowMSSQL)
            if haveTableName != -1 and rowPostgreSQL != 0:
                    file = open (x , 'w' , encoding='utf-8')
                    # old_data = old_data.replace(rowMSSQL , rowPostgreSQL)
                    old_data = re.sub(rowMSSQL , rowPostgreSQL , old_data)
                    file.write(old_data)
                    print('success')
                    file.close()
    except Exception as err:
        #Ошибка может вылезать, если попытаемся прочитать папку с файлами
        print(err)
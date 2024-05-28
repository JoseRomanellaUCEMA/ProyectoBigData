import yfinance as yf
import pandas as pd
import datetime as dt
import os
import sqlite3

dict_empresas = {
    "Apple": "AAPL",
    "Amazon": "AMZN",
    "Microsoft": "MSFT",
    "Google": "GOOGL",
    "Tesla": "TSLA",
}

os.makedirs("Datasets", exist_ok=True)

start_date = dt.date(2019, 1, 1)
end_date = dt.date.today()

for key, value in dict_empresas.items():
    try:
        dataset = yf.download(value, start=start_date, end=end_date)
        file_path = os.path.join("Datasets", f"{key}.csv")
        dataset.to_csv(file_path)
        print(f"Archivo {key} cargado exitosamente en {file_path}.")
    except Exception as e:
        print(f"Error al cargar datos para {key}: {e}")

db_path = './database/stock_db.db'
os.makedirs(os.path.dirname(db_path), exist_ok=True)
conn = sqlite3.connect(db_path)
print("Connected to SQLite")
conn.close()

folder_path = './Datasets'
files = os.listdir(folder_path)

dfs = []
for file in files:
    if file.endswith('.csv'):
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        df['Empresa'] = file.split('.')[0]
        dfs.append(df)

result = pd.concat(dfs, ignore_index=True)

def write_sql_main(db_path, df, table_name):
    try:
        conn = sqlite3.connect(db_path)
        print("Connected to SQLite")
        df.to_sql(table_name, conn, if_exists='append', index=False)
        print(f"Data inserted successfully into {table_name}")
        result = 'ok'
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
        result = 'failed'
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")
    return result

write_sql_main(db_path, result, 'main')


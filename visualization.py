import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('./database/stock_db.db')

df = pd.read_sql_query("SELECT * FROM rendimiento_diario_sin_nulls", conn)

conn.close()

plt.figure(figsize=(10, 6))
plt.boxplot([df[df['Empresa'] == 'Apple']['rendimiento_diario_porcentual'],
             df[df['Empresa'] == 'Amazon']['rendimiento_diario_porcentual'],
             df[df['Empresa'] == 'Microsoft']['rendimiento_diario_porcentual'],
             df[df['Empresa'] == 'Google']['rendimiento_diario_porcentual'],
             df[df['Empresa'] == 'Tesla']['rendimiento_diario_porcentual']],
            labels=['Apple', 'Amazon', 'Microsoft', 'Google', 'Tesla'])
plt.title('Distribución del rendimiento diario de las acciones')
plt.xlabel('Empresa')
plt.ylabel('Rendimiento Diario (%)')
plt.grid(True)
plt.show()
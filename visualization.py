import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

conn = sqlite3.connect('./database/stock_db.db')

df = pd.read_sql_query("SELECT * FROM rendimiento_diario_sin_nulls", conn)

conn.close()

sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))

sns.boxplot(
    x='Empresa', 
    y='rendimiento_diario_porcentual', 
    data=df[df['Empresa'].isin(['Apple', 'Amazon', 'Microsoft', 'Google', 'Tesla'])],
    palette=['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#FF69B4']
)

plt.title('Distribución del rendimiento diario de las acciones', fontsize=15)
plt.xlabel('Empresa', fontsize=12)
plt.ylabel('Rendimiento Diario (%)', fontsize=12)

plt.show()


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
workbook1= 'diabetesnorm.xlsx'
df = pd.read_excel(workbook1)
#print(df.head())
# 1. Histograma de la distribución de edades
plt.figure(figsize=(10, 6))
plt.hist(df['age'], bins=10, color='skyblue', alpha=0.7)
plt.title('Distribución de Edad', fontsize=14)
plt.xlabel('Edad', fontsize=12)
plt.ylabel('Frecuencia', fontsize=12)
plt.grid(True)
plt.show()
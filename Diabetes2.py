import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

workbook1 = 'diabetes2.xlsx'
df = pd.read_excel(workbook1)

sns.set(style="whitegrid")

for column in df.select_dtypes(include=np.number).columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], bins=10, kde=True, color='skyblue', alpha=0.7)

    plt.title(f'Distribución de {column}', fontsize=16, fontweight='bold')
    plt.xlabel(column, fontsize=14)
    plt.ylabel('Frecuencia', fontsize=14)

    plt.grid(visible=True, linestyle='--', linewidth=0.5, alpha=0.7)

    plt.savefig(f'{column}_histograma.png', format='png', bbox_inches='tight')
    plt.savefig(f'{column}_histograma.svg', format='svg', bbox_inches='tight')
    plt.savefig(f'{column}_histograma.eps', format='eps', bbox_inches='tight')

    plt.show()

    plt.close()
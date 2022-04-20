import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


tips2 = pd.read_csv('boxplot.csv')
sns.set_theme(style="whitegrid")
ax = sns.boxplot(x="Recyclables", y="Volume(kg)", hue="City", data=tips2, palette="Set3")

plt.show()

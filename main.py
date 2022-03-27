import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame(columns=['Year', 'Range', 'Baseline_Landfill', 'Baseline_Virgin_material', 'Recycling_Waste_paper'],
                  data=[['2017', 1, -1689.2, -3875.3, 1404.5],
                        ['2017', 2, -1689.5, -4287.4, 1548.6],
                        ['2018', 1, -1480.5, -3396.6, 1231.0],
                        ['2018', 2, -1480.8, -3757.8, 1357.3],
                        ['2019', 1, -1134.8, -2603.4, 943.5],
                        ['2019', 2, -1135.0, -2880.3, 1040.3],
                        ['2020', 1, -942.3, -2161.9, 783.5],
                        ['2020', 2, -942.5, -2391.8, 863.9]])
df.set_index(['Year', 'Range'], inplace=True)
df0 = df.reorder_levels(['Year', 'Range']).sort_index()

colors = plt.cm.Paired.colors

df0 = df0.unstack(level=-1) # unstack the 'Context' column
fig, ax = plt.subplots()
(df0['Baseline_Landfill']+df0['Baseline_Virgin_material']+df0['Recycling_Waste_paper']).plot(kind='bar', color=[colors[1], colors[0]], rot=0, ax=ax)
(df0['Baseline_Virgin_material']+df0['Recycling_Waste_paper']).plot(kind='bar', color=[colors[3], colors[2]], rot=0, ax=ax)
df0['Recycling_Waste_paper'].plot(kind='bar', color=[colors[5], colors[4]], rot=0, ax=ax)

legend_labels = [f'{val} ({Year})' for val, Year in df0.columns]
ax.legend(legend_labels)

plt.tight_layout()
plt.show()
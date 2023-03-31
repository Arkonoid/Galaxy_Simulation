import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme()

chart = pd.read_csv('galaxy_data.csv')

ax = sns.jointplot(
    data=chart,
    x='SAPIENCE INDEX', y='HEIGHT', hue='MORPHOLOGY'
)

plt.show()

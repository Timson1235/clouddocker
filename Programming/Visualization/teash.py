import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('FHCode\\Programming\\Visualization\\titanic.csv')

# Fixed properties of the scatter points
sns.scatterplot(data=df,
                x='age',
                y='fare',
                c='red',     # fixed color choice
                s=50,        # fixed size choice
                marker='x')  # fixed marker choice
plt.show()  # Zeige das Diagramm an

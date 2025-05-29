import pandas as pd
import matplotlib.pyplot as plt

# Načti mrazivé dny (12.–14. května)
df = pd.read_csv('mrazive_dny.csv')

# Vytvoř sloupec s rokem
df['year'] = pd.to_datetime(df['date']).dt.year

# Vytvoř graf výskytu podle roku
df['year'].value_counts().sort_index().plot(kind='bar')
plt.title('Počet mrazivých dní během zmrzlíků podle roku')
plt.xlabel('Rok')
plt.ylabel('Počet mrazivých případů')
plt.tight_layout()
plt.show()





import pandas as pd
import matplotlib.pyplot as plt

# Načti data
df = pd.read_csv('mrazive_dny.csv')

# Převeď datum na datetime a získej den
df['day'] = pd.to_datetime(df['date']).dt.day

# Vykresli graf
df['day'].value_counts().sort_index().plot(kind='bar')
plt.title('Počet mrazivých případů podle dne (12.–14. května)')
plt.xlabel('Den v květnu')
plt.ylabel('Počet případů')
plt.xticks([0, 1, 2], ['12. května', '13. května', '14. května'])
plt.tight_layout()
plt.show()


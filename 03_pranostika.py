import pandas as pd

# Načtení upraveného souboru
df = pd.read_csv('final_kveten_12_14_min_cleaned.csv')

# Převod temperature_2m_min na číslo (pro jistotu, pokud by byl string)
df['temperature_2m_min'] = pd.to_numeric(df['temperature_2m_min'], errors='coerce')

# Filtrování mrazivých dní
df_mraz = df[df['temperature_2m_min'] < 0]

# Uložení do nového CSV souboru
df_mraz.to_csv('final_kveten_12_14_mrazive_dny.csv', index=False)

print("Soubor 'final_kveten_12_14_mrazive_dny.csv' byl vytvořen.")

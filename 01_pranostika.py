import pandas as pd

# Načti CSV s oddělovačem ;
df = pd.read_csv('final_data.csv', sep=';')

# Převod 'date' na datetime
df['date'] = pd.to_datetime(df['date'])

# Převod temperature_2m_min na číslo (pokud jsou čárky)
df['temperature_2m_min'] = pd.to_numeric(df['temperature_2m_min'].astype(str).str.replace(',', '.'), errors='coerce')

# Výběr jen 12., 13. a 14. května
df_kveten = df[(df['date'].dt.month == 5) & (df['date'].dt.day.isin([12, 13, 14]))]

# Výběr požadovaných sloupců
df_filtered = df_kveten[['date', 'temperature_2m_min', 'latitude', 'longitude']]

# Seřazení podle data (volitelné)
df_filtered = df_filtered.sort_values(by='date')

# Uložení do nového souboru
df_filtered.to_csv('final_kveten_12_14_min.csv', index=False)

print("Soubor 'final_kveten_12_14_min.csv' byl vytvořen.")

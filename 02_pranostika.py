import pandas as pd

# Načtení již vytvořeného souboru
df = pd.read_csv('final_kveten_12_14_min.csv')

# Převedení 'date' na datetime, pokud ještě není
df['date'] = pd.to_datetime(df['date'])

# Zkrácení formátu na YYYY-MM-DD
df['date'] = df['date'].dt.strftime('%Y-%m-%d')

# Uložení zpět do CSV
df.to_csv('final_kveten_12_14_min_cleaned.csv', index=False)

print("Soubor 'final_kveten_12_14_min_cleaned.csv' byl vytvořen s upraveným formátem data.")

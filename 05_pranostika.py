import pandas as pd

# Načtení vyčištěného souboru
df = pd.read_csv('final_kveten_12_14_min_cleaned.csv')

# Převeď sloupec 'date' na datetime
df['date'] = pd.to_datetime(df['date'])

# Filtrování podle jednotlivých dní
df_pankrac = df[df['date'].dt.day == 12]
df_servac = df[df['date'].dt.day == 13]
df_bonifac = df[df['date'].dt.day == 14]

# Uložení do tří samostatných souborů
df_pankrac.to_csv('pankrac_12_kveten.csv', index=False)
df_servac.to_csv('servac_13_kveten.csv', index=False)
df_bonifac.to_csv('bonifac_14_kveten.csv', index=False)

print("Soubor pro Pankráce, Serváce a Bonifáce byl úspěšně vytvořen.")

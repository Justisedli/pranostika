import pandas as pd

# Načti soubor
df = pd.read_csv('final_kveten_12_14_min_cleaned.csv')

# Spočítej počet NaN v temperature_2m_min
pocet_nan = df['temperature_2m_min'].isna().sum()
pocet_celkem = len(df)

# Vypiš výsledek
print(f"Chybných hodnot: {pocet_nan} z {pocet_celkem} ({(pocet_nan / pocet_celkem) * 100:.2f} %)")

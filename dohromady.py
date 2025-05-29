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

import pandas as pd

# Načti soubor
df = pd.read_csv('final_kveten_12_14_min_cleaned.csv')

# Spočítej počet NaN v temperature_2m_min
pocet_nan = df['temperature_2m_min'].isna().sum()
pocet_celkem = len(df)

# Vypiš výsledek
print(f"Chybných hodnot: {pocet_nan} z {pocet_celkem} ({(pocet_nan / pocet_celkem) * 100:.2f} %)")

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

import pandas as pd

# Načtení dat
df = pd.read_csv('mrazive_dny.csv')

# Převod sloupce 'date' na datetime
df['date'] = pd.to_datetime(df['date'])

# Přidání sloupců pro den a rok
df['day'] = df['date'].dt.day
df['year'] = df['date'].dt.year

# 1️⃣ Počet výskytů mrazu podle dne (12., 13., 14.)
pocty_dnu = df['day'].value_counts().sort_index()
print("🧊 Počet mrazivých případů v jednotlivých dnech:")
print(pocty_dnu)

nejcastejsi_den = pocty_dnu.idxmax()
nejcastejsi_pocet = pocty_dnu.max()
print(f"\n👉 Z dat vyplývá, že mráz se v období zmrzlíků nejčastěji vyskytoval **{nejcastejsi_den}. května**, a to ve **{nejcastejsi_pocet} případech**.")

# 2️⃣ Ve kterých letech mrzlo alespoň jeden den
unikatni_roky = df['year'].unique()
pocet_let = len(unikatni_roky)
print(f"\n📅 Mráz se mezi 12.–14. květnem vyskytl alespoň jednou ve **{pocet_let} různých letech**.")

print("Seznam let, kdy mrzlo:")
print(sorted(unikatni_roky))

# 3️⃣ (Volitelně) Výskyt mrazu podle roku (kolikrát v každém roce)
mrazy_po_rocich = df['year'].value_counts().sort_index()
print("\n📊 Počet mrazivých dní v jednotlivých letech:")
print(mrazy_po_rocich)

# Shrnutí pro komentář
nejvic_mrazu_v_roce = mrazy_po_rocich.idxmax()
max_mrazu = mrazy_po_rocich.max()
print(f"\n📈 Nejvíce mrazivých dnů během zmrzlíků bylo zaznamenáno v roce {nejvic_mrazu_v_roce} – celkem {max_mrazu} dny.") 

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




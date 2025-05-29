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

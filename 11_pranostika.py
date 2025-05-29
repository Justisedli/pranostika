import pandas as pd
import folium

# Načtení dat
df = pd.read_csv('prehled_mrazivych_dnu_podle_stanic.csv')

# Přidej souřadnice ke stanicím
stanice_data = {
    "Karlovy Vary": (50.2016, 12.9139),
    "Plzeň-Mikulka": (49.7645, 13.3787),
    "Ústí nad Labem": (50.6833, 14.0410),
    "Praha-Ruzyně": (50.1003, 14.2555),
    "České Budějovice": (48.9519, 14.4697),
    "Liberec": (50.7697, 15.0238),
    "Jičín": (50.4393, 15.3525),
    "Čáslav": (49.9407, 15.3863),
    "Pardubice": (50.0158, 15.7402),
    "Dukovany": (49.0954, 16.1344),
    "Brno-Tuřany": (49.1530, 16.6888),
    "Prostějov": (49.4525, 17.1347),
    "Holešov": (49.3205, 17.5699),
    "Ostrava-Mošnov": (49.6918, 18.1126)
}

# Vytvoření mapy
m = folium.Map(location=[49.8, 15.5], zoom_start=7)

# Přidání bodů
for _, row in df.iterrows():
    station = row['station']
    count = row['pocet_mrazivych_dnu']
    if station in stanice_data:
        lat, lon = stanice_data[station]
        folium.CircleMarker(
            location=[lat, lon],
            radius=5 + count * 1.5,  # velikost podle počtu
            popup=f"{station} ({count} dní)",
            color='blue',
            fill=True,
            fill_opacity=0.7
        ).add_to(m)

# Uložení do souboru
m.save("mapa_mrazivych_dnu.html")
print("✅ Mapa byla vytvořena: mapa_mrazivych_dnu.html")



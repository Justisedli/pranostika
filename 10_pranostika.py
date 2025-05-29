import pandas as pd
from math import radians, cos, sin, asin, sqrt

# 1️⃣ Načti data
df = pd.read_csv('mrazive_dny.csv')

# 2️⃣ Seznam stanic
stanice_data = [
    {"station": "Karlovy Vary", "kraj": "Karlovarský", "lat": 50.2016, "lon": 12.9139},
    {"station": "Plzeň-Mikulka", "kraj": "Plzeňský", "lat": 49.7645, "lon": 13.3787},
    {"station": "Ústí nad Labem", "kraj": "Ústecký", "lat": 50.6833, "lon": 14.0410},
    {"station": "Praha-Ruzyně", "kraj": "Praha", "lat": 50.1003, "lon": 14.2555},
    {"station": "České Budějovice", "kraj": "Jihočeský", "lat": 48.9519, "lon": 14.4697},
    {"station": "Liberec", "kraj": "Liberecký", "lat": 50.7697, "lon": 15.0238},
    {"station": "Jičín", "kraj": "Královéhradecký", "lat": 50.4393, "lon": 15.3525},
    {"station": "Čáslav", "kraj": "Středočeský", "lat": 49.9407, "lon": 15.3863},
    {"station": "Pardubice", "kraj": "Pardubický", "lat": 50.0158, "lon": 15.7402},
    {"station": "Dukovany", "kraj": "Vysočina", "lat": 49.0954, "lon": 16.1344},
    {"station": "Brno-Tuřany", "kraj": "Jihomoravský", "lat": 49.1530, "lon": 16.6888},
    {"station": "Prostějov", "kraj": "Olomoucký", "lat": 49.4525, "lon": 17.1347},
    {"station": "Holešov", "kraj": "Zlínský", "lat": 49.3205, "lon": 17.5699},
    {"station": "Ostrava-Mošnov", "kraj": "Moravskoslezský", "lat": 49.6918, "lon": 18.1126}
]
df_stanice = pd.DataFrame(stanice_data)

# 3️⃣ Funkce pro výpočet vzdálenosti
def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371  # poloměr Země v km
    return c * r

# 4️⃣ Najdi nejbližší stanici ke každému mrazivému dni
def prirad_stanici(radek):
    min_vzdalenost = float('inf')
    nejblizsi = None
    for _, stanice in df_stanice.iterrows():
        vzd = haversine(radek['longitude'], radek['latitude'], stanice['lon'], stanice['lat'])
        if vzd < min_vzdalenost:
            min_vzdalenost = vzd
            nejblizsi = stanice
    return pd.Series({'station': nejblizsi['station'], 'kraj': nejblizsi['kraj']})

# 5️⃣ Přiřazení a přidání sloupců
df[['station', 'kraj']] = df.apply(prirad_stanici, axis=1)

# 6️⃣ Výpočet a uložení výsledků
vyskyt_podle_stanice = df.groupby(['station', 'kraj']).size().reset_index(name='pocet_mrazivych_dnu')
vyskyt_podle_stanice = vyskyt_podle_stanice.sort_values(by='pocet_mrazivych_dnu', ascending=False)

print(vyskyt_podle_stanice)
vyskyt_podle_stanice.to_csv('prehled_mrazivych_dnu_podle_stanic.csv', index=False)


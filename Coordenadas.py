import math
import pandas as pd

# Função para calcular a distância entre dois pontos
def haversine(lat1, lon1, lat2, lon2):
    # Raio da Terra em quilômetros
    R = 6378.0
    
    # Convertendo as coordenadas de graus para radianos
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    
    # Diferenças das latitudes e longitudes
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    # Fórmula de Haversine
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Distância em quilômetros
    distance = R * c
    return distance

# Dados de coordenadas 2025 (latitude, longitude)
data = [
    "-20.822183228338172, -49.5063675573577",
    "-8.062871364433526, -34.90294263241903",
    "-19.930016186282142, -44.013927750882466",
    "-12.97881330728407, -38.50429343156842",
    "-22.89328366668088, -43.292231999361235",
    "-23.545342906798965, -46.47421310668807",
    "-23.951014212998047, -46.33882500602809",
    "-19.865869464567098, -43.97111011964356",
    "-3.807240579373143, -38.52240627786332",
    "-22.912151117637194, -43.2301551066958",
    "-22.912151117637194, -43.2301551066958",
    "-3.807240579373143, -38.52240627786332",
    "-29.974054775600386, -51.194922695487485",
    "-30.065600510371148, -51.23589458276787",
    "-29.162360808474226, -51.17617991450056",
    "-23.52763551986749, -46.678430272503206",
    "-22.965394045707782, -46.537484823707736",
    "-23.60101079597613, -46.720076950889634",
    "-22.89117468388948, -43.22810170856672",
    "-12.919475028286602, -38.42821113554098"
]
# Dados 2024
# data = [
#     "-25.447969403250738, -49.27697050671818",
#     "-16.67105434916062, -49.284635057259145",
#     "-19.930016186282142, -44.013927750882466",
#     "-12.97881330728407, -38.50429343156842",
#     "-22.89328366668088, -43.292231999361235",
#     "-23.545342906798965, -46.47421310668807",
#     "-28.684431654546955, -49.36770206811713",
#     "-19.865869464567098, -43.97111011964356",
#     "-15.604041364203747, -56.121647753522495",
#     "-22.912151117637194, -43.2301551066958",
#     "-22.912151117637194, -43.2301551066958",
#     "-3.807240579373143, -38.52240627786332",
#     "-29.974054775600386, -51.194922695487485",
#     "-30.065600510371148, -51.23589458276787",
#     "-29.162360808474226, -51.17617991450056",
#     "-23.52763551986749, -46.678430272503206",
#     "-22.965394045707782, -46.537484823707736",
#     "-23.60101079597613, -46.720076950889634",
#     "-22.89117468388948, -43.22810170856672",
#     "-12.919475028286602, -38.42821113554098"
# ]
# Convertendo os dados em um DataFrame
df = pd.DataFrame(data, columns=["Coordinates"])
df[['Latitude', 'Longitude']] = df['Coordinates'].str.split(',', expand=True)
df['Latitude'] = df['Latitude'].astype(float)
df['Longitude'] = df['Longitude'].astype(float)

# Criando uma matriz de distâncias
distances = []

# Calculando a distância entre todas as coordenadas
for i in range(len(df)):
    row_distances = []
    for j in range(len(df)):
        lat1, lon1 = df.loc[i, 'Latitude'], df.loc[i, 'Longitude']
        lat2, lon2 = df.loc[j, 'Latitude'], df.loc[j, 'Longitude']
        distance = haversine(lat1, lon1, lat2, lon2)
        row_distances.append(distance)
    distances.append(row_distances)

# Convertendo para DataFrame para uma melhor visualização
distance_matrix = pd.DataFrame(distances)

# Adicionando uma coluna com a soma das distâncias de cada linha
distance_matrix['Soma das Distâncias'] = distance_matrix.sum(axis=1)

# Exportando o DataFrame para um arquivo CSV
distance_matrix.to_csv('matriz_distancias2025a.csv', index=False)

print("A tabela foi exportada para 'matriz_distancias.csv'")

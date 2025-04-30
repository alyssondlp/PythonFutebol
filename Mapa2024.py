import folium

# Lista de coordenadas
data = [
    [-49.27697051, -25.4479694],
    [-49.28463506, -16.67105435],
    [-44.01392775, -19.93001619],
    [-38.50429343, -12.97881331],
    [-43.292232, -22.89328367],
    [-46.47421311, -23.54534291],
    [-49.36770207, -28.68443165],
    [-43.97111012, -19.86586946],
    [-56.12164775, -15.60404136],
    [-43.23015511, -22.91215112],
    [-43.23015511, -22.91215112],
    [-38.52240628, -3.807240579],
    [-51.1949227, -29.97405478],
    [-51.23589458, -30.06560051],
    [-51.17617991, -29.16236081],
    [-46.67843027, -23.52763552],
    [-46.53748482, -22.96539405],
    [-46.72007695, -23.6010108],
    [-43.22810171, -22.89117468],
    [-38.42821114, -12.91947503],
    [-46.02443752, -21.51795356]  # Novo ponto em vermelho
]

# Criar o mapa centralizado na média das coordenadas
m = folium.Map(location=[-23.951012841834878, -
               46.33883048441824], zoom_start=5)

# Adicionar os pontos como bolinhas no mapa
for coord in data:
    # Definir a cor para o último ponto como vermelho
    color = "red" if coord == [-46.02443752, -21.51795356] else "blue"

    folium.CircleMarker(
        location=[coord[1], coord[0]],  # Ordem: [latitude, longitude]
        radius=6,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.6
    ).add_to(m)

# Salvar o mapa em um arquivo HTML
m.save("mapa_com_pontos_novos.html")

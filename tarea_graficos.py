#Tarea gráficos en Python
#Ejecutar los códigos en la terminal para la instalación de las librerías utilizadas
#python -m pip install pandas plotly xlrd nbformat geopandas unidecode (Isaac*)
#py -m pip install pandas (lectura de link externo)
#py -m pip install plotly (creación de gráficos dinámicos)
#py -m pip install xlrd (soporte de lectura del archivo de los datos)
#py -m pip install nbformat (soporte para verlo en laptop)
#py -m pip install geopandas (poder leer arvhivos .zip)
#py -m pip install unidecode (para normalizar los datos)

#%%
import pandas as pd
import numpy as np
import plotly.express as px

link = 'https://sitiooij.poder-judicial.go.cr/phocadownload/Estadisticas/estadsticaspoliciales2024.xls'
datos = pd.read_excel(link)

filtro = datos["Provincia"] != "DESCONOCIDO" #los valores se transforman en booleanos y excluye DESCONOCIDO
datos_filtrados = datos[filtro] #los valores se convierten en un data frame
provincias = datos_filtrados['Provincia'].value_counts()
orden_provincias = provincias.index.tolist()

fig = px.bar(
        x=provincias.values, 
        y=provincias.index,
        orientation= 'h',
        height=400,
        title="Cantidad de delitos por provincia en 2024",
        color=provincias.values,
        color_continuous_scale=[(0.00, "#c8ecca"),   (0.25, "#97ca99"),
                                (0.30, "#7bba91"), (0.50, "#559f80"),
                                (0.60, "#2e846f"),  (1.00, "#006a5e")],
        category_orders={"y": orden_provincias}
)

fig.update_traces(
    hovertemplate="<b>Provincia:</b> %{y}<br>" +
                  "<b>Delitos:</b> %{x:,}<br>" +
                  "<extra></extra>" 
)

fig.update_xaxes(title_text='Provincias')
fig.update_yaxes(title_text='Cantidad de Delitos')

fig.show()
#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

link = 'https://sitiooij.poder-judicial.go.cr/phocadownload/Estadisticas/estadsticaspoliciales2024.xls'
datos = pd.read_excel(link)

filtro = datos["Provincia"] != "DESCONOCIDO" #los valores se transforman en booleanos y excluye DESCONOCIDO
datos_filtrados = datos[filtro] #los valores se convierten en un data frame
provincias = datos_filtrados['Provincia'].value_counts()

pivot_df = pd.crosstab(index=datos_filtrados['Provincia'], 
                      columns=datos_filtrados['Delito'])

num_delitos = len(pivot_df.columns)

COLORES_DELITOS =["#e0f3db", "#a2d2a4", "#7bba91", "#559f80", "#2e846f", "#006a5e"][:num_delitos]

pivot_df.plot.bar(stacked=True,
                  grid=True,
                  color=COLORES_DELITOS,
                  zorder=3)

plt.show()
# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

link = 'https://sitiooij.poder-judicial.go.cr/phocadownload/Estadisticas/estadsticaspoliciales2024.xls'
datos = pd.read_excel(link)

filtro_incluir = (datos["Provincia"] == "CARTAGO") | (datos["Provincia"] == "HEREDIA") #Filtro para solo inlcuir a Cartago y Heredia
filtro_final = filtro_incluir & (datos["Provincia"] != "DESCONOCIDO") #Filtro para excluir a DESCONOCIDO
datos_filtrados = datos[filtro_final] #los valores se convierten en un data frame
provincias = datos_filtrados['Provincia'].value_counts()

pivot_df = pd.crosstab(index=datos_filtrados['Provincia'], 
                       columns=datos_filtrados['Delito'])
pivot_df = pivot_df.loc[pivot_df.sum(axis=1).sort_values(ascending=False).index]


fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.12 
x = np.arange(len(pivot_df.index)) 
num_sub_cats = len(pivot_df.columns)

offset_group_start = x - (bar_width * num_sub_cats / 2) + (bar_width / 2) 

COLORES_DELITOS =["#e0f3db", "#a2d2a4", "#7bba91", "#559f80", "#2e846f", "#006a5e"][:num_sub_cats] 

for i, sub_cat in enumerate(pivot_df.columns):
    ax.bar(
        offset_group_start + (i * bar_width),
        pivot_df[sub_cat],
        width=bar_width,
        label=sub_cat,
        color=COLORES_DELITOS[i]
    )

ax.set_xlabel("Provincias")
ax.set_ylabel("Cantidad de Delitos")
ax.set_title("Comparativa de Delitos entre Cartago y Heredia", loc="left")
ax.set_xticks(x)
ax.set_xticklabels(pivot_df.index)

ax.set_axisbelow(True)
ax.grid(axis='y', zorder=0)

ax.legend(title="Tipo de Delito",
          bbox_to_anchor=(1.01, 1),
            loc='upper left')

plt.show()
# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#link de datos
link = 'https://sitiooij.poder-judicial.go.cr/phocadownload/Estadisticas/estadsticaspoliciales2024.xls'
datos = pd.read_excel(link)

filtro_incluir = (datos["Provincia"] == "SAN JOSE") #Filtro para solo inlcuir a San José
filtro = datos["Provincia"] != "DESCONOCIDO" #los valores se transforman en booleanos y excluye DESCONOCIDO
datos_filtrados = datos[filtro] #los valores se convierten en un data frame
delitos = datos_filtrados['Delito'].value_counts()
orden_delitos = delitos.index.tolist()

my_circle = plt.Circle( (0,0), 0.7, color='white')


plt.pie(delitos, labels=orden_delitos, colors= ["#006a5e", "#2e846f", "#559f80", "#7bba91", "#a2d2a4", "#e0f3db"])
p = plt.gcf()
p.gca().add_artist(my_circle)
# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

link = 'https://sitiooij.poder-judicial.go.cr/phocadownload/Estadisticas/estadsticaspoliciales2024.xls'
datos = pd.read_excel(link)

filtro = datos["Provincia"] == "SAN JOSE" #los valores se transforman en booleanos y excluye DESCONOCIDO
datos_filtrados = datos[filtro] #los valores se convierten en un data frame
delitos = datos_filtrados['Delito'].value_counts()
orden_delitos = delitos.index.tolist()

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

link = 'https://sitiooij.poder-judicial.go.cr/phocadownload/Estadisticas/estadsticaspoliciales2024.xls'
datos = pd.read_excel(link)

datos["Fecha"] = pd.to_datetime(datos["Fecha"], errors='coerce')
datos['Nombre_Mes'] = datos["Fecha"].dt.month_name(locale='es_ES')
datos['Numero_Mes'] = datos["Fecha"].dt.month
datos_limpios = datos.dropna(subset=['Nombre_Mes'])

conteo_mensual = datos_limpios.groupby(['Numero_Mes', 'Nombre_Mes']).size().reset_index(name='Total_Delitos')
conteo_mensual = conteo_mensual.sort_values(by='Numero_Mes')

fig, ax = plt.subplots(figsize=(10, 6)) 

plt.plot('Nombre_Mes', 'Total_Delitos', 
         data=conteo_mensual, 
         linestyle='-', 
         marker='o', 
         color='#7bba91',
         label='Total Delitos')


plt.title("Distribución de Delitos por Mes en 2024", loc='left')
plt.xlabel("Mes")
plt.ylabel("Cantidad de Delitos")

fig.autofmt_xdate(rotation=35) 

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend() 
plt.show()

# ISAAC
# %% Nuevo Gráfico: Barras Verticales (Total Delitos por Mes)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Se reutiliza el código de limpieza de la sección de Línea para tener los datos mensuales
link = 'https://sitiooij.poder-judicial.go.cr/phocadownload/Estadisticas/estadsticaspoliciales2024.xls'
datos = pd.read_excel(link)

datos["Fecha"] = pd.to_datetime(datos["Fecha"], errors='coerce')
datos['Nombre_Mes'] = datos["Fecha"].dt.month_name(locale='es_ES')
datos['Numero_Mes'] = datos["Fecha"].dt.month
datos_limpios = datos.dropna(subset=['Nombre_Mes'])

conteo_mensual = datos_limpios.groupby(['Numero_Mes', 'Nombre_Mes']).size().reset_index(name='Total_Delitos')
conteo_mensual = conteo_mensual.sort_values(by='Numero_Mes')
meses = conteo_mensual['Nombre_Mes']
delitos_mes = conteo_mensual['Total_Delitos']

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(meses, delitos_mes, color='#559f80', zorder=3)

ax.set_title("Distribución de Delitos por Mes (Barras Verticales)", loc='left')
ax.set_xlabel("Mes")
ax.set_ylabel("Cantidad de Delitos")

ax.set_axisbelow(True)
ax.grid(axis='y', linestyle='--', alpha=0.7, zorder=0)
fig.autofmt_xdate(rotation=35) 

plt.show()

# %% Nuevo Gráfico: Barras Simples (Delitos por Provincia)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

link = 'https://sitiooij.poder-judicial.go.cr/phocadownload/Estadisticas/estadsticaspoliciales2024.xls'
datos = pd.read_excel(link)

filtro = datos["Provincia"] != "DESCONOCIDO" 
datos_filtrados = datos[filtro]
provincias_conteo = datos_filtrados['Provincia'].value_counts()
provincias_ordenadas = provincias_conteo.index.tolist()

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(provincias_ordenadas, provincias_conteo.values, color='#006a5e', zorder=3)

ax.set_title("Total de Delitos por Provincia (Barras Simples)", loc='left')
ax.set_xlabel("Provincia")
ax.set_ylabel("Cantidad de Delitos")

ax.set_axisbelow(True)
ax.grid(axis='y', linestyle='--', alpha=0.7, zorder=0)

plt.show()

# %% Nuevo Gráfico: Barras 100% (Distribución Porcentual de Delito por Provincia)
import pandas as pd
import plotly.express as px

link = 'https://sitiooij.poder-judicial.go.cr/phocadownload/Estadisticas/estadsticaspoliciales2024.xls'
datos = pd.read_excel(link)

filtro = datos["Provincia"] != "DESCONOCIDO" 
datos_filtrados = datos[filtro]

# Crea una tabla de frecuencias de Delito por Provincia
df_crosstab = pd.crosstab(datos_filtrados['Provincia'], datos_filtrados['Delito'])

# Calcula el porcentaje: divide cada valor entre la suma total de su fila (axis=1)
df_percent = df_crosstab.apply(lambda x: x / x.sum(), axis=1)
df_percent = df_percent.stack().reset_index(name='Porcentaje')
df_percent['Porcentaje'] = df_percent['Porcentaje'] * 100 # Convertir a %

# Usa Plotly para un gráfico de barras 100% (con mode='percent')
fig = px.bar(
    df_percent,
    x='Porcentaje', 
    y='Provincia',
    color='Delito',
    orientation='h',
    height=500,
    title="Distribución Porcentual (100%) de Delitos por Provincia",
    color_discrete_sequence=["#006a5e", "#2e846f", "#559f80", "#7bba91", "#a2d2a4", "#e0f3db"],
    category_orders={"y": df_percent['Provincia'].unique().tolist()}
)

fig.update_layout(xaxis_title='Porcentaje de Delitos', yaxis_title='Provincia')
fig.update_traces(
    hovertemplate="<b>Provincia:</b> %{y}<br>" +
                  "<b>Delito:</b> %{customdata[0]}<br>" + 
                  "<b>Porcentaje:</b> %{x:.2f}%%<extra></extra>",
    customdata=df_percent[['Delito']]
)
fig.show()

# %% Nuevo Gráfico: Pirámide (Comparativa Delitos San José vs Alajuela)
import pandas as pd
import plotly.express as px

link = 'https://sitiooij.poder-judicial.go.cr/phocadownload/Estadisticas/estadsticaspoliciales2024.xls'
datos = pd.read_excel(link)

# Filtrar solo San José y Alajuela
provincias_a_comparar = ["SAN JOSE", "ALAJUELA"]
datos_comparativa = datos[datos["Provincia"].isin(provincias_a_comparar)].copy()

# Contar la ocurrencia de cada Delito en cada Provincia
delitos_conteo = datos_comparativa.groupby(['Delito', 'Provincia']).size().reset_index(name='Total_Delitos')

# Para la pirámide, los datos de un lado deben ser negativos (eje x)
delitos_conteo['Total_Delitos_Piramide'] = delitos_conteo.apply(
    lambda row: row['Total_Delitos'] * -1 if row['Provincia'] == 'ALAJUELA' else row['Total_Delitos'], axis=1
)

# Usa Plotly para crear la pirámide (gráfico de barras lateral a lateral)
fig = px.bar(
    delitos_conteo, 
    x='Total_Delitos_Piramide', 
    y='Delito', 
    color='Provincia',
    orientation='h',
    height=800,
    title="Pirámide de Delitos: Comparativa San José vs Alajuela",
    color_discrete_sequence=['#006a5e', '#559f80'] # Usando tus colores
)

fig.update_layout(
    barmode='relative',
    xaxis=dict(
        tickvals=[-1000, -500, 0, 500, 1000], # Ejemplo de valores, ajusta según tus datos
        ticktext=['1000', '500', '0', '500', '1000'],
        title='Cantidad de Delitos'
    ),
    yaxis=dict(title='Tipo de Delito')
)

fig.update_traces(
    hovertemplate="<b>Provincia:</b> %{customdata[0]}<br>" +
                  "<b>Delitos:</b> %{x|:,.0f}<br>" +
                  "<extra></extra>",
    customdata=delitos_conteo[['Provincia']]
)

fig.show()

# %% Nuevo Gráfico: Araña (Radar) - Matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from math import pi

link = 'https://sitiooij.poder-judicial.go.cr/phocadownload/Estadisticas/estadsticaspoliciales2024.xls'
datos = pd.read_excel(link)

provincias_radar = ["SAN JOSE", "HEREDIA", "CARTAGO"]
datos_radar = datos[datos["Provincia"].isin(provincias_radar)].copy()

# Crear tabla cruzada para contar delitos por provincia
df_radar = pd.crosstab(datos_radar['Provincia'], datos_radar['Delito'])
df_radar = df_radar.T # Transponer para que los delitos sean las filas (ejes del radar)

# 1. Normalizar los datos: Escalar los valores entre 0 y 1 para que el gráfico sea comparable
df_normalized = (df_radar - df_radar.min()) / (df_radar.max() - df_radar.min())
categories = df_normalized.index.tolist()
N = len(categories)

# 2. Preparar el ángulo para cada eje
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1] # Cierra el círculo

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# 3. Dibujar cada provincia
for i, provincia in enumerate(provincias_radar):
    values = df_normalized[provincia].values.flatten().tolist()
    values += values[:1] # Cierra la línea

    # Dibujar la línea y el área
    color = ["#006a5e", "#559f80", "#a2d2a4"][i]
    ax.plot(angles, values, linewidth=2, linestyle='solid', label=provincia, color=color)
    ax.fill(angles, values, color=color, alpha=0.2)

# 4. Configuración del gráfico
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, size=8) # Etiquetas de los delitos
ax.set_yticks([0.25, 0.50, 0.75, 1.00]) # Puntos de la escala
ax.set_yticklabels(["25%", "50%", "75%", "100%"], color='grey', size=7)
ax.set_ylim(0, 1)

plt.title("Gráfico de Araña: Comparativa de Delitos Normalizados (San José, Heredia, Cartago)", size=12, y=1.1, loc='left')
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.show()
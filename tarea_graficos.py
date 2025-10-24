#Tarea gráficos en Python
#Ejecutar los códigos en la terminal para la instalación de las librerías utilizadas
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
# %%

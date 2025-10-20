#Tarea gráficos en Python
#Ejecutar los códigos en la terminal para la instalación de las librerías utilizadas
#py -m pip install pandas (lectura de link externo)

#py -m pip install plotly (creación de gráficos dinámicos)

#py -m pip install xlrd (soporte de lectura del archivo de los datos)

#py -m pip install nbformat (soporte para verlo en laptop)

#%%
import pandas as pd
import numpy as np
import plotly.express as px

link = 'https://sitiooij.poder-judicial.go.cr/phocadownload/Estadisticas/estadsticaspoliciales2024.xls'
datos = pd.read_excel(link)

filtro = datos["Provincia"] != "DESCONOCIDO" #los valores se transforman en booleanos
datos_filtrados = datos[filtro] #los valores se convierten en un data frame
provincias = datos_filtrados['Provincia'].value_counts()

fig = px.bar(
        x=provincias.index, 
        y=provincias.values,
        title="Cantidad de delitos por provincia en 2024",
        color=provincias.values,
        color_continuous_scale=[(0.00, "#e0f3db"),   (0.10, "#a2d2a4"),
                                (0.15, "#7bba91"), (0.50, "#559f80"),
                                (0.66, "#2e846f"),  (1.00, "#006a5e")]
)

fig.update_traces(
    hovertemplate="<b>Provincia:</b> %{x}<br>" +
                  "<b>Delitos:</b> %{y:,}<br>" +
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

filtro = datos["Provincia"] != "DESCONOCIDO" #los valores se transforman en booleanos
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

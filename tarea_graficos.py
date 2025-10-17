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

provincias = datos['Provincia'].value_counts()

fig = px.bar(
        x=provincias.index, 
        y=provincias.values,
        title="Cantidad de delitos por provincia en 2024",
        color=provincias.values,
        color_continuous_scale=[(0.00, "#006a5e"), (0.33, "#559f80"),
                                (0.33, "#7bba91"), (0.66, "#a2d2a4"),
                                (0.66, "#c8e8c3"), (1.00, "#e0f3db")]
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



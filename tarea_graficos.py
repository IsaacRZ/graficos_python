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
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

link = 'https://sitiooij.poder-judicial.go.cr/phocadownload/Estadisticas/estadsticaspoliciales2024.xls'
datos = pd.read_excel(link)

filtro = datos["Provincia"] != "DESCONOCIDO" #los valores se transforman en booleanos
datos_filtrados = datos[filtro] #los valores se convierten en un data frame
provincias = datos_filtrados['Provincia'].value_counts()
orden_provincias = provincias.index.tolist()

pivot_df = data.pivot(index="category", columns="sub_category", values="value")
totals = pivot_df.sum(axis=1)

fig, ax = plt.subplots(figsize=(7, 5))

bar_width = 0.25
x = np.arange(len(pivot_df.index))

ax.bar(x, totals, width=bar_width * 3.5, color="lightgrey", zorder=0, label="Total")

for i, sub_cat in enumerate(pivot_df.columns):
    ax.bar(
        x + (i - 1) * bar_width,
        pivot_df[sub_cat],
        width=bar_width,
        label=sub_cat,
        zorder=1,
    )

ax.set_xlabel("Category")
ax.set_ylabel("Value")
ax.set_title("Regions - Revenue by Segment", loc="left")
ax.set_xticks(x)
ax.set_xticklabels(pivot_df.index)
ax.legend(title="Sub Category")

fig.savefig(
    "../../static/graph/grouped-barplot-with-the-total-of-each-group-represented-as-a-grey-rectangle.png",
    dpi=100,
    bbox_inches="tight",
)
plt.show()
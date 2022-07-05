from os import getenv
from typing import Dict, List
import shimoku_api_python as Shimoku
import pandas as pd
import numpy as np
df = pd.DataFrame = pd.read_csv('datos.csv')
print('cargando datos df')
valorMaximo=df.max()
valorMinimo=df.min()
imax= str(valorMaximo[1])
rmax= str(valorMaximo[2])
imin= str(valorMinimo[1])
rmin= str(valorMinimo[2])
# codigo shimoku
html=(
      "<p style='background-color: '#daf4f0';>"
      "<b>Descripcion</b>: Esta grafico permite mostrar los picos de "
      "instalaciones y registros, realizados durante un dia de trabajo.</p>"
     )
env='prod'
menu_path="PruebaConcepto/Reporte"
acces_token  = getenv(env,'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
universe_id: str = getenv(env,'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx')
business_id: str = getenv(env,'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx')
print('Entornos creados')
shimoku = Shimoku.Client(
    config={'access_token': acces_token},
    universe_id = universe_id,
    environment='production',
)
print('Cliente configurado')
shimoku.plt.set_business(business_id)
report: Dict = shimoku.plt.bar(
    df,x='hora', y=['instalado','registrados'],
    menu_path=menu_path,
    order=0,
    title='Instalaciones y Registros',
)
print ('Grafica generada')
shimoku.plt.html(
    html=html,
    menu_path=menu_path,
    order=1, rows_size=2, cols_size=12,
)
print ('Html generado')
data_=[
    {
       "description":"",
       "title":"Max.Instalado",
       "value":imax,
       "align":"center",
       "color":"red",
    },
   {
       "description":"",
       "title":"Max.Registrado",
       "value":rmax,
       "align":"center",
       "color":"success",
   },
   {
       "description":"",
       "title":"Min.Instalado",
       "value":imin,
       "align":"center",
       "color":"blue",
   },
   {
       "description":"",
       "title":"Min.Registrado",
       "value":rmin,
       "align":"center",
       "color":"orange",
   },
]
print ('cargando indicadores')
shimoku.plt.indicator(
    data=data_,
    menu_path=menu_path,
    order=2,
    rows_size=2, cols_size=12,
    value='value',
    header="title",
    footer='description',
    align='align',
    color='color',
)
print ('DataWebApp creada')

from os import getenv
from typing import Dict, List
import shimoku_api_python as Shimoku
import pandas as pd
import numpy as np
env ='prod'
menu="PruebaConcepto2/Reporte"
acces_token = getenv(env,'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
universe_id: str = getenv(env,'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx')
business_id: str = getenv(env, 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx')
shimoku = Shimoku.Client(
	    config={'access_token':acces_token},
	    universe_id = universe_id,
	    environment = 'production',
	)
shimoku.plt.set_business(business_id)
cont="Descripción para el html de la gráfica de barras."
df = pd.DataFrame = pd.read_csv('datos.csv')	
def BuscaMaxMin(M,tipo,df):
	if (M == 'max'):
		valorMax = df.max()
		if (tipo == 'i'):
			vm = str(valorMax[1])
		if (tipo == 'r'):
			vm = str(valorMax[2])
	if (M == 'min'):
		valorMin = df.min()
		if (tipo == 'i'):
			vm = str(valorMin[1])
		if (tipo == 'r'):
			vm = str(valorMin[2])
	return vm
def DescripHtml(cont,orden,menu,row,col):
	html=(
		  "<p><b>Descripción:</b>" + cont +" </p>"
		)
	shimoku.plt.html(
	    html=html,
	    menu_path = menu,
	    order=orden,
	    rows_size=row,
	    cols_size=col
		)
def GraficaBarras(menu,orden,titulo,df):
	report: Dict = shimoku.plt.bar(
	       df,x='hora',y=['instalado','registrados'],
	       menu_path = menu,
	       order = orden,	
	       title = titulo,
		)
def Indicadores(menu,orden,df):
	data_=[
		{
			"description":"",
			"title":"Max.Instalado",
			"value":BuscaMaxMin('max','i',df),
			"align":"center",
			"color":"red",
		},
		{
			"description":"",
			"title":"Max.Registrado",
			"value":BuscaMaxMin('max',"r",df),
			"align":"center",
			"color":"success",
		},
		{
			"description":"",
			"title":"Min.Registrado",
			"value":BuscaMaxMin("min",'r',df),
			"align":"center",
			"color":"orange",
		},
		{
			"description":"",
			"title":"Min.Instalado",
			"value":BuscaMaxMin("min",'i',df),
			"align":"center",
			"color":"blue",
		},
	]
	shimoku.plt.indicator(
        data=data_,
    	menu_path=menu,
    	order=orden,
    	rows_size=2, cols_size=12,
    	value='value',
    	header="title",
    	footer='description',
    	align='align',
    	color='color',
		)
def principal ():
	print ("Creando indicadores")
	Indicadores(menu,0,df)
	print ("Indicadores creados")
	print ("creando gráfica de barras")
	GraficaBarras(menu,1,'Instalaciones y registros',df)
	print ("Grafica de barras creada")
	print ("Generando html")
	DescripHtml(cont,2,menu,3,12)
	print ("html crreado")
	print ("Webapp creada")

principal ()
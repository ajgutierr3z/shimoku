from os import getenv
from typing import Dict, List
import shimoku_api_python as Shimoku
import pandas as pd
import numpy as np
import time as t

env ='prod'
menu="PruebaConcepto3/Reporte"
acces_token = getenv(env,'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
universe_id: str = getenv(env,'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx')
business_id: str = getenv(env, 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx')
shimoku = Shimoku.Client(
	    config={'access_token':acces_token},
	    universe_id = universe_id,
	    environment = 'production',
	)
shimoku.plt.set_business(business_id)
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
	shimoku.plt.html(
	    html=cont,
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
def GraficaLinea(menu,orden):
	report: Dict = shimoku.plt.line(
			df, x='hora',y=['instalado','registrados'],
			menu_path=menu,
			order=orden,
		)
def GraficaPastel(df,menu,orden,fil,col,titulo,pading,nom1,val1,nom2,val2):
	data_=[
		{'name':nom1,'value':val1},
		{'name':nom2,'value':val2},
	]
	shimoku.plt.pie(
			data=data_,
			x='name',y='value',
			menu_path=menu,
			order=orden,
			rows_size=fil,
			cols_size=col,
			title=titulo,
			padding=pading,
		)

def principal ():
	shimoku.plt.delete_path(menu_path=menu)
	DescripHtml('<div style="width:100%; height:90px; backgroud-color: rgb(185,205,225); border:1px solid gray; border-radius: 1em;"><h1>Usando indicadores en Shimoku</h1><hr><p>Los indicadores muestran los máximos y mínimos, de los paquetes instalados o registrados en un día</p></div>',0,menu,1,12)	
	Indicadores(menu,1,df)
	DescripHtml('<div style="width:100%; height:90px; backgroud-color: rgb(185,205,225); border:1px solid gray; border-radius: 1em;"><h1>Uso de Gráficas de barras en Shimoku</h1><hr><p>Mostrando los máximos y mínimos que se registraron e instalaron durante un día</p></div>',2,menu,1,12)
	GraficaBarras(menu,3,'Instalaciones y registros',df)
	DescripHtml('<p><b>Descripción: </b>Descripción para el html de la gráfica de barras.</p>',4,menu,3,12)	
	DescripHtml('<div style="width:100%; height:90px; backgroud-color: rgb(185,205,225); border:1px solid gray; border-radius: 1em;"><h1>Uso de Gráfica de lineas en Shimoku</h1><hr><p>Mostrando Mínimos y Máximos de un día</p></div>',5,menu,1,12)
	GraficaLinea(menu,6)
	DescripHtml('<p><b>Descripción:</b>Mostrando grafica de lineas de registrados e instalados</p>',7,menu,3,12)
	DescripHtml('<div style="width:100%; height:90px; backgroud-color: rgb(185,205,225); border:1px solid gray; border-radius: 1em;"><h1>Uso de gráfica de pastel en shimoku</h1><hr><p>Mostrando los mínimos y máximos de instalaciones y registros realizados en un día</p></div>',8,menu,1,12)
	GraficaPastel(df,menu,9,3,5,"Maximos y Minimos instalados",'0,0,0,0','Máx.Instalados ('+BuscaMaxMin('max','i',df)+')',BuscaMaxMin('max','i',df),'Min.Instalados ('+BuscaMaxMin('min','i',df)+')',BuscaMaxMin('min','i',df))
	GraficaPastel(df,menu,10,3,5,"Minimos y Maximos registrados",'0,0,0,0','Max.Registrados ('+BuscaMaxMin('max','r',df)+')',BuscaMaxMin('max','r',df),'Min.Registrados ('+BuscaMaxMin('min','r',df)+')',BuscaMaxMin('min','r',df))
	DescripHtml("<p><b>Descripción:</b> Gráfica de pastel Mostrando los mínimos y máximos por instalados y registrados</p>",11,menu,2,12)
	DescripHtml('<div style="width:100%; height:90px; backgroud-color: rgb(185,205,225); border:1px solid gray; border-radius: 1em;"><h1>Para más información</h1><hr><p>Sobre el código usado y los reportes generadados pulsa en el botón al calce</p></div>',12,menu,1,12)
	DescripHtml('<button type="button" onclick="javascript:void(window.open(\' https://ajgutierrez.com.mx/2022/07/05/shimoku-prueba-de-concepto/ \'))">Explicación en mi sitio web</button>',13,menu,2,4)
	DescripHtml('<button type="button" onclick="javascript:void(window.open(\' https://github.com/ajgutierr3z/shimoku \'))">Códigos utilizados en el github</button>',14,menu,2,4)
	print ("Webapp creada")
#inicia = t.time()
principal ()
#duracion = t.time() - inicia 
#print("duracion de la creacion del reporte: %.10f segundos.  "%duracion)
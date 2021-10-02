<h1 align="center">
    TopiTops
</h1>

## Introduction:
TopiTops es una api generada a travez del web scraping de las otts mas importantes a nivel global.

## Desarollo:
   Mediante nuestro "main.py" instanciamos cada una de las plataformas, al ejecutarlas el retorna un JSON el cual es cargado en el servidor local o server por medio de MongoDB.
   Por medio del método 'GET', realizamos las peticiones APIrest al MongoDB, la API por medio de la libreria FLASK. 
   **Endpoint: "/api/all_top"

## Pasos para iniciar el proyecto:
- Iniciamos un entorno virtual ["virtualenv venv"]
- Instalamos las librerias     ["pip install -r requierments.txt"]
- Iniciamos el scraping        ["python main.py"]

## BETA 1.0
Al dia de hoy la version Beta1.0 de TopiTops genera:
- Top 10 OverAll
- Top 10 Peliculas
- Top 10 Series
- Top 10 Kids

De las siguientes plataformas:	
- DisneyPlus
- StarPlus

## Escalabilidad / Proyecto final:
Presentando la Beta, el proyecto real el cual vemos una gran escalabilidad. 
Es una api que por medio de peticiones en el servidor a la vpn express itere el scrapping del main para diferentes paises, tanto de Latam como del resto del mundo.

## TO DO:
* [X]  NETFLIX
* [ ]  HBO MAX
* [ ]  VALIDAR SSH - VPN EXPRESS
* [ ]  SCRAPING LATAM, US , GLOBAL
* [ ]  CONSUMIRLO EN FRONT-END
* [ ]  SUBIDAS Y BAJADAS de posicion.

# Scraper Sistema Nacional de Informacion e Integracion de Mercados

Scrapper de precios de central de abastos

## Datos
Fuente: [Sistema Nacional de Informacion e Integracion de Mercados](http://www.economia-sniim.gob.mx/)

Secciones:
- Mercados Agricolas
    - Frutas y Hortalizas
    - Flores
    - Granos basicos
    - Azucar
    - Aceites comestibles
- Mercados Pecuarios
    - Bovinos: Empacadoras y distribuidoras
    - Aves: Pollo por partes (Empacadoras y distribuidoras)

## Esquema Final
### Agricultura
Mongo collection: agricultura
Esquema: 
´´´
{
    "fecha": "mm/dd/yyyy",
    "presentacion": "string",
    "origen": "string",
    "destino": "string",
    "precio_min": "string",
    "precio_max": "string",
    "precio_frec": "string",
    "obs": "string"
}
´´´


## Requerimientos
- [Python 3.5+] (https://www.python.org/)
- [Doccker] (https://www.docker.com/)
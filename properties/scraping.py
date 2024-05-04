from lxml import etree
import requests
from io import StringIO
import re
from properties.models import Property


response = requests.get("https://mexico.inmobiliarie.com/inmuebles-en-venta-y-renta/terreno-en-lomas-del-centinela-cerca-de-universidades/")
parser = etree.HTMLParser()
tree = etree.parse(StringIO(str(response.content)),parser)

#busquedas generales
description = tree.xpath('//div[@class="directorist-listing-details__text"]//span/text()')[3]
ubicacion = tree.xpath('//a[@target="google_map"]/text()')[0]
precio = tree.xpath('//div[@class="directorist-info-item directorist-pricing-meta directorist-info-item-price"]//span/text()')
tipo = tree.xpath('//span/a/text()')[6]
alto = tree.xpath('//div[@class="directorist-single-info__value"]/text()')[1]
ancho = tree.xpath('//div[@class="directorist-single-info__value"]/text()')[1]

#para la búsqueda exacta de los datos
calle = re.search('Roble', ubicacion)
colonia = re.search('Lomas del Centinela', ubicacion)
ciudad = re.search('Jalisco', ubicacion)
postal = re.search('45204', ubicacion)


#impresiones de los datos
print(f'descripcion:{description}') 

if calle and colonia and ciudad and postal:
    print(f'calle: {calle.group()}')
    print(f'colonia: {colonia.group()}')
    print(f'colonia: {ciudad.group()}')
    print(f'codigo postal: {postal.group()}')

print(f'precio:{precio}') 


#guardamos en la base de datos
propiedad = Property()

# Asignar los datos a los campos correspondientes
propiedad.description = description
propiedad.street = calle.group() if calle else None
propiedad.colony = colonia.group() if colonia else None
propiedad.city = ciudad.group() if ciudad else None
propiedad.postal_code = postal.group() if postal else None
propiedad.price = float(precio[0]) if precio else None
propiedad.type = tipo
propiedad.wide = float(ancho)
propiedad.long = float(alto)

# Guardar la instancia en la base de datos
propiedad.save()
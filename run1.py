import csv

file = open(f"index.html", 'w')

codigoIndex = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Index</title>
    </head>
    <body>
        <h1>Indice</h1>
        <h2>Listado de Instituciones Educativas</h2>
        <hr>
    """
file.write(codigoIndex)

with open('ejercicio/data/Listado-Instituciones-Educativas-distribuidas-por-zona-distrito-y-circuito.csv', newline='') as File:  
    reader = csv.DictReader(File, delimiter='|')
    for row in reader:
        ruta = f"<a href='ejercicio/archivos-html/{row['Código AMIE']}.html'>{row['Nombre de la Institución Educativa']}</a><br>"

        file.write(ruta)


codigoFinal = """
    </body>
    </html>
"""

file.write(codigoFinal)
file.close()
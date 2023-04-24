import csv

with open('ejercicio/data/Listado-Instituciones-Educativas-distribuidas-por-zona-distrito-y-circuito.csv', newline='') as File:  
    reader = csv.DictReader(File, delimiter='|')
    for row in reader:
        file = open(f"ejercicio/archivos-html/{row['Código AMIE']}.html", 'w')

        codigo = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title></title>
        </head>
        <body>
            <h1>Nombre de Institución</h1>
            <h2>{row['Nombre de la Institución Educativa']}</h2>
            <hr>
            <h3>Datos relevantes</h3>
            <hr>
            <p><b>Provincia:</b> {row['Provincia']}</p>
            <p><b>Canton:</b> {row['Cantón']}</p>
            <p><b>Parroquia:</b> {row['Parroquia']}</p>
            <hr>
            <p>Autor fxgonzalez5</p>
        </body>
        </html>
        """

        file.write(codigo)
        file.close()

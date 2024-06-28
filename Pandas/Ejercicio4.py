# Escribir programa que genere y muestre por pantalla un DataFrame con los datos de la tabla siguiente:

# Mes	    Ventas	Gastos
# Enero 	30500	22000
# Febrero	35600	23400
# Marzo	    28300	18100
# Abril	    33900	20700

import pandas as pd

datos = [['Enero', 30500, 22000], ['Febrero', 35600, 23400], ['Marzo', 28300, 18100], ['Abril', 33900,20700]]
contabilidad = pd.DataFrame(datos, columns=['Mes', 'Ventas', 'Gastos'])

print(contabilidad)
import tkinter as tk
from tkinter import messagebox
import pandas as pd
from datetime import datetime

# Clase para representar una tarjeta de crédito
class TarjetaCredito:
    def __init__(self, nombre, fecha_corte, fecha_pago, saldo_actual, pago_minimo):
        self.nombre = nombre
        self.fecha_corte = datetime.strptime(fecha_corte, "%d/%m")
        self.fecha_pago = datetime.strptime(fecha_pago, "%d/%m")
        self.saldo_actual = saldo_actual
        self.pago_minimo = pago_minimo

# Función para organizar los pagos
def organizar_pagos(tarjetas, ingreso_mensual):
    datos = []
    total_pag_minimos = sum(tarjeta.pago_minimo for tarjeta in tarjetas)
    saldo_disponible = ingreso_mensual - total_pag_minimos

    for tarjeta in tarjetas:
        datos.append({
            'Tarjeta': tarjeta.nombre,
            'Pago mínimo': tarjeta.pago_minimo,
            'Saldo actual': tarjeta.saldo_actual
        })

        if saldo_disponible > 0:
            pago_adicional = min(saldo_disponible, tarjeta.saldo_actual)
            tarjeta.saldo_actual -= pago_adicional
            saldo_disponible -= pago_adicional
            datos[-1]['Pago adicional'] = pago_adicional

    df = pd.DataFrame(datos)
    df['Pago total'] = df['Pago mínimo'] + df.get('Pago adicional', 0)
    return df

# Función para recoger la información de la GUI y organizar los pagos
def calcular_pagos():
    tarjetas = []
    
    try:
        # Recoger información de las tarjetas
        for i in range(len(names)):
            nombre = names[i].get()
            fecha_corte = fechas_corte[i].get()
            fecha_pago = fechas_pago[i].get()
            saldo_actual = float(saldos[i].get())
            pago_minimo = float(pagos_minimos[i].get())
            tarjeta = TarjetaCredito(nombre, fecha_corte, fecha_pago, saldo_actual, pago_minimo)
            tarjetas.append(tarjeta)
        
        ingreso_mensual = float(ingreso_entry.get())

        # Calcular pagos organizados
        pagos_df = organizar_pagos(tarjetas, ingreso_mensual)

        # Mostrar resultados
        resultados = pagos_df.to_string(index=False)
        messagebox.showinfo("Resultados", resultados)
        
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores válidos.")

# Inicializar la aplicación
app = tk.Tk()
app.title("Organizador de Pagos de Tarjetas de Crédito")

# Crear entradas para tres tarjetas de crédito
names = []
fechas_corte = []
fechas_pago = []
saldos = []
pagos_minimos = []

for i in range(3):
    tk.Label(app, text=f"Tarjeta {i+1} Nombre:").grid(row=i, column=0)
    name_entry = tk.Entry(app)
    name_entry.grid(row=i, column=1)
    names.append(name_entry)

    tk.Label(app, text=f"Fecha Corte (dd/mm):").grid(row=i, column=2)
    fecha_corte_entry = tk.Entry(app)
    fecha_corte_entry.grid(row=i, column=3)
    fechas_corte.append(fecha_corte_entry)

    tk.Label(app, text=f"Fecha Pago (dd/mm):").grid(row=i, column=4)
    fecha_pago_entry = tk.Entry(app)
    fecha_pago_entry.grid(row=i, column=5)
    fechas_pago.append(fecha_pago_entry)

    tk.Label(app, text="Saldo Actual:").grid(row=i, column=6)
    saldo_entry = tk.Entry(app)
    saldo_entry.grid(row=i, column=7)
    saldos.append(saldo_entry)

    tk.Label(app, text="Pago Mínimo:").grid(row=i, column=8)
    pago_minimo_entry = tk.Entry(app)
    pago_minimo_entry.grid(row=i, column=9)
    pagos_minimos.append(pago_minimo_entry)

# Ingreso mensual
tk.Label(app, text="Ingreso Mensual:").grid(row=3, column=0)
ingreso_entry = tk.Entry(app)
ingreso_entry.grid(row=3, column=1)

# Botón para calcular
calcular_button = tk.Button(app, text="Calcular Pagos", command=calcular_pagos)
calcular_button.grid(row=4, columnspan=10)

# Ejecutar la aplicación
app.mainloop()

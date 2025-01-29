import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import datetime
import calendar
from collections import defaultdict

class CreditCard:
    """
    Clase para modelar una tarjeta de crédito con su fecha de corte y pago.
    
    Atributos:
        name (str): Nombre de la tarjeta.
        statement_day (int): Día del mes para la fecha de corte.
        payment_day (int): Día del mes para la fecha de pago.
        expenses (list): Lista de gastos con fecha y monto.
    """
    def __init__(self, name, statement_day, payment_day):
        self.name = name
        self.statement_day = statement_day
        self.payment_day = payment_day
        self.expenses = []  # Formato: (fecha_gasto, monto, fecha_pago)

    def add_expense(self, amount, expense_date):
        """
        Agrega un gasto y calcula automáticamente su fecha de pago.
        """
        statement_date = self._calculate_statement_date(expense_date)
        payment_date = self._calculate_payment_date(statement_date)
        self.expenses.append((expense_date, amount, payment_date))

    def _calculate_statement_date(self, expense_date):
        year = expense_date.year
        month = expense_date.month
        
        last_day_current = calendar.monthrange(year, month)[1]
        adjusted_day_current = min(self.statement_day, last_day_current)
        current_statement = datetime.date(year, month, adjusted_day_current)
        
        if expense_date <= current_statement:
            return current_statement
        else:
            month = (month % 12) + 1
            year = year if month != 1 else year + 1
            last_day_next = calendar.monthrange(year, month)[1]
            adjusted_day_next = min(self.statement_day, last_day_next)
            return datetime.date(year, month, adjusted_day_next)

    def _calculate_payment_date(self, statement_date):
        if self.payment_day > statement_date.day:
            last_day = calendar.monthrange(statement_date.year, statement_date.month)[1]
            adjusted_day = min(self.payment_day, last_day)
            return datetime.date(statement_date.year, statement_date.month, adjusted_day)
        else:
            month = (statement_date.month % 12) + 1
            year = statement_date.year if month != 1 else statement_date.year + 1
            last_day = calendar.monthrange(year, month)[1]
            adjusted_day = min(self.payment_day, last_day)
            return datetime.date(year, month, adjusted_day)

class PaymentOrganizer:
    """
    Organiza múltiples tarjetas y genera un calendario de pagos detallado por tarjeta.
    """
    def __init__(self):
        self.cards = {}
    
    def add_card(self, card):
        self.cards[card.name] = card
    
    def generate_payment_schedule(self):
        """
        Genera un reporte de pagos con tarjetas y montos por fecha.
        
        Returns:
            dict: {fecha_pago: {"tarjetas": {nombre: monto}, "total": suma}}
        """
        payment_schedule = defaultdict(lambda: {"tarjetas": defaultdict(float), "total": 0.0})
        for card in self.cards.values():
            for _, amount, payment_date in card.expenses:
                payment_schedule[payment_date]["tarjetas"][card.name] += amount
                payment_schedule[payment_date]["total"] += amount
        return dict(sorted(payment_schedule.items()))

class CreditCardApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Organizador de Tarjetas de Crédito")
        self.geometry("800x600")
        self.organizer = PaymentOrganizer()
        self._create_widgets()

    def _create_widgets(self):
        # Panel de entrada de datos
        input_frame = ttk.LabelFrame(self, text="Agregar Datos")
        input_frame.pack(pady=10, padx=10, fill="x")

        # Agregar Tarjeta
        ttk.Label(input_frame, text="Nombre Tarjeta:").grid(row=0, column=0, padx=5)
        self.card_name = ttk.Entry(input_frame)
        self.card_name.grid(row=0, column=1, padx=5)

        ttk.Label(input_frame, text="Día Corte:").grid(row=0, column=2, padx=5)
        self.statement_day = ttk.Entry(input_frame, width=5)
        self.statement_day.grid(row=0, column=3, padx=5)

        ttk.Label(input_frame, text="Día Pago:").grid(row=0, column=4, padx=5)
        self.payment_day = ttk.Entry(input_frame, width=5)
        self.payment_day.grid(row=0, column=5, padx=5)

        ttk.Button(input_frame, text="Agregar Tarjeta", command=self._add_card).grid(row=0, column=6, padx=10)

        # Agregar Gasto
        ttk.Label(input_frame, text="Monto:").grid(row=1, column=0, pady=10)
        self.amount = ttk.Entry(input_frame)
        self.amount.grid(row=1, column=1)

        ttk.Label(input_frame, text="Fecha (YYYY-MM-DD):").grid(row=1, column=2)
        self.expense_date = ttk.Entry(input_frame)
        self.expense_date.grid(row=1, column=3)

        self.card_combobox = ttk.Combobox(input_frame, state="readonly")
        self.card_combobox.grid(row=1, column=4)
        ttk.Button(input_frame, text="Agregar Gasto", command=self._add_expense).grid(row=1, column=5, padx=10)

        # Tabla de Resultados
        self.tree = ttk.Treeview(self, columns=("Fecha", "Tarjeta", "Monto"), show="headings")
        self.tree.heading("Fecha", text="Fecha de Pago")
        self.tree.heading("Tarjeta", text="Tarjeta")
        self.tree.heading("Monto", text="Monto")
        self.tree.pack(pady=10, padx=10, fill="both", expand=True)

        # Botón Generar Reporte
        ttk.Button(self, text="Generar Calendario", command=self._update_schedule).pack(pady=5)

    def _add_card(self):
        name = self.card_name.get()
        try:
            statement = int(self.statement_day.get())
            payment = int(self.payment_day.get())
            new_card = CreditCard(name, statement, payment)
            self.organizer.add_card(new_card)
            self.card_combobox["values"] = list(self.organizer.cards.keys())
            messagebox.showinfo("Éxito", f"Tarjeta {name} agregada!")
        except ValueError:
            messagebox.showerror("Error", "Días deben ser números enteros")

    def _add_expense(self):
        card_name = self.card_combobox.get()
        amount = self.amount.get()
        date_str = self.expense_date.get()

        try:
            amount = float(amount)
            year, month, day = map(int, date_str.split("-"))
            date = datetime.date(year, month, day)
            card = self.organizer.cards[card_name]
            card.add_expense(amount, date)
            messagebox.showinfo("Éxito", "Gasto agregado!")
        except (ValueError, KeyError):
            messagebox.showerror("Error", "Datos inválidos o tarjeta no seleccionada")

    def _update_schedule(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        schedule = self.organizer.generate_payment_schedule()
        for fecha, detalles in schedule.items():
            for tarjeta, monto in detalles["tarjetas"].items():
                self.tree.insert("", "end", values=(
                    fecha.strftime("%d/%m/%Y"),
                    tarjeta,
                    f"${monto:.2f}"
                ))

# --------------------------------------------
# Ejecutar la Aplicación
# --------------------------------------------
if __name__ == "__main__":
    app = CreditCardApp()
    app.mainloop()
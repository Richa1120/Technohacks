import tkinter as tk
from tkinter import ttk
import requests

class CurrencyConverter:
    def __init__(self, master):
        self.master = master
        self.master.title("Currency Converter")

        # Fetch latest exchange rates
        self.latest_rates = self.fetch_latest_rates()

        #Fetch all currencies
        self.currencies=self.fetch_currencies()

        # Initialize GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Currency labels and entry fields
        tk.Label(self.master, text="Amount:").grid(row=0, column=0, padx=5, pady=5)
        self.amount_entry = tk.Entry(self.master)
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.master, text="From:").grid(row=1, column=0, padx=5, pady=5)
        self.from_currency_combo = ttk.Combobox(self.master, values=self.currencies)
        self.from_currency_combo.grid(row=1, column=1, padx=5, pady=5)
        self.from_currency_combo.set("USD")

        tk.Label(self.master, text="To:").grid(row=2, column=0, padx=5, pady=5)
        self.to_currency_combo = ttk.Combobox(self.master, values=self.currencies)
        self.to_currency_combo.grid(row=2, column=1, padx=5, pady=5)
        self.to_currency_combo.set("EUR")

        # Convert button
        self.convert_button = tk.Button(self.master, text="Convert", command=self.convert)
        self.convert_button.grid(row=3, columnspan=2, padx=5, pady=5)

        # Result label
        self.result_label = tk.Label(self.master, text="")
        self.result_label.grid(row=4, columnspan=2, padx=5, pady=5)

    def fetch_latest_rates(self):
        response = requests.get("https://v6.exchangerate-api.com/v6/5e8ff166e06b6a76b7d1238e/latest/USD")
        data = response.json()
        return data["conversion_rates"]

    def fetch_currencies(self):
        response = requests.get("https://v6.exchangerate-api.com/v6/5e8ff166e06b6a76b7d1238e/latest/USD")
        data = response.json()
        return list(data["conversion_rates"].keys())

    def convert(self):
        try:
            amount = float(self.amount_entry.get())
            from_currency = self.from_currency_combo.get()
            to_currency = self.to_currency_combo.get()

            if from_currency == to_currency:
                result = amount
            else:
                from_rate = self.latest_rates[from_currency]
                to_rate = self.latest_rates[to_currency]
                result = amount * (to_rate / from_rate)

            self.result_label.config(text=f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")
        except Exception as e:
            self.result_label.config(text="Error: " + str(e))

def main():
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()

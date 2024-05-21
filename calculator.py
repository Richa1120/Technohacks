import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        # Initialize the display
        self.display_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Display
        self.display = tk.Entry(self.master, textvariable=self.display_var, font=("Arial", 15), bd=10, insertwidth=2, width=15, borderwidth=4)
        self.display.grid(row=0, column=0, rowspan=2, columnspan=3)

        # Clear button
        tk.Button(self.master, text="C", padx=10, pady=10, font=("Arial", 15), command=self.clear_display).grid(row=0, column=3)
        
        #Delete button
        tk.Button(self.master, text="DEL", padx=10, pady=10, font=("Arial",15),command=self.delete).grid(row=1,column=3)

        # Buttons
        buttons = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '.', '0', '=', '+']
        row_val = 2
        col_val = 0

        for button in buttons:
            tk.Button(self.master, text=button, padx=20, pady=20, font=("Arial", 15), command=lambda button=button: self.on_button_click(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1


    def on_button_click(self, char):
        current_text = self.display_var.get()
        if char == '=':
            try:
                result = str(eval(current_text))
                self.display_var.set(result)
            except Exception as e:
                self.display_var.set("Error")
        else:
            new_text = current_text + str(char)
            self.display_var.set(new_text)

    def clear_display(self):
        self.display_var.set("")

    def delete(self):
        current_text=self.display_var.get()
        self.display_var.set(current_text[:-1])

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

# import modules
import json as json
import requests as requests
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class RealTimeCurrencyConverter():
    def __init__(self, url):
            self.data = requests.get(url).json()
            self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount): 
        initial_amount = amount 
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency] 
  
        # limiting the precision to 4 decimal places 
        amount = round(amount * self.currencies[to_currency], 4) 
        return amount
    

class App(tk.Tk):

    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title = ('Currency Converter')
        self.currency_converter = converter

        self.geometry("800x800")
        

                # create tabs
        my_notebook = ttk.Notebook(self)
        my_notebook.pack(pady=5)   #padding

        # create frames
        currency_frame = Frame(my_notebook, width=780, height=780)
        crypto_frame = Frame(my_notebook, width=780, height=780)

        currency_frame.pack(fill="both",expand=1 )
        crypto_frame.pack(fill="both",expand=1 )

        # add tabs
        my_notebook.add(currency_frame,text='currencies')
        my_notebook.add(crypto_frame,text='cryptocurrency')

        self.intro_label = Label(currency_frame, text = 'Real Time Currency Convertor App',  fg = 'blue', relief = tk.RAISED, justify = tk.CENTER, borderwidth = 3)
        self.intro_label.config(font = ('Manrope',20,'bold'))
        self.intro_label.place(x = 60, y = 20)


        # date label
        self.date_label = Label(currency_frame, text = f"1 Kenyan Shilling = {self.currency_converter.convert('KES','USD',1)} USD \n Date : {self.currency_converter.data['date']}", relief = tk.GROOVE, borderwidth = 5)
        self.date_label.place(x = 300, y= 80)

        # amount label
        self.amount_label = Label(currency_frame, text = 'Amount to convert:',font=('aerial',25,'bold','underline'),fg='dark red')
        self.amount_label.place(x = 150, y = 150)
        
         # amount entry 
        valid = (self.register(self.restrictNumberOnly), '%d', '%P')
        self.amount_field = Entry(self,font=('aerial',24),validate='key', validatecommand=valid)
        self.amount_field.place(x = 150, y = 230)

    
        # from_currency label
        self.from_currency_label = Label(currency_frame, text = 'Convert from:',font=('aerial',25,'bold','underline'),fg='dark red')
        self.from_currency_label.place(x = 30, y = 280) 

        # dropdown
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("KES") # default value
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("USD") # default value 

        # from_currency dropdown
        font = ("aerial", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable, values=list(self.currency_converter.currencies.keys()), font= font, state = 'readonly', width = 30,height=15, justify = tk.CENTER)
        self.from_currency_dropdown.place(x = 320, y= 320)
        
        # to_currency label
        self.to_currency_label = Label(currency_frame, text = 'Convert to:',font=('aerial',25,'bold','underline'),fg='dark red')
        self.to_currency_label.place(x = 30, y = 400) 

        # drop down
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable, values=list(self.currency_converter.currencies.keys()), font= font, state = 'readonly', width = 30,height=15, justify = tk.CENTER)
        self.to_currency_dropdown.place(x = 320, y= 435)

        # results label
        self.results_label = Label(currency_frame, text = 'Results:',font=('aerial',25,'bold','underline'),fg='dark red')
        self.results_label.place(x = 150, y = 480)

        # converted field
        self.converted_amount_field_label = Label(self, text = '', font=('aerial',24),fg = 'black', bg = 'white', relief = tk.RIDGE, justify = tk.CENTER, width = 15, borderwidth = 3)
        self.converted_amount_field_label.place(x = 325, y = 505)

         # Convert button
        self.convert_button = Button(self, text = "Convert", fg = "black", command = self.perform) 
        self.convert_button.config(font=('Manrope', 12, 'bold'),bg='blue',width=20)
        self.convert_button.place(x = 150, y = 600)

        #clear button

        # clear button
        self.clear_button = Button(self,text='Clear',command=self.clear)
        self.clear_button.config(font=('Manrope', 12, 'bold'),bg='red',width=20)
        self.clear_button.place(x= 500,y=600)


    def clear(self):
        self.amount_field.delete(0, END)
        self.converted_amount_field_label['text'] = ''
        
        

    def perform(self):
        if not self.amount_field.get():
            messagebox.showwarning('WARNING','You did not fill the amount to convert')
        else:
            amount = float(self.amount_field.get())
            from_curr = self.from_currency_variable.get()
            to_curr = self.to_currency_variable.get()

            converted_amount = self.currency_converter.convert(from_curr,to_curr,amount)
            converted_amount = round(converted_amount, 4)

            self.converted_amount_field_label.config(text = str(converted_amount))


    def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return string=="" or (string.count('.')<=1 and result is not None)    
        

      
if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeCurrencyConverter(url)
    App(converter)
    mainloop()





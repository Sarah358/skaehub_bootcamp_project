# import modules
import json as json
import requests as requests
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

from requests.api import request

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
class BitcoinConverter():
    def __init__(self, url2):
            self.response = requests.get(url2).json()
            self.kenya = self.response['KES']
            self.price = "{:,}".format(self.kenya)
            self.usd = self.response['USD']
            self.price2 = "{:,}".format(self.usd)
            self.time = datetime.now().strftime("%H:%M:%S")
   


    
             
class App(tk.Tk):

    def __init__(self, converter,bitcoin):
        tk.Tk.__init__(self)
        self.title = ('Currency Converter')
        self.currency_converter = converter
        self.bitcoin = bitcoin
        self.geometry("800x800")
        

                # create tabs
        my_notebook = ttk.Notebook(self)
        my_notebook.pack(pady=5)   #padding

        # create frames
        currency_frame = Frame(my_notebook, width=780, height=780)
        bitcoin_frame = Frame(my_notebook, width=780, height=780)

        currency_frame.pack(fill="both",expand=1 )
        bitcoin_frame.pack(fill="both",expand=1 )

        # add tabs
        my_notebook.add(currency_frame,text='currencies')
        my_notebook.add(bitcoin_frame,text='bitcoin')

        #################################
        #### Currency frame
        ##################################

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
        self.amount_field = Entry(currency_frame,font=('aerial',24),validate='key', validatecommand=valid)
        self.amount_field.place(x = 150, y = 200)

    
        # from_currency label
        self.from_currency_label = Label(currency_frame, text = 'Convert from:',font=('aerial',25,'bold','underline'),fg='dark red')
        self.from_currency_label.place(x = 30, y = 250) 

        # dropdown
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("KES") # default value
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("USD") # default value 

        # from_currency dropdown
        font = ("aerial", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(currency_frame, textvariable=self.from_currency_variable, values=list(self.currency_converter.currencies.keys()), font= font, state = 'readonly', width = 30,height=15, justify = tk.CENTER)
        self.from_currency_dropdown.place(x = 320, y= 270)
        
        # to_currency label
        self.to_currency_label = Label(currency_frame, text = 'Convert to:',font=('aerial',25,'bold','underline'),fg='dark red')
        self.to_currency_label.place(x = 30, y = 350) 

        # drop down
        self.to_currency_dropdown = ttk.Combobox(currency_frame, textvariable=self.to_currency_variable, values=list(self.currency_converter.currencies.keys()), font= font, state = 'readonly', width = 30,height=15, justify = tk.CENTER)
        self.to_currency_dropdown.place(x = 320, y= 360)

        # results label
        self.results_label = Label(currency_frame, text = 'Results:',font=('aerial',25,'bold','underline'),fg='dark red')
        self.results_label.place(x = 150, y = 480)

        # converted field
        self.converted_amount_field_label = Label(currency_frame, text = '', font=('aerial',24),fg = 'black', bg = 'white', relief = tk.RIDGE, justify = tk.CENTER, width = 15, borderwidth = 3)
        self.converted_amount_field_label.place(x = 325, y = 480)

         # Convert button
        self.convert_button = Button(currency_frame, text = "Convert", fg = "black", command = self.perform) 
        self.convert_button.config(font=('Manrope', 12, 'bold'),bg='blue',width=20)
        self.convert_button.place(x = 150, y = 600)

        #clear button

        # clear button
        self.clear_button = Button(currency_frame,text='Clear',command=self.clear)
        self.clear_button.config(font=('Manrope', 12, 'bold'),bg='red',width=20)
        self.clear_button.place(x= 500,y=600)

        #########################################################################################################
        ##########bitcoin frame
        self.intro_label = Label(bitcoin_frame, text = 'Bitcoin Price Tracker',  fg = 'blue', relief = tk.RAISED, justify = tk.CENTER, borderwidth = 3)
        self.intro_label.config(font = ('Manrope',20,'bold'))
        self.intro_label.place(x = 100, y = 20)

        #  price text kenya
        self.LabelText = Label(bitcoin_frame, font=('Manrope', 22, 'bold'),text= 'BITCOIN PRICE IN KES :')
        self.LabelText.place(x=50,y = 125)

        # price label kenya
        self.LabelPrice = Label(bitcoin_frame, text =f"KSH  {self.bitcoin.price }", font=('aerial',24, 'bold'),fg = 'black', bg = 'white', relief = tk.RIDGE, justify = tk.CENTER, width = 20, borderwidth = 3)
        self.LabelPrice.place(x=150,y = 180)

         #  price text usd
        self.LabelTextUsd = Label(bitcoin_frame, font=('Manrope', 22, 'bold'),fg = 'red',text= 'BITCOIN PRICE IN USD :')
        self.LabelTextUsd.place(x=50,y = 260)

        # price label uds
        self.LabelPrice = Label(bitcoin_frame, text =f"$  {self.bitcoin.price2 }", font=('aerial',24, 'bold'),fg = 'dark red', bg = 'white', relief = tk.RIDGE, justify = tk.CENTER, width = 20, borderwidth = 3)
        self.LabelPrice.place(x=150,y = 320)

        #  last updated
        self.LabelTextUpdated = Label(bitcoin_frame, font=('Manrope', 22, 'bold'),fg = 'red',text= 'Last Updated:')
        self.LabelTextUpdated.place(x=180,y = 400)

        # last updated text
        self.LabelUpdated = Label(bitcoin_frame, text =f"  {self.bitcoin.time }", font=('aerial',24, 'bold'),fg = 'black')
        self.LabelUpdated.place(x=200,y = 450)

          

        

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
    url2 = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,KES,EUR'
    converter = RealTimeCurrencyConverter(url)
    bitcoin = BitcoinConverter(url2)
    App(converter,bitcoin)
    mainloop()
    


    
####################################
# cryptocurrency frame
###############################



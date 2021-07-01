# skaehub_bootcamp_project
# Real time currency conversion app/Bitcoin price tracker

## About the app

Real time currency conversion app fetches data of real time currency rates and helps in converting currencies from one currency to another. 

Bitcoin tracker app keeps track of current bitcoin prices and displays the results in ksh and us dollars.

## Api url's
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    url2 = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,KES,EUR'

## 1. Currency converter app.
### Get started
first install:

```
    pip install requests 
    pip install tkinter

```    
Tkinter will help us with ours GUI as follows

![Screenshot from 2021-07-01 13-51-14](https://user-images.githubusercontent.com/60597568/124117630-08e42700-da79-11eb-9d8b-b23d7313cd15.png)

## import modules

```
import json as json
import requests as requests
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

```

## Start coding

After importing our modules we are now ready to code.

### Create a class with two methods
WE first create our class and get data from api for conversion rates and conversion method to convert amount from one currency to another.

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


### Create another class for the gui
In the class we have to use the tkinter module and structure our gui.Here we just create a main method and include the title,dimensions and tabs. For my app i had two tabs,one for currency conversion and another one for bitcoin conversion.

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

### Create labels and entrys 
 In this section, create your labels and entry fields.(Check source code for my entry fields and labels).

 ### convert button
 The convert button contains a command that calls the convert function where all the conversions are performed as follows

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

### Clear button
The clear button calls the clear function which clears all data in the entry fields and a user can input new data as follows.

    def clear(self):
        self.amount_field.delete(0, END)
        self.converted_amount_field_label['text'] = ''
        
### Restricnumberonly function
THis functions allows a user to only enter numbers to be converted and not string values.So when a user tries to input a letter instaed of a number. Nothing happens to the entry field.

    def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return string=="" or (string.count('.')<=1 and result is not None)  

## Close the main loop 
 Lastly close the mainloop and your call the main function and with that you have a currency converter app with a gui interface.


 #  Bitcoin price Tracker app
THe next tab in our gui is bitcoin tab as shown below. 

![Screenshot from 2021-07-01 14-29-12](https://user-images.githubusercontent.com/60597568/124117489-e18d5a00-da78-11eb-924b-3b67bce3070a.png)


Nothing big happens here as you can see. We just get the latest price of bitcoins in usd and kes and display the results on our gui interface 

### Get started.

We are using same modules as the currency converter. Check them above. Next create a class to hold the bitcoin prices and add , to the values for readability as shown below

    class BitcoinConverter():
    def __init__(self, url2):
            self.response = requests.get(url2).json()
            self.kenya = self.response['KES']
            self.price = "{:,}".format(self.kenya)
            self.usd = self.response['USD']
            self.price2 = "{:,}".format(self.usd)
            self.time = datetime.now().strftime("%H:%M:%S")


Also get the current time to ensure the values displayed are realtime. 

### labels
Finally just create labels to display the results and you are done.

## Demo of the app functionality

![convert2](https://user-images.githubusercontent.com/60597568/124120802-da684b00-da7c-11eb-9b5d-577eae8dbc14.gif)


# conclusion
To get the full source code of the app, navigate to realtime_currency.py file.

To add to the project just pull a request and make sure to commit your changes.... 

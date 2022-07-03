import tkinter as tk
from tkinter import ttk
import numpy as np
import yahoofinancebot, datetime


window = tk.Tk()
window.title("Yahoo Trading Bot")
window.iconbitmap('icon/icon.ico')
window.configure(bg='white')

value = tk.StringVar()
days = tk.StringVar()
months = tk.StringVar()
years = tk.StringVar()

def study():
    sell.configure(background="white")
    buy.configure(background="white")
    Bot = yahoofinancebot.bot(symbol=value.get(),start_date= datetime.datetime( int(years.get()), int(months.get()) , int(days.get()) ))
    if int(Bot.prediction[value.get()]["buy"]) == 0 and int(Bot.prediction[value.get()]["sell"]) == 1 :
        sell.configure(background="red")
    if int(Bot.prediction[value.get()]["buy"]) == 1 and int(Bot.prediction[value.get()]["sell"]) == 0 :
        buy.configure(background="green")

label = tk.Label(window, text="Enter a value :", background="white", font=("Arial",12,"italic","bold"), width=20)
label2 = tk.Label(window, background="white", font=("Arial",12,"italic","bold"), width=2)
value = tk.Entry(window,textvariable=value, background="white", font=("Arial",12,"italic","bold"), width=40)
study = tk.Button(window,text="Predict", background="white", font=("Arial",12,"bold"), width=20, command=study)
buy = tk.Label(window,text="Buy" ,background="white",  foreground="white",font=("Arial",12,"italic","bold"), width=10)
sell = tk.Label(window,text="Sell" ,background="white",  foreground="white",font=("Arial",12,"italic","bold"), width=10)
copyrigth = tk.Label(window,text=" Copyrigth Global Analysis Sarl - contact : +22672587871", background="white", font=("Arial",8,"italic","bold"), width=50)

x = np.arange(1,32)
y = np.arange(1,13)
z = np.arange(2018,datetime.date.today().year+1)



stday = tk.Label(window, text="start day :", background="white", font=("Arial",8,"italic"))
day = ttk.Combobox(window,width=2,textvariable=days,values=x, state="readonly")
day.current(1)
stmonth = tk.Label(window, text="start month :", background="white", font=("Arial",8,"italic"))
month = ttk.Combobox(window,width=2,textvariable=months,values=y, state="readonly")
month.current(1)
styear = tk.Label(window, text="start year :", background="white", font=("Arial",8,"italic"))
year = ttk.Combobox(window,width=8,textvariable=years,values=z, state="readonly")
year.current(1)


label.grid(column=0,row=0)
value.grid(column=1,row=0)
stday.grid(column=2,row=0)
day.grid(column=3,row=0)
stmonth.grid(column=4,row=0)
month.grid(column=5,row=0)
styear.grid(column=6,row=0)
year.grid(column=7,row=0)
label2.grid(column=8,row=0)
study.grid(column=9,row=0)
buy.grid(column=0,row=2)
sell.grid(column=0,row=3)
copyrigth.grid(column=1,row=4)

window.mainloop()

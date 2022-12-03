from tkinter import *

root=Tk()
root.title("Sales Application")
root.geometry("700x400")
root.configure(bg="yellow")

months = ('January','February','March','April','May','June','July','August','September','October','November','December')
profits = (20000, 45000, 78000, 97000, 12000, 456000, 65000, 54000, 10000, 30000, 70000, 90000)

month_label = Label(root)
month_label.place(relx=0.5, rely=0.3, anchor=CENTER)
profit_label = Label(root)
profit_label.place(relx=0.5, rely=0.4, anchor=CENTER)
max_profit = Label(root)
min_profit = Label(root)

month_label["text"] = "Months : " + str(months)
profit_label["text"] = "Profit : " + str(profits)

def max_profits_function():
    max_profits = max(profits)
    max_profits_index = profits.index(max_profits)
    max_profits_month = months[max_profits_index]
    max_profit["text"] = "Maximum profits of " + str(max_profits) + " was given in the month of " + str(max_profits_month)

def min_profits_function():
    min_profits = min(profits)
    min_profits_index = profits.index(min_profits)
    min_profits_month = months[min_profits_index]
    min_profit["text"] = "Minimum profits of " + str(min_profits) + " was given in the month of " + str(min_profits_month)

btn = Button(root, text="Show Max Profitable Month", bg='blue', fg='white', command=max_profits_function)
btn.place(relx=0.5, rely=0.6, anchor=CENTER)

max_profit.place(relx=0.5, rely=0.7, anchor=CENTER)

btn1 = Button(root, text="Show Min Profitable Month", bg='blue', fg='white', command=min_profits_function)
btn1.place(relx=0.5, rely=0.6, anchor=CENTER)

min_profit.place(relx=0.5, rely=0.8, anchor=CENTER)

root.mainloop()

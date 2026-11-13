import tkinter as tk
root=tk.Tk()
root.title("CALCULATOR")
root.geometry("400x600")
root.configure(bg="black")
def click(num):
    pg=entry.get()
    entry.delete(0,tk.END)
    entry.insert(0,pg+ str(num))
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
def clear():
    entry.delete(0,tk.END)        



entry=tk.Entry(root,borderwidth=8,font=40)
entry.pack(fill="x",ipadx=10,pady=12,padx=12)

row1 = tk.Frame(root)
row1.pack(pady=10)

b=tk.Button(row1,text="9",bg="grey",font=30,padx=28,pady=22,command=lambda:click(9))
b.pack(side="left",padx=10,)
b=tk.Button(row1,text="8",bg="grey",font=30,padx=28,pady=22,command=lambda:click(8))
b.pack(side="left",padx=10)
b=tk.Button(row1,text="7",bg="grey",font=30,padx=28,pady=22,command=lambda:click(7))
b.pack(side="left",padx=10)
b=tk.Button(row1,text="/",bg="grey",font=30,padx=28,pady=22,command=lambda:click("/"))
b.pack(side="left",padx=10)


row2 = tk.Frame(root)
row2.pack(pady=10)

b=tk.Button(row2,text="6",bg="grey",font=30,padx=28,pady=22,command=lambda:click(6))
b.pack(side="left",padx=10)
b=tk.Button(row2,text="5",bg="grey",font=30,padx=28,pady=22,command=lambda:click(5))
b.pack(side="left",padx=10)
b=tk.Button(row2,text="4",bg="grey",font=30,padx=28,pady=22,command=lambda:click(4))
b.pack(side="left",padx=10)
b=tk.Button(row2,text="*",bg="grey",font=30,padx=28,pady=22,command=lambda:click("*"))
b.pack(side="left",padx=10)

row3=tk.Frame(root)
row3.pack(pady=10)

b=tk.Button(row3,text="3",bg="grey",font=30,padx=28,pady=22,command=lambda:click(3))
b.pack(side="left",padx=10)
b=tk.Button(row3,text="2",bg="grey",font=30,padx=28,pady=22,command=lambda:click(2))
b.pack(side="left",padx=10)
b=tk.Button(row3,text="1",bg="grey",font=30,padx=28,pady=22,command=lambda:click(1))
b.pack(side="left",padx=10)
b=tk.Button(row3,text="-",bg="grey",font=30,padx=28,pady=22,command=lambda:click("-"))
b.pack(side="left",padx=10)


row4=tk.Frame(root)
row4.pack(pady=10)

b=tk.Button(row4,text=0,bg="grey",font=30,width=10,padx=28,pady=22,command=lambda:click(0))
b.pack(side="left",padx=10)

b=tk.Button(row4,text="C",bg="grey",font=30,padx=28,pady=22,command=clear)
b.pack(side="left",padx=10)

b=tk.Button(row4,text="+",bg="grey",font=30,padx=28,pady=22,command=lambda:click("+"))
b.pack(side="left",padx=10)

row5=tk.Frame(root)
row5.pack(pady=10)

b=tk.Button(row5,text="=",bg="grey",font=30,padx=28,pady=22,width=30,command=evaluate)
b.pack(side="left",padx=10)


root.mainloop()
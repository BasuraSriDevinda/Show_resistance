import tkinter as tk
from tkinter import ttk


from random import choice
from tkinter import PhotoImage
import  main,createdatabase
"""numberOfBand=0
def ok():
    global  numberOfBand
    numberOfBand = int(choice.get())

    print(numberOfBand)
    print(color.data)
    createdatabase

    main.destroy()
    pass"""

numberOfBand = 0
class MyWindow:

    def __init__(self,Selectcolour,number ):
        self.number=number
        self.Selectcolour = Selectcolour
        self.Selectcolour.title("Fixed Size Window")
        self.Selectcolour.geometry("400x550")
        self.Selectcolour.resizable(False, False)

        self.colorCodeResistance()
        self.MassageLable("********file the combobox relevant color**********")
        self.createWorking(number)
        self.butto("          ok          ")

    def colorCodeResistance(self):
        self.Selectcolour.configure(bg="lightblue")

    def MassageLable(self, message):
        label = tk.Label(
            self.Selectcolour,
            text=message.upper(),
            wraplength=250,
            justify ="left",
            bg="lightblue",
            font=("Arial", 12)
        )
        label.grid(row=0,rowspan=3,column=0,columnspan=3)

    def createWorking(self,number):
        Label1=[]
        comBox=[]
        def on_select(event):

            widget = event.widget.get()
            position = event.widget.winfo_y()
            for label  in Label1:
                if label.winfo_y()==position:
                    label.config(fg="white", bg=widget)
                    print(label)
            print(position,widget)



        pass

        for i in range(int(number)):

            NoBand=tk.Label(self.Selectcolour,text=str(i+1)+ " band".upper())
            NoBand.grid(row=i+5,column=1)
            Label1.append(NoBand)


            name = ttk.Combobox(self.Selectcolour, values=['Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet', 'Gray', 'White', 'Gold', 'Silver', 'No Color'])
            name.grid(row=i+5,column=2)
            name.kind= i
            comBox.append(name)
            name.bind("<<ComboboxSelected>>", on_select)

            pass
        pass
    def butto(self,name):
        self.Button=name
        self.Button=tk.Button(self.Selectcolour,text=name ,bg="red")
        self.Button.grid(row=10,column=3)

    pass

def colorChos():
    pass
def main():


    def ok():
        global numberOfBand
        numberOfBand = int(choice.get())

        #print(numberOfBand)
        #print(color.data)
        createdatabase

        main.destroy()
        pass
    main = tk.Tk()
    main.geometry("200x200")
    main.configure(bg="#3385ff")
    icon = PhotoImage(file="481597.png")
    main.iconphoto(True, icon)

    main.title("".upper())
    choice = tk.StringVar()

    choice.set("1")

    tk.Radiobutton(main, text="band 3".upper(), variable=choice, value="3", bg="#3399ff").pack()
    tk.Radiobutton(main, text="band 4".upper(), variable=choice, value="4", bg="#3399ff").pack()
    tk.Radiobutton(main, text="band 5".upper(), variable=choice, value="5", bg="#3399ff").pack()
    tk.Radiobutton(main, text="band 6".upper(), variable=choice, value="6", bg="#3399ff").pack()
    # show massage for chose  what kind of band are exiting resistance
    FirstMassage = tk.Label(main, text="chose  what kind of band are exiting resistance ".upper(), bg="#3385ff",fg="#ffffff", wraplength=150, justify="left").pack()
    SelectB = tk.Button(main, text="ok".upper(), bg="#ffffff", command=ok, width=50, height=5).pack()

    main.resizable(False, False)
    main.mainloop()
    # create root window show
    if int(choice.get()) >= 3:
        print("huthr")
        root = tk.Tk()
        app = MyWindow(root, str(numberOfBand))
        root.mainloop()
    pass


if __name__ == "__main__":
    main()
    #create main window  for chose the  riba of resistance

    """main=tk.Tk()
    main.geometry("200x200")
    main.configure(bg="#3385ff")
    icon = PhotoImage(file="481597.png")
    main.iconphoto(True, icon)

    main.title("".upper())
    choice = tk.StringVar()

    choice.set("1")

    tk.Radiobutton(main, text="band 3".upper(), variable=choice, value="3",bg="#3399ff").pack()
    tk.Radiobutton(main, text="band 4".upper(), variable=choice, value="4",bg="#3399ff").pack()
    tk.Radiobutton(main, text="band 5".upper(), variable=choice, value="5",bg="#3399ff").pack()
    tk.Radiobutton(main, text="band 6".upper(), variable=choice, value="6",bg="#3399ff").pack()
    # show massage for chose  what kind of band are exiting resistance
    FirstMassage =tk.Label(main,text="chose  what kind of band are exiting resistance ".upper(),bg="#3385ff",fg="#ffffff",wraplength=150,justify ="left").pack()
    SelectB=tk.Button(main,text="ok".upper(),bg="#ffffff",command=ok,width=50,height=5).pack()

    main.resizable(False,False)
    main.mainloop()
    # create root window show
    if int(choice.get())>=3:


        root = tk.Tk()
        app = MyWindow(root,str(numberOfBand))
        root.mainloop()
    #print(type(app))"""



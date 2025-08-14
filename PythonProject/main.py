import tkinter as tk
from tkinter import ttk


from random import choice
from tkinter import PhotoImage
import  calculation,createdatabase
import exel

numberOfBand = 0
##check the empty value
def checkEmpty(list):
    for i in list:
        if i == "":
            return False
    return True
def Back(wind):
    wind.destroy()
    main()
    #print(wind)
    pass

class MyWindow:

    def __init__(self,Selectcolour,number ):
        self.colourCode = []
        self.number=number
        self.Selectcolour = Selectcolour
        self.Selectcolour.title("Fixed Size Window")
        self.Selectcolour.geometry("400x400")
        self.Selectcolour.resizable(False, False)


        self.colorCodeResistance()
        self.MassageLable("********file the combobox relevant color**********",0,0,3,3,12)
        self.createWorking(number)
        self.butto("          ok          ", "oke",10,3,1)
        self.butto("          back          ", "back", 10, 5,self.Selectcolour)
        self.butto("          open          ", "open", 9, 5, 1)
    def outputMassage(self,number):
        if number==0:
            self.text=["Resistance :","Tolerance :","Temperature \ncoefficient"]
            self.minimunresitace=str(self.values[0]-self.values[1]) +" (Ω)"
            self.maximunresistace = str(self.values[0] + self.values[1]) +" (Ω)"
            print(self.minimunresitace,"           "  ,self.maximunresistace)
            self.MassageLable("MAX", 2, 3, 1, 1, 10)

            self.MassageLable(self.maximunresistace,2 , 5, 1, 1, 10)
            self.MassageLable("MIN", 3, 3, 1, 1, 10)

            self.MassageLable(self.minimunresitace, 3, 5, 1, 1, 10)

            #print(self.values)
            for i  in range(len(self.values)):
                if self.text[i] == "Resistance :":
                    self.values[i] = str(self.values[i]) + "(Ω)"
                if self.text[i] == "Tolerance :":
                    self.values[i] = str(self.values[i]) + "(Ω)"

                self.MassageLable(str(self.text[i]), i+12, 2, 1, 1,10)

                self.MassageLable(str(self.values[i]),i+12,3,1,1,10)
        pass

    def colorCodeResistance(self):
        self.Selectcolour.configure(bg="lightblue")

    def MassageLable(self, message,r,c,rs,cs,f):
        #print(message)



        label = tk.Label(
            self.Selectcolour,
            text=message.upper(),
            wraplength=250,
            justify ="left",
            bg="lightblue",
            font=("Arial", f)
        )
        label.grid(row=r,rowspan=rs,column=c,columnspan=cs)

    def createWorking(self,number):
        self.Label1=[]
        self.comBox=[]
        def on_select(event):

            widget = event.widget.get()
            position = event.widget.winfo_y()
            for label  in self.Label1:
                if label.winfo_y()==position:
                    label.config(fg="white", bg=widget)




        pass

        for i in range(int(number)):

            NoBand=tk.Label(self.Selectcolour,text=str(i+1)+ " band".upper())
            NoBand.grid(row=i+5,column=1)
            self.Label1.append(NoBand)


            name = ttk.Combobox(self.Selectcolour, values=['Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet', 'Gray', 'White', 'Gold', 'Silver', 'No Color'])
            name.grid(row=i+5,column=2)
            name.kind= i
            self.comBox.append(name)
            name.bind("<<ComboboxSelected>>", on_select)

            pass
        pass
    def butto(self,name,function,posR,poC,par):
        self.par=par
        functionValue={"oke": self.print1,"back":Back,"open":exel.exelOpen}
        self.Button=name
        self.r=posR
        self.c=poC
        self.Fun=function
        self.Button=tk.Button(self.Selectcolour,text=name ,bg="red",command=lambda:functionValue[function](par))
        self.Button.grid(row=self.r, column=self.c)

    def print1(self,par):
        self.x=par
        self.colourCode=[]
       # add chosing color code in the ordering Like 1 band and 2 band =[ "red","orange"]

        for i in self.comBox:
            self.colourCode.append(i.get())
#print(self.colourCode)


        if checkEmpty(self.colourCode)== True:



            if numberOfBand==3:
                self.values=calculation.Band3(self.colourCode)
                self.outputMassage(0)
            elif numberOfBand==4:
                self.values=calculation.Band4(self.colourCode)
                self.outputMassage(0)
                pass
            elif numberOfBand==5:
                self.values=calculation.Band5(self.colourCode)
                self.outputMassage(0)
                pass
            elif numberOfBand==6:
                self.values=calculation.Band6(self.colourCode)
                self.outputMassage(0)
                pass
            pass

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
        #print("huthr")
        root = tk.Tk()
        app = MyWindow(root, str(numberOfBand))
        root.mainloop()
    pass

if __name__ == "__main__":
    main()
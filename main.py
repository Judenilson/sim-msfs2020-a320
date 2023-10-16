from tkinter import *
from tkinter import ttk

class App:
    def __init__(self, master=None):
        self.defaultFont = ("Arial", "10")   
        self.h1 = ("verdana", 14, "italic", "bold")
        self.h2 = ("verdana", 12, "italic", "bold")
        self.h3 = ("verdana", 10, "bold")

        self.containerTakeoff = Frame(master, pady=10)
        self.containerTakeoff.pack(fill="x", padx=10)   
        self.containerExitButton = Frame(master, padx=20).pack()  
        self.containerLanding = Frame(master, padx=20).pack()

        # TAKEOFF
        self.Title = Label(self.containerTakeoff, text="TAKEOFF Performance", font=self.h1).pack()
        # SLOPE --------------------------
        self.slopeSection = LabelFrame(self.containerTakeoff, text="RWY Slope Calculator", font=self.h3)
        self.slopeSection.pack()

        self.slopeDepLabel = Label(self.slopeSection, text="THR elevation in use", font=self.defaultFont)
        self.slopeDepLabel.grid(row = 0, column = 0, sticky = W, pady = 2, padx= 10)
        self.slopeDep = Entry(self.slopeSection, width=10, font=self.defaultFont)
        self.slopeDep.grid(row = 0, column = 1, sticky = W, pady = 2, padx= 10)

        self.slopeArrLabel = Label(self.slopeSection, text="Opposit THR elevation", font=self.defaultFont)
        self.slopeArrLabel.grid(row = 1, column = 0, sticky = W, pady = 2, padx= 10)
        self.slopeArr = Entry(self.slopeSection, width=10, font=self.defaultFont)
        self.slopeArr.grid(row = 1, column = 1, sticky = W, pady = 2, padx= 10)

        self.rwyLengthLabel = Label(self.slopeSection, text="RWY Length in use", font=self.defaultFont)
        self.rwyLengthLabel.grid(row = 2, column = 0, sticky = W, pady = 2, padx= 10)
        self.rwyLength = Entry(self.slopeSection, width=10, font=self.defaultFont)
        self.rwyLength.grid(row = 2, column = 1, sticky = W, pady = 2, padx= 10)
    
        self.slopeButton = Button(self.slopeSection, text="Test", width=5, command=self.mudar_texto)
        self.slopeButton.grid(row = 3, column = 0, sticky = W, pady = 2, padx= 10)
        self.slopeResponse = Label(self.slopeSection, text="RWY Slope")
        self.slopeResponse.grid(row = 3, column = 1, sticky = W, pady = 2, padx= 10)

        # WEATHER --------------------------
        self.weatherSection = LabelFrame(self.containerTakeoff, text="Weather", font=self.h3)
        self.weatherSection.pack()

        self.windLabel = Label(self.weatherSection, text="Wind ---/--", font=self.defaultFont)
        self.windLabel.grid(row = 0, column = 0, sticky = W, pady = 2, padx= 10)
        self.windDirection = Entry(self.weatherSection, width=3, font=self.defaultFont)
        self.windDirection.grid(row = 0, column = 1, sticky = W, pady = 2, padx= 10)
        self.windLabelBar = Label(self.weatherSection, text="/", font=self.defaultFont)
        self.windLabelBar.grid(row = 0, column = 2, sticky = W, pady = 2, padx= 10)
        self.windSpeed = Entry(self.weatherSection, width=4, font=self.defaultFont)
        self.windSpeed.grid(row = 0, column = 3, sticky = W, pady = 2, padx= 10)

        self.oatLabel = Label(self.weatherSection, text="OAT °C", font=self.defaultFont)
        self.oatLabel.grid(row = 1, column = 0, sticky = W, pady = 2, padx= 10)
        self.oat = Entry(self.weatherSection, width=4, font=self.defaultFont)
        self.oat.grid(row = 1, column = 3, sticky = W, pady = 2, padx= 10)

        self.qnhLabel = Label(self.weatherSection, text="QNH hPa", font=self.defaultFont)
        self.qnhLabel.grid(row = 2, column = 0, sticky = W, pady = 2, padx= 10)
        self.qnh = Entry(self.weatherSection, width=4, font=self.defaultFont)
        self.qnh.grid(row = 2, column = 3, sticky = W, pady = 2, padx= 10)

        # exit Button
        self.exitButton = Button(self.containerExitButton, text="Exit", width=5, command=self.containerTakeoff.quit)
        self.exitButton.pack(side=RIGHT)

    def mudar_texto(self):
        try:
            dep = self.slopeDep.get()
            arr = self.slopeArr.get()
            rwyLength = self.rwyLength.get()
            if dep == "" or arr == "" or rwyLength == "":
                self.slopeResponse["text"] = "..."
            else:
                self.slopeResponse["text"] = round((((int(arr) - int(dep)) / int(rwyLength))*100),2)
        except:
            self.slopeResponse["text"] = "..."


root = Tk()
root.geometry("400x300")
root.title("A320 FBW Performance")
# root.resizable(width=0, height=0)
App(root)
root.mainloop()
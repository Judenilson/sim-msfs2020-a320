from tkinter import *
from tkinter import ttk

class App:
    def __init__(self, master=None):
        ve2 = (root.register(self.validate_entry2), "%P")
        ve4 = (root.register(self.validate_entry4), "%P")
        ve5 = (root.register(self.validate_entry5), "%P")
        vt = (root.register(self.validate_temperature), "%P")
        vd = (root.register(self.validate_degrees), "%P")

        self.defaultFont = ("Arial", "10")   
        self.h1 = ("verdana", 14, "italic", "bold")
        self.h2 = ("verdana", 12, "italic", "bold")
        self.h3 = ("verdana", 10, "bold")

        self.containerTakeoff = Frame(master, pady=10, bg="#888")
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
        self.slopeDep = Entry(self.slopeSection, width=5, font=self.defaultFont, validate= "key", validatecommand=ve4)
        self.slopeDep.grid(row = 0, column = 1, sticky = W, pady = 2, padx= 10)

        self.slopeOpositLabel = Label(self.slopeSection, text="Opposit THR elevation", font=self.defaultFont)
        self.slopeOpositLabel.grid(row = 1, column = 0, sticky = W, pady = 2, padx= 10)
        self.slopeOposit = Entry(self.slopeSection, width=5, font=self.defaultFont, validate= "key", validatecommand=ve4)
        self.slopeOposit.grid(row = 1, column = 1, sticky = W, pady = 2, padx= 10)

        self.rwyLengthLabel = Label(self.slopeSection, text="RWY Length in use", font=self.defaultFont)
        self.rwyLengthLabel.grid(row = 2, column = 0, sticky = W, pady = 2, padx= 10)
        self.rwyLength = Entry(self.slopeSection, width=5, font=self.defaultFont, validate= "key", validatecommand=ve5)
        self.rwyLength.grid(row = 2, column = 1, sticky = W, pady = 2, padx= 10)
    
        self.slopeButton = Button(self.slopeSection, text="Calculate", width=10, command=self.mudar_texto)
        self.slopeButton.grid(row = 3, column = 0, sticky = W, pady = 2, padx= 10)
        self.slopeResponse = Label(self.slopeSection, text="...", padx=8, font=self.h3)
        self.slopeResponse.grid(row = 3, column = 1, sticky = W, pady = 2, padx= 10)

        # WEATHER --------------------------
        self.weatherSection = LabelFrame(self.containerTakeoff, text="Weather", font=self.h3)
        self.weatherSection.pack()

        self.windLabel = Label(self.weatherSection, text="Wind ---/--", font=self.defaultFont)
        self.windLabel.grid(row = 0, column = 0, sticky = W, pady = 2, padx= 10)
        self.windDirection = Entry(self.weatherSection, width=3, font=self.defaultFont, validate= "key", validatecommand=vd)
        self.windDirection.grid(row = 0, column = 1, sticky = W, pady = 2, padx= 10)
        self.windLabelBar = Label(self.weatherSection, text="/", font=self.defaultFont)
        self.windLabelBar.grid(row = 0, column = 2, sticky = W, pady = 2, padx= 10)
        self.windSpeed = Entry(self.weatherSection, width=4, font=self.defaultFont, validate= "key", validatecommand=ve2)
        self.windSpeed.grid(row = 0, column = 3, sticky = W, pady = 2, padx= 10)

        self.oatLabel = Label(self.weatherSection, text="OAT °C", font=self.defaultFont)
        self.oatLabel.grid(row = 1, column = 0, sticky = W, pady = 2, padx= 10)
        self.oat = Entry(self.weatherSection, width=4, font=self.defaultFont, validate= "key", validatecommand=vt)
        self.oat.grid(row = 1, column = 3, sticky = W, pady = 2, padx= 10)

        self.qnhLabel = Label(self.weatherSection, text="QNH hPa", font=self.defaultFont)
        self.qnhLabel.grid(row = 2, column = 0, sticky = W, pady = 2, padx= 10)
        self.qnh = Entry(self.weatherSection, width=4, font=self.defaultFont,  validate= "key", validatecommand=ve4)
        self.qnh.grid(row = 2, column = 3, sticky = W, pady = 2, padx= 10)

        self.rwyConditionLabel = Label(self.weatherSection, text="RWY Condition", font=self.defaultFont)
        self.rwyConditionLabel.grid(row = 3, column = 0, sticky = W, pady = 2, padx= 10)
        condition_var = "Dry"
        self.rwyCondition = ttk.Combobox(self.weatherSection, width=12, font=self.defaultFont, textvariable=condition_var, state="readonly")
        self.rwyCondition["values"] = ("Dry", "Wet", "Water 6.3mm", "Water 12.7mm", "Slush 6.3mm", "Slush 12.7mm", "Comp. Snow")
        self.rwyCondition.current(0)
        self.rwyCondition.grid(row = 3, column = 1, columnspan=3, sticky = W, pady = 2, padx= 10)
        
        # exit Button
        self.exitButton = Button(self.containerExitButton, text="Exit", width=5, command=self.containerTakeoff.quit)
        self.exitButton.pack(side=RIGHT)

    def mudar_texto(self):
        try:
            dep = self.slopeDep.get()
            oposit = self.slopeOposit.get()
            rwyLength = self.rwyLength.get()
            if dep == "" or oposit == "" or rwyLength == "":
                self.slopeResponse["text"] = "..."
            else:
                self.slopeResponse["text"] = round((((int(dep) - int(oposit)) / int(rwyLength))*100),2)
        except:
            self.slopeResponse["text"] = "..."

    def validate_entry2(self,text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value < 100
    
    def validate_entry3(self,text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value < 1000
    
    def validate_entry4(self,text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value < 10000
    
    def validate_entry5(self,text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value < 100000
    
    def validate_degrees(self,text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 360
    
    def validate_temperature(self,text):
        if text == "": return True
        if text == "-": return True
        try:
            value = int(text)
        except ValueError:
            return False
        return -100 < value < 100
    


root = Tk()
root.geometry("400x300")
root.title("A320 FBW Performance")
# root.resizable(width=0, height=0)
App(root)
root.mainloop()
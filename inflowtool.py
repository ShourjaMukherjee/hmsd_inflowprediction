from tkinter import *
import pickle

def predict_inflow(a,b,c,d):
    with open("MLPmodel.pickle","rb") as f:
        model=pickle.load(f)
    inflow=model.predict([[a,b,c,d]])[0]
    display_output(str(inflow))
    return inflow

def display_output(output):
    label=Label(window,text="The predicted inflow is: "+ output[:10])
    label.grid(row=9,column=0)

window = Tk()
window.title("Inflow Prediction Tool")
window.geometry('400x400')
a = Label(window ,text = "Enter Precipitation").grid(row = 0,column = 0)
b = Label(window ,text = "Enter Evaporation").grid(row = 1,column = 0)
c = Label(window ,text = "Enter Previous Inflow value").grid(row = 2,column = 0)
d = Label(window ,text = "Enter Previous Inflow difference").grid(row = 3,column = 0)
a1 = Entry(window)
b1 = Entry(window)
c1 = Entry(window)
d1 = Entry(window)
btn = Button(window ,text="Submit",command= lambda: predict_inflow(float(a1.get()),float(b1.get()),float(c1.get()),float(d1.get()))).grid(row=4,column=0)
a1.grid(row = 0,column = 1)
b1.grid(row = 1,column = 1)
c1.grid(row = 2,column = 1)
d1.grid(row = 3,column = 1)

window.mainloop()

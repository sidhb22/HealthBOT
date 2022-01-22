from tkinter import *
from PIL import ImageTk, Image
a=Tk()
var=ImageTk.PhotoImage(Image.open("blue.jpg"))
var_1=Label(a, image=var).place(x=1, y=1)
def chatdis():
    msg=e.get()
    msg=str.lower(msg)
    send="You:"+msg
    txt.insert(END, "\n"+send)
    if msg== "hi" or msg== "hello" or msg== "anybody there?":
        txt.insert(END, "\n" + "Mr.Ted:Hi. How can I help you?")
    elif msg == "is omicron very dangerous?":
        txt.insert(END, "\n" + "Mr.Ted:Studies have shown that Omicron is milder but you take it seriously!")
    elif msg == "how do i prevent myself from covid?":
        txt.insert(END, "\n" + "Mr.Ted:Wear your mask, 6-feet distancing and sanitize your hand regularly")
        txt.insert(END, "\n" + "Mr.Ted:Also get vaccinated")
    elif msg=="i have some symptoms of covid":
        txt.insert(END, "\n" + "Mr.Ted:Please list them out.")
    elif msg == "fever 101 and dry cough":
        txt.insert(END, "\n" + "Mr.Ted:You can take paracetamol crocin every 6 hours.")
        txt.insert(END, "\n" + "Mr.Ted:If it doesnt reduce in 24 hrs, go to your nearest testing lab and contact your doctor.")
    elif msg == "can you order a self-test kit?":
        txt.insert(END, "\n" + "Mr.Ted:Yes I will place a order and it will reach you in 24 hrs.")
    elif msg == "bye":
        txt.insert(END, "\n" + "Mr.Ted:Bye")
        txt.insert(END, "\n" + "Mr.Ted:Take Care Stay Safe")
    else:
        txt.insert(END, "\n" + "I didn't understand your question")
    e.delete(0, END)
txt=Text(a)
a.title("Mr.Ted")
txt.grid(row=0, column=0, columnspan=2)
e=Entry(a, width=100)
send=Button(a, text="Send", command=chatdis).grid(row=1, column=1)
e.grid(row=1, column=0)
a.mainloop()
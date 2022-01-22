from tkinter import *
from PIL import ImageTk, Image
a=Tk()
def chatdis():
    msg=e.get()
    msg=str.lower(msg)
    send="You:"+msg
    txt.insert(END, "\n"+send)
    if msg== "hi" or msg== "hello" or msg== "anybody there?":
        txt.insert(END, "\n" + "Mr.Ted:Hi. How can I help you?")
    elif msg == "is omicron dangerous?":
        txt.insert(END, "\n" + "Mr.Ted:Studies have shown that Omicron is milder")
        txt.insert(END, "\n" + "Mr.Ted:But you take it seriously")
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
c1=Label(a, text="Things you can ask:").place(x=500, y=0)
c2=Label(a, text="1.Severity of Omicron").place(x=500, y=20)
c3=Label(a, text="2.Prevention from covid").place(x=500, y=40)
c4=Label(a, text="3.SOPs when having COVID symptoms").place(x=500, y=60)
c5=Label(a, text="4.Ordeing a Self-Test Kit").place(x=500, y=80)
e=Entry(a, width=100)
send=Button(a, text="Send", command=chatdis).grid(row=1, column=1)
e.grid(row=1, column=0)
a.mainloop()
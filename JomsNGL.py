from supabase import create_client
from tkinter import *
url = "https://wflctqihcpwthiurslqq.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndmbGN0cWloY3B3dGhpdXJzbHFxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwMzgwMjMsImV4cCI6MjA3MzYxNDAyM30.35KUeEfKNO6Teil9Gv0_aN6Q6S0K-9YWi-YDcZ6q-JY"
db = create_client(url,key)
sw = Tk()
sw.geometry("400x600")
sw.title("JomarNGL")
sw.iconbitmap("JOMS NGL.ico")
def exxit():
    sw.destroy()
def sendToDatabase():
    a = em.get()
    b = nm.get()
    c = msg.get()
    db.table("firstTryDB").insert({"Email":a,"Name":b, "Message": c }).execute()
    
    msg.delete(0,END)
    em.delete(0,END)
    nm.delete(0, END)
    tm.config(text="Sent SuccessFully!")
    exbtn.pack()
    
def send():
    global msg,tm,exbtn,em,nm
    Label(sw, text="Enter your Email").pack()
    em = Entry(sw,width=30)
    em.pack(pady=5)
    
    Label(sw, text="Enter your Name").pack()
    nm = Entry(sw,width=30)
    nm.pack(pady=5)
    
    Label(sw, text="Send me a Message").pack()
    msg = Entry(sw,width=30)
    msg.pack(pady=5)
    
    Button(text="Send",command=sendToDatabase).pack()
    tm = Label(sw,text='')
    tm.pack(pady=5)
    
    exbtn = Button(sw,text="Exit", command=exxit)
send()
sw.mainloop()
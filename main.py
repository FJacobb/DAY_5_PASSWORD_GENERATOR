import random
from tkinter import *
# import copy


def custom_generat():
    def on_enter2(e):
        generate['image'] = img6

    def on_leave2(e):
        generate['image'] = img5
    def password_generate():
        password = []
        box.delete(0, "end")
        for i in range(0, int(alph.get())):
            password.append(random.choice(alphabet))
        for i in range(0, int(num.get())):
            password.append(random.choice(numbers))
        for i in range(0, int(sym.get())):
            password.append(random.choice(symbol))
        random.shuffle(password)
        password = ''.join(password)
        return box.insert(0, password)
    canvers.create_text(35,80, text="Alphabet:", fill="#ffffff")
    canvers.create_text(33, 100, text="Number:", fill="#ffffff")
    canvers.create_text(110, 80, text="Symbol:", fill="#ffffff")
    alph = Entry(canvers, width=3,bg="#0C295B", fg="#ffffff")
    alph.place(x=63,y=72)
    num = Entry(canvers, width=3, bg="#0C295B", fg="#ffffff")
    num.place(x=63, y=92)
    sym = Entry(canvers, width=3, bg="#0C295B", fg="#ffffff")
    sym.place(x=132, y=72)
    generate = Button(canvers, image=img5, bg="#0C295B",border=0, command=password_generate)
    generate.place(x=84, y=120)
    generate.bind("<Enter>", on_enter2)
    generate.bind("<Leave>", on_leave2)





def normal_generat():
    password = []
    box.delete(0, "end")
    aph = random.randint(2, 8)
    nmb = random.randint(2, 8)
    sym = random.randint(2,8)
    if (aph+sym+nmb) >=8:
        for i in range(0, aph):
            password.append(random.choice(alphabet))
        for i in range(0, nmb):
            password.append(random.choice(numbers))
        for i in range(0, sym):
            password.append(random.choice(symbol))
        random.shuffle(password)
        password = ''.join(password)
        return box.insert(0, password)


def next():
    global box, canvers
    # def copy_text():
    #     copy.copy(box.get())
    def on_enter(e):
        customers['image'] = img4
    def on_leave(e):
        customers['image'] = img3

    def on_enter2(e):
        generate['image'] = img6

    def on_leave2(e):
        generate['image'] = img5
    start.destroy()
    bg = Label(home, image=img1)
    bg.place(x=-2,y=-1)
    canvers = Canvas(width=165, height=165)
    canvers.configure(bg="#001E5E",highlightthickness=0)
    box = Entry(canvers, width=20,border=0, bg="#0C295B", fg="#ffffff")
    box.place(x=10, y=50)
    Frame(canvers, width=125, height=1, bg="#ffffff").place(x=10, y=68)
    # Button(canvers, text="copy", bg="#0C295B", fg="#ffffff", border=0, command=copy_text, font=("arel", 7,"bold")).place(x=132,y=55)

    canvers.create_image(82,81, image=img2)
    customers = Button(canvers,image=img3, border=0,bg="#0C295B", command=custom_generat)
    customers.place(x=10, y=120)
    generate = Button(canvers, image=img5, border=0,bg="#0C295B", command=normal_generat)
    generate.place(x=84,y=120)
    customers.bind("<Enter>", on_enter)
    customers.bind("<Leave>", on_leave)
    generate.bind("<Enter>", on_enter2)
    generate.bind("<Leave>", on_leave2)
    canvers.place(x=200, y=20)
    name = canvers.create_text(65, 40, text="Generate password:", font=("arel", 9, "bold"), fill="#ffffff")
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]
symbol = [";","=","+","-","_","[","]","^","&","#","@","!",".",","]


home = Tk()
home.title("PASSWORD GENERATOR")
home.geometry("398x206")
img = PhotoImage(file="IMAGE/Asset 2.png")
img1 = PhotoImage(file="IMAGE/Asset 1.png")
img2 = PhotoImage(file="IMAGE/Asset 5.png")
img3 = PhotoImage(file="IMAGE/Asset 8.png")
img4 = PhotoImage(file="IMAGE/Asset 9.png")
img5 = PhotoImage(file="IMAGE/Asset 10.png")
img6 = PhotoImage(file="IMAGE/Asset 11.png")
start = Label(home, image=img)
start.place(x=-2,y=-1)
home.after(4000, next)

home.mainloop()
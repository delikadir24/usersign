from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk
window = Tk()
window.title("Kullanıcı Giriş Ekranı")
window.iconbitmap("C:/kisi.png")
window.geometry("390x220")
window.resizable(width=False, height=False)
resim = ImageTk.PhotoImage(Image.open("C:/kisi.png"))
lresim = Label(window,image=resim)
lresim.place(x=250,y=10)
L3 = Label(window)
L3.place(x=148,y=200)
def giris():
    if (E1.get() == str("admin")) and (E2.get() == str("1234")):
        L3['text'] = ("Giriş Başarılı...")
        messagebox.showinfo("Başlık", "Giriş Başarılı")
        print("başarılı")
    else:
        L3['text'] = ("Hatalı Giriş !")
        messagebox.showerror("Hata Başlık", "Hatalı Giriş")
L1 = Label(window, text="Kullanıcı Adı")
L1.place(x=75, y=15)
E1 = Entry(window, width=25)
E1.place(x=77,y=45)
L2 = Label(window, text="Şifre")
L2.place(x=75, y=80)
E2 = Entry(window, textvariable=StringVar(),show='*', width=25)
E2.place(x=77, y=110)
bt = Button(window, text="Giriş Yap", padx="20",pady="5", command=giris)
bt2 = Button(window, text="Çıkış",command=window.destroy,  padx="20",pady="5")
bt.place(x=75,y=150)
bt2.place(x=190,y=150)
window.mainloop()
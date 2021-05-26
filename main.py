import tkinter 
from tkinter import *
from PIL import Image, ImageTk

def kartaA():
    print("Karta katalogowa produktu")

def kartaB():
    print("Karta rodziny produktu")

def donothing():
    filewin = Toplevel(okno)
    filewin.geometry("100x100")
    button = Button(filewin, text="Nic nie robi...")
    button.pack()

tab_Ogolne = []
tab_Swietlne = []
tab_Elektryczne = []
tab_Pozostale = []
tab_Mechaniczne = []

def cleeenzaps():
    lo = len(tab_Ogolne)
    ls = len(tab_Swietlne)
    lp = len(tab_Pozostale)
    le = len(tab_Elektryczne)
    lm = len(tab_Mechaniczne)
    if lo > 0:
        tab_Ogolne.clear()
    if ls > 0:
        tab_Swietlne.clear()
    if lp > 0:
        tab_Pozostale.clear()
    if le > 0:
        tab_Elektryczne.clear()
    if lm > 0:
        tab_Mechaniczne.clear()

def zapisz_zebrane_dane():
    cleeenzaps()
    tab_Ogolne.append(l_E12.get())
    tab_Ogolne.append(l_E13.get())
    tab_Ogolne.append(l_E14.get())
    tab_Ogolne.append(l_E16.get())
    tab_Ogolne.append(l_E17.get())
    tab_Ogolne.append(l_E18.get())
    tab_Ogolne.append(l_E19.get())
    tab_Ogolne.append(l_E20.get())
    tab_Ogolne.append(l_E21.get())
    tab_Ogolne.append(l_E22.get())
    tab_Ogolne.append(l_E23.get())
    print("OGOLNE")
    print(tab_Ogolne)
    tab_Elektryczne.append(l_E25.get())
    tab_Elektryczne.append(l_E26.get())
    print("elektryczne")
    print(tab_Elektryczne)
    tab_Swietlne.append(p_E14.get())
    tab_Swietlne.append(p_E14.get())
    tab_Swietlne.append(p_E15.get())
    tab_Swietlne.append(p_E16.get())
    tab_Swietlne.append(p_E17.get())
    tab_Swietlne.append(p_E18.get())
    tab_Swietlne.append(p_E19.get())
    tab_Swietlne.append(p_E20.get())
    print("Swietlne")
    print(tab_Swietlne)

def pokazSchemat():
    schem = Toplevel(okno)
    lab=Label(schem, text=tab_Ogolne)
    lab.pack()



okno = tkinter.Tk()
okno.geometry("1200x600")
okno.title("Generator Kart ver 1.2")

ico = Image.open('IkonGEN.png')
photo = ImageTk.PhotoImage(ico)
okno.wm_iconphoto(False, photo)


menubar = Menu(okno)

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="Nowy", command = donothing)
filemenu.add_command(label = "Otwórz", command = donothing)
filemenu.add_command(label = "Zapisz", command = donothing)
filemenu.add_command(label = "Zapisz jako...", command = donothing)
filemenu.add_command(label = "Zamknij", command = donothing)

filemenu.add_separator()

filemenu.add_command(label = "Exit", command = okno.quit)
menubar.add_cascade(label = "Plik", menu = filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label = "Cofnij", command = donothing)

editmenu.add_separator()

editmenu.add_command(label = "Wytnij", command = donothing)
editmenu.add_command(label = "Kopiuj", command = donothing)
editmenu.add_command(label = "Wklej", command = donothing)
editmenu.add_command(label = "Skasuj", command = donothing)
editmenu.add_command(label = "Wybierz wszystko", command = donothing)

menubar.add_cascade(label = "Edytuj", menu = editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label = "Pomoc menu", command = donothing)
helpmenu.add_command(label = "O aplikacji...", command = donothing)
menubar.add_cascade(label = "Pomoc", menu = helpmenu)



var = StringVar()
#var2 = StringVar()

#scrollbar = Scrollbar(okno)
#scrollbar.pack( side = RIGHT, fill = Y )
def sel():
       selection = " " + str(var.get())
       label.config(text = selection)


teksty=["Zastosowanie","Cechy produktu","Zdjęcie","Rys. techniczny","Krzywa rozsyłu","Nagłówek","Produkt","Rodzina","Parametry"]




# fundamenty aplikacji
o_L1 = Label(okno, text = teksty[5])
o_L1.place(x = 10,y = 10)

o_E1 = Entry(okno, bd = 5, width=50)
o_E1.place(x = 100,y = 10)

o_B1 = Button(okno, text = teksty[6],relief=RAISED, command = kartaA)
o_B1.place(x = 420,y = 10)

o_B2 = Button(okno, text = teksty[7],relief=RAISED, command = kartaB)
o_B2.place(x = 490,y = 10)

o_L2 = Label(okno,text = teksty[2])
o_L2.place(x = 10,y = 50)

o_E2 = Entry(okno,bd = 5, width=50)
o_E2.place(x = 100,y = 50)

o_L3 = Label(okno,text = teksty[0])
o_L3.place(x = 10,y = 100)

o_E3 = Entry(okno,bd = 5, width=50)
o_E3.place(x = 100,y = 100)

o_L4 = Label(okno,text = teksty[1])
o_L4.place(x = 10,y = 150)

o_E5 = Entry(okno,bd = 5, width=50)
o_E5.place(x = 100,y = 150)

o_L6 = Label(okno,text = teksty[3])
o_L6.place(x = 10,y = 200)

o_E7 = Entry(okno,bd = 5, width=50)
o_E7.place(x = 100,y = 200)

o_L8 = Label(okno,text = teksty[4])
o_L8.place(x = 10,y = 250)

o_E9 = Entry(okno,bd = 5, width=50)
o_E9.place(x = 100,y = 250)

o_L11 = Label(okno, text = "Oświadczenie")
o_L11.place(x = 10,y = 300)

o_E11 = Entry(okno,bd = 5, width=50)
o_E11.insert(0," Zastrzega się możliwość zmian bez uprzedzenia. Błędy i ominięcia są możliwe. Należy zawsze upewnić się czy korzystasz z najnowszej wersji dokumentu.")
o_E11.place(x = 100,y = 300)

o_L12 = Label(okno, text = "Data")
o_L12.place(x = 10,y = 350)

o_E12 = Entry(okno,bd = 5, width=50)
o_E12.insert(0," 13 stycznia 2020 ")
o_E12.place(x = 100,y = 350)

o_Entry_tolerancja1=Entry(okno,bd=5)
o_Entry_tolerancja1.insert(0,"* tolerancja mocy 5 %")
o_Entry_tolerancja1.place(x=10, y=400)

o_Entry_tolerancja2=Entry(okno,bd=5,width=60)
o_Entry_tolerancja2.insert(0,"** tolerancja strumienia świetlnego 7% w temp. otoczenia 25°C")
o_Entry_tolerancja2.place(x=10, y=450)



# druga strona z parametrami
# parametry
o_L10 = Label(okno,text = teksty[8] ,fg="chocolate",relief = GROOVE)
o_L10.place(x = 510, y = 50)
# kolumna 1 , fragment 1/2  x= 450; fragment 2/2 x=600; roznica w "y" to 20
l_L11 = Label(okno,text = "Ogólne", fg="green" ,relief = GROOVE)
l_L11.place(x = 450, y = 70)

l_L12 = Label(okno, text ="Kod produktu")
l_L12.place(x = 450,y = 90)

l_E12 = Entry(okno, bd = 5)
l_E12.insert(0,"NULL")
l_E12.place(x = 600,y = 90)

l_L13 = Label(okno, text ="Kod rodziny produktu")
l_L13.place(x = 450,y = 110)

l_E13 = Entry(okno, bd = 5)
l_E13.insert(0,"NULL")
l_E13.place(x = 600,y = 110)

l_L14 = Label(okno, text ="Kod barwy")
l_L14.place(x = 450,y = 130)

l_E14 = Entry(okno, bd = 5)
l_E14.insert(0,"NULL")
l_E14.place(x = 600,y = 130)

l_L15 = Label(okno, text ="Wbudowany zasilacz")
l_L15.place(x = 450,y = 150)

l_w = Radiobutton ( okno, text = "Tak", variable = var,  value = "Tak"  ,command = sel  )
l_w.place(x=600,y=150)

l_w2 = Radiobutton ( okno, text = "Nie", variable = var,  value = "Nie"  ,command = sel )
l_w2.place(x=630,y=150)

label = Label(okno,fg="green")
label.place(x=680,y=150)

l_L16 = Label(okno, text ="Producent zasilacza")
l_L16.place(x = 450,y = 170)

l_E16 = Entry(okno, bd = 5)
l_E16.insert(0,"NULL")
l_E16.place(x = 600,y = 170)

l_L17 = Label(okno, text ="Sterowanie")
l_L17.place(x = 450,y = 190)

l_E17 = Entry(okno, bd = 5)
l_E17.insert(0,"NULL")
l_E17.place(x = 600,y = 190)

l_L18 = Label(okno, text ="Klasa ochronności")
l_L18.place(x = 450,y = 210)

l_E18 = Entry(okno, bd = 5)
l_E18.insert(0,"NULL")
l_E18.place(x = 600,y = 210)

l_L19 = Label(okno, text ="Stopień ochrony")
l_L19.place(x = 450,y = 230)

l_E19 = Entry(okno, bd = 5)
l_E19.insert(0,"NULL")
l_E19.place(x = 600,y = 230)

l_L20 = Label(okno, text ="Odporność na uderzenia")
l_L20.place(x = 450,y = 250)

l_E20 = Entry(okno, bd = 5)
l_E20.insert(0,"NULL")
l_E20.place(x = 600,y = 250)

l_L21 = Label(okno, text ="Kolor")
l_L21.place(x = 450,y = 270)

l_E21 = Entry(okno, bd = 5)
l_E21.insert(0,"NULL")
l_E21.place(x = 600,y = 270)

l_L22 = Label(okno, text ="Producent źródeł światła")
l_L22.place(x = 450,y = 290)

l_E22 = Entry(okno, bd = 5)
l_E22.insert(0,"NULL")
l_E22.place(x = 600,y = 290)

l_L23 = Label(okno, text ="Ilość źródeł światła ")
l_L23.place(x = 450,y = 310)

l_E23 = Entry(okno, bd = 5)
l_E23.insert(0,"NULL")
l_E23.place(x = 600,y = 310)

l_L24 = Label(okno,text = "Elektryczne",fg="green" ,relief = GROOVE)
l_L24.place(x = 450, y = 330)

l_L25 = Label(okno, text ="Napięcie znamionowe")
l_L25.place(x = 450,y = 350)

l_E25 = Entry(okno, bd = 5)
l_E25.insert(0,"NULL")
l_E25.place(x = 600,y = 350)

l_L26 = Label(okno, text ="Częstotliwość sieciowa ")
l_L26.place(x = 450,y = 370)

l_E26 = Entry(okno, bd = 5)
l_E26.insert(0,"NULL")
l_E26.place(x = 600,y = 370)

# kolumna 2 fragment 1/2  x = 750; fragment 2/2 x=950; roznica w "y" to 20
p_L13 = Label(okno,text = "Świetlne", fg="green", relief = GROOVE)
p_L13.place(x = 750, y = 70)

p_L14 = Label(okno, text ="Moc znamionowa")
p_L14.place(x = 750,y = 90)

p_E14 = Entry(okno, bd = 5)
p_E14.insert(0,"NULL")
p_E14.place(x = 950,y = 90)

p_L15 = Label(okno, text ="Strumień świetlny oprawy")
p_L15.place(x = 750,y = 110)

p_E15 = Entry(okno, bd = 5)
p_E15.insert(0,"NULL")
p_E15.place(x = 950,y = 110)

p_L16 = Label(okno, text ="Wydajność oprawy")
p_L16.place(x = 750,y = 130)

p_E16 = Entry(okno, bd = 5)
p_E16.insert(0,"NULL")
p_E16.place(x = 950,y = 130)

p_L17 = Label(okno, text ="CRI/Ra")
p_L17.place(x = 750,y = 150)

p_E17 = Entry(okno, bd = 5)
p_E17.insert(0,"NULL")
p_E17.place(x = 950,y = 150)

p_L18 = Label(okno, text ="Temperatura barwowa")
p_L18.place(x = 750,y = 170)

p_E18 = Entry(okno, bd = 5)
p_E18.insert(0,"NULL")
p_E18.place(x = 950,y = 170)

p_L19 = Label(okno, text ="Barwa światła")
p_L19.place(x = 750,y = 190)

p_E19 = Entry(okno, bd = 5)
p_E19.insert(0,"NULL")
p_E19.place(x = 950,y = 190)

p_L20 = Label(okno, text ="Kąt rozsyłu")
p_L20.place(x = 750,y = 210)

p_E20 = Entry(okno, bd = 5)
p_E20.insert(0,"NULL")
p_E20.place(x = 950,y = 210)

p_L21 = Label(okno,text = "Pozostałe" ,fg="green", relief = GROOVE)
p_L21.place(x = 750, y = 230)

p_L22 = Label(okno, text ="Waga")
p_L22.place(x = 750,y = 250)

p_E22 = Entry(okno, bd = 5)
p_E22.insert(0,"NULL")
p_E22.place(x = 950,y = 250)

p_L23 = Label(okno, text ="Żywotność")
p_L23.place(x = 750,y = 270)

p_E23 = Entry(okno, bd = 5)
p_E23.insert(0,"NULL")
p_E23.place(x = 950,y = 270)

p_L24 = Label(okno, text ="Żywotność L90B10")
p_L24.place(x = 750,y = 290)

p_E24 = Entry(okno, bd = 5)
p_E24.insert(0,"NULL")
p_E24.place(x = 950,y = 290)

p_L25 = Label(okno, text ="Żywotność L80B10")
p_L25.place(x = 750,y = 310)

p_E25 = Entry(okno, bd = 5)
p_E25.insert(0,"NULL")
p_E25.place(x = 950,y = 310)

p_L26 = Label(okno, text ="Żywotność L70B10")
p_L26.place(x = 750,y = 330)

p_E26 = Entry(okno, bd = 5)
p_E26.insert(0,"NULL")
p_E26.place(x = 950,y = 330)

p_L27 = Label(okno, text ="Sposób montażu ")
p_L27.place(x = 750,y = 350)

p_E27 = Entry(okno, bd = 5)
p_E27.insert(0,"NULL")
p_E27.place(x = 950,y = 350)

p_L28 = Label(okno, text ="Zakres temperatur otoczenia ")
p_L28.place(x = 750,y = 370)

p_E28 = Entry(okno, bd = 5)
p_E28.insert(0,"NULL")
p_E28.place(x = 950,y = 370)


p_L29 = Label(okno,text = "Mechaniczne",fg="green" , relief = GROOVE)
p_L29.place(x = 750, y = 390)

p_L30 = Label(okno, text ="Materiał obudowy")
p_L30.place(x = 750,y = 410)

p_E30 = Entry(okno, bd = 5)
p_E30.insert(0,"NULL")
p_E30.place(x = 950,y = 410)

p_L31 = Label(okno, text ="Materiał klosza")
p_L31.place(x = 750,y = 430)

p_E31 = Entry(okno, bd = 5)
p_E31.insert(0,"NULL")
p_E31.place(x = 950,y = 430)

p_L32 = Label(okno, text ="Wymiary (A x B x C mm)")
p_L32.place(x = 750,y = 450)

p_E32 = Entry(okno, bd = 5)
p_E32.insert(0,"NULL")
p_E32.place(x = 950,y = 450)


p_L33 = Label(okno, text ="Wymiary (Ø x D mm)")
p_L33.place(x = 750,y = 470)

p_E33 = Entry(okno, bd = 5)
p_E33.insert(0,"NULL")
p_E33.place(x = 950,y = 470)



# guziki do kreacji danych
btn_submit = Button(okno,text = "Zapisz dane karty ", relief=RAISED, command = zapisz_zebrane_dane)
btn_submit.place(x=1000,y=530)

btn_pokaz = Button(okno,text = "Pokaz wynik ", relief=RAISED, command = pokazSchemat)
btn_pokaz.place(x=920,y=530)



okno.config(menu = menubar)
okno.mainloop()


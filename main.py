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
"""
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
    tab_Pozostale.append()
"""
def pokazSchemat():
    schem = Toplevel(okno)
    lab=Label(schem, text=tab_Ogolne)
    lab.pack()
    lab2=Label(schem, text=tab_Swietlne)
    lab2.pack()
    lab3=Label(schem, text=tab_Elektryczne)
    lab3.pack()

def automatyczna_PozycjaWTabeli(strona,numer_pozycji,tekst,wsad_wejsciowy,pozycjaStartowaX,pozycjaStartowaY ,roznica_y,root,przesuniecie):
    st=strona
    nr = numer_pozycji
    tx = tekst
    ws=wsad_wejsciowy
    pzS_X=pozycjaStartowaX
    pzS_Y=pozycjaStartowaY
    #x_plus=roznica_x
    y_plus=roznica_y
    przez=przesuniecie
    starLabel= st + "_L"+str(nr)
    print(starLabel)
    starEntry =st + "_E"+str(nr)
    print(starEntry)
    starLabel = Label(root, text=tx)
    xx = pzS_X # +x_plus
    yy = pzS_Y+y_plus
    starLabel.place(x=xx,y=yy)
    starEntry=Entry(root, bd = 5)
    starEntry.insert(0,ws)
    xxx=xx+przez
    starEntry.place(x=xxx,y=yy)
    print("Label")
    print("Entry")

okno = tkinter.Tk()
okno.geometry("1200x800")
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
#def sel():
 #      selection = " " + str(var.get())
 #      label.config(text = selection)


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
# kolumna 1 , fragment 1/2  x= 450; fragment 2/2 x=650; roznica w "y" to 20

l_L11 = Label(okno,text = "Ogólne", fg="green" ,relief = GROOVE)
l_L11.place(x = 450, y = 70)

tab_Parametry_Ogolne = ["Kod produktu","Kod rodziny produktu","Kod barwy","Wbudowany zasilacz","Producent zasilacza","Sterowanie","Klasa ochronności","Stopień ochrony","Odporność na uderzenia","Kolor","Producent źródeł światła","Ilość źródeł światła "]
x_Ogolne = 450
y_Ogolne = 70
przesuniecie = 150
roznicaY = 30
pozz= 1
for x in tab_Parametry_Ogolne:
    automatyczna_PozycjaWTabeli("l",pozz,x,"Null",x_Ogolne,y_Ogolne,roznicaY,okno,przesuniecie)
    pozz+=1
    y_Ogolne+=roznicaY


l_L24 = Label(okno,text = "Elektryczne",fg="green" ,relief = GROOVE)
y_Ogolne+=roznicaY
l_L24.place(x = x_Ogolne, y = y_Ogolne)

tab_Parametry_Elektryczne =["Napięcie znamionowe","Częstotliwość sieciowa "]

for x in tab_Parametry_Elektryczne:
    automatyczna_PozycjaWTabeli("l",pozz,x,"Null",x_Ogolne,y_Ogolne,roznicaY,okno,przesuniecie)
    pozz+=1
    y_Ogolne+=roznicaY


# kolumna 2 fragment 1/2  x = 750; fragment 2/2 x=950; roznica w "y" to 20
x_OgolnePrawe= 750
y_Ogolne = 70
pozz = 1
tab_Parametry_Swietlne=["Moc znamionowa","Strumień świetlny oprawy","Wydajność oprawy","CRI/Ra","Temperatura barwowa","Barwa światła","Kąt rozsyłu"]

p_L13 = Label(okno,text = "Świetlne", fg="green", relief = GROOVE)
p_L13.place(x = 750, y = 70)


for x in tab_Parametry_Swietlne:
    automatyczna_PozycjaWTabeli("p",pozz,x,"Null",x_OgolnePrawe,y_Ogolne,roznicaY,okno,przesuniecie)
    pozz+=1
    y_Ogolne+=roznicaY



p_L21 = Label(okno,text = "Pozostałe" ,fg="green", relief = GROOVE)
y_Ogolne+=roznicaY
p_L21.place(x = x_OgolnePrawe, y = y_Ogolne)

tab_Parametry_Pozostale = ["Waga","Żywotność","Żywotność L90B10","Żywotność L80B10","Żywotność L70B10","Sposób montażu ","Zakres temp. otoczenia "]

for x in tab_Parametry_Pozostale:
    automatyczna_PozycjaWTabeli("p",pozz,x,"Null",x_OgolnePrawe,y_Ogolne,roznicaY,okno,przesuniecie)
    pozz+=1
    y_Ogolne+=roznicaY




p_L29 = Label(okno,text = "Mechaniczne",fg="green" , relief = GROOVE)
y_Ogolne+=roznicaY
p_L29.place(x = x_OgolnePrawe, y = y_Ogolne)

tab_Parametry_Mechaniczne=["Materiał obudowy","Materiał klosza","Wymiary (A x B x C mm)","Wymiary (Ø x D mm)"]

for x in tab_Parametry_Mechaniczne:
    automatyczna_PozycjaWTabeli("p",pozz,x,"Null",x_OgolnePrawe,y_Ogolne,roznicaY,okno,przesuniecie)
    pozz+=1
    y_Ogolne+=roznicaY




# automatyczna_PozycjaWTabeli("l",40,"testowanie automatu","NULL",200,500,20,okno,150)

# guziki do kreacji danych
#btn_submit = Button(okno,text = "Zapisz dane karty ", relief=RAISED, command = zapisz_zebrane_dane)
#btn_submit.place(x=1000,y=530)

#btn_pokaz = Button(okno,text = "Pokaz wynik ", relief=RAISED, command = pokazSchemat)
#btn_pokaz.place(x=920,y=530)



okno.config(menu = menubar)
okno.mainloop()


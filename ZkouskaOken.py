import tkinter as tk
      
okno = tk.Tk()
okno.title("Smetana")
okno.geometry("300x300")
            
#text
label = tk.Label(okno, text="Nivniwho?")
label.pack()
            
#textové pole
vstup = tk.Entry(okno)
vstup.pack()
            
#tlačítko co pracuje s textovým polem
def coJsiNapsal():
    text = vstup.get()
    print(text)
tlačitko = tk.Button(okno, text="Co jsem napsal?", bg="yellow", command =coJsiNapsal)
tlačitko.pack()
#tlačítko
tlačitko2 = tk.Button(okno, text="KONEC!", bg="red", command =okno.destroy)
tlačitko2.pack()


#celkem nechápu
"""
def prepis():
    vysledek.config(text="Nový text")
tlacitko = tk.Button(okno, text="Přepiš text", command=prepis)
vstup = tk.Entry(okno)
vstup.pack()
vysledek = tk.Label(okno, text="Zatím jsi nic nenapsal")
vysledek.pack()
tlacitko.pack()
"""
nezamestnany = tk.BooleanVar()
checkbox = tk.Checkbutton(okno, text="Jsi zaměstnaný", variable=nezamestnany)
checkbox.pack()

jmena = tk.StringVar()
tk.Radiobutton(okno, text="Karel", variable=jmena, value="Karel").pack()

okno.mainloop()
            